#Lecture 13 Final:
# CE 895
# Mar 2017 jkroundy@ku.edu

import sys
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


#Autocorrelation function
def acf(x,nac):
	nn = x.shape[0]
	acf = np.zeros((nac,2))
	for lag in xrange(nac):
		acf[lag,:] = stats.pearsonr(x[:nn-lag],x[lag:])
	return acf

#When will lake Mead/Powell go dry?

#Import data from Lee's Ferry
fname = 'Lees_Ferry_1906_2014.csv'
dd = np.loadtxt(fname, skiprows=1,delimiter=',',dtype=np.int,usecols=(0,1))
tflow = np.loadtxt(fname, skiprows=1,delimiter=',',dtype=np.float,usecols=(2))


#Create the variable "aflow" for the Annual Flows based on Water Year (Oct-Sep) 1906-2014 stored in the variable "yrs".
# Then Plot the results
tyrs = np.unique(dd[:,1])
n = tyrs.shape[0]-1  #total years in data
aflow = np.zeros((n,))
yrs = np.zeros((n,),dtype=np.int)
ic = 0
inc = 12
for i in xrange(n):
	aflow[i] = tflow[ic:ic+inc].sum()/10**6
	yrs[i] = dd[ic+inc-1,1]
	ic = ic + inc 

w = 8.5 #width of figure [inches]
h = 11.0 #height of figure [inches]
yfac = w/h
fig = plt.figure(figsize=(w,h))
ax = plt.axes([0.1,0.55,0.8,0.3]) #create a plot axes
bf = 2
xx = [yrs.min()-bf,yrs.max()+bf]
yy = np.ones((2,))*aflow.mean()
ax.plot(xx,yy,color=[1,0,0],linestyle='--',linewidth=2,marker='',markerfacecolor=[0,0,1],markeredgecolor=[0,0,0],markersize=8)
ax.plot(yrs,aflow,color=[0,0,1],linestyle='-',linewidth=2,marker='o',markerfacecolor=[0,0,1],markeredgecolor=[0,0,0],markersize=5)
ax.set_xlim(xx)
ax.set_title(r'Colorado River at Lees Ferry 1906-2014')
ax.set_ylabel(r'Streamflow Flow [MAF]')
ax.set_xlabel(r'Water Year')
plt.savefig('./Lees_Ferry_Annual_Flow_Timesereis.pdf',format='pdf',bbox_inches='tight')#Save the plot as a PDF



#Calculate and Plot the Autocorrelation function for Annual Flow
nac = 7
acfT = acf(aflow,nac) #Calls function
p1 = acfT[1,0]

w = 8.5 #width of figure [inches]
h = 11.0 #height of figure [inches]
yfac = w/h
fig = plt.figure(figsize=(w,h))
ax = plt.axes([0.1,0.55,0.8,0.3]) #create a plot axes
x = np.array(xrange(nac))
xx = [-0.50,nac-0.5]
ax.plot(x,acfT[:,0],color=[0,0,0],linestyle='-',linewidth=2,marker='',markerfacecolor=[0,0,1],markeredgecolor=[0,0,0],markersize=8)
sidx = acfT[:,1] < 0.05
ax.plot(x[sidx],acfT[sidx,0],color=[1,0,0],linestyle='',linewidth=2,marker='o',markerfacecolor=[1,0,0],markeredgecolor=[1,0,0],markersize=8,label='Significant')
ax.plot(x[~sidx],acfT[~sidx,0],color=[0,0,0],linestyle='',linewidth=2,marker='s',markerfacecolor=[0,0,0],markeredgecolor=[0,0,0],markersize=8,label='Not Significant')
ax.plot(xx,[0,0],color=[1,0,0],linestyle='--',linewidth=2,marker='',markerfacecolor=[0,0,1],markeredgecolor=[0,0,0],markersize=8)
ax.set_xlim(xx)
ax.set_ylabel(r'Correlation [-]')
ax.set_xlabel(r'Temporal Lag [years]')
ax.set_title(r'Autocorrelation Function')
plt.legend(bbox_to_anchor=(0.6, 0.8, 0.38, .3), loc=8,ncol=1, mode="expand", borderaxespad=0.,numpoints=1,fontsize=12,markerscale=1)
plt.savefig('./Lees_Ferry_Autocorrelation.pdf',format='pdf',bbox_inches='tight')#Save the plot as a PDF


#Generate 10,000 simulations of 50 years of flow using a random normal model. Inilize the model with observed flow in 2014. 
#Then Make a plot of the mean, standard deviation and lag-1 correlation for the 50 years of data and compare this to the 
# observations.

#Generate Synthetic Streamflow
nn = 50 # Number of years to predict
mm = 10000 #Number of simulations

#Generate Random Normal Variables
np.random.seed(19) # The seed initializes the random number generator
zn = stats.norm.rvs(0,1.0,(nn,mm))# Generate random number from a normal distribution wiht a mean of 0 and std of 1


#Set up  other variables 
sx = aflow.std(ddof=1) #Standard deviation for streamflow
mx = aflow.mean() #Mean for streamflow
initflow = 14.14 #MAF
eta = np.sqrt(((n-1)/(n-2))*(1-p1**2)*sx**2)
xt = np.ones((1,mm))*initflow # Inital flow variable
sflow = np.zeros((nn,mm)) #Synthetic Stream flow variable

for i in xrange(nn):
	sflow[i,:] = mx + p1*(xt-mx) + eta*zn[i,:] #Get synetic flow for the next year 
	xt = sflow[i,:] #save for next time step calculation


#Make plots
w = 11.0 #width of figure [inches]
h = 8.5 #height of figure [inches]
yfac = w/h
fig = plt.figure(figsize=(w,h))

# For the Mean
x = sflow.mean(0)
xo = mx*np.ones((2))
xx = np.array([0.5,1.5])
ax = plt.axes([0.1,0.1,0.2,0.4*yfac])
ax.plot(xx,xo,color=[1,0,0],linestyle='--',linewidth=2,marker='',markerfacecolor=[1,0,0],markeredgecolor=[1,0,0],markersize=12)
plt.boxplot(x,whis = 1.5)
ax.get_xaxis().set_ticks([])
ax.set_xlim(xx)
ax.set_ylabel(r'Mean  [MAF]')
ax.set_title('Mean of Synthetic Time series')

# For the Std
x = sflow.std(0,ddof=1)
xo = sx*np.ones((2))
xx = np.array([0.5,1.5])
ax = plt.axes([0.4,0.1,0.2,0.4*yfac])
ax.plot(xx,xo,color=[1,0,0],linestyle='--',linewidth=2,marker='',markerfacecolor=[1,0,0],markeredgecolor=[1,0,0],markersize=12)
plt.boxplot(x,whis = 1.5)
ax.get_xaxis().set_ticks([])
ax.set_xlim(xx)
ax.set_ylabel(r'Std  [MAF]')
ax.set_title('Std of Synthetic Time series')

# For the lag-1 Correlation
x = np.zeros((mm,))
for i in xrange(mm):
	x[i] = stats.pearsonr(sflow[:nn-1,i],sflow[1:,i])[0]
xo = p1*np.ones((2))
xx = np.array([0.5,1.5])
ax = plt.axes([0.7,0.1,0.2,0.4*yfac])
ax.plot(xx,xo,color=[1,0,0],linestyle='--',linewidth=2,marker='',markerfacecolor=[1,0,0],markeredgecolor=[1,0,0],markersize=12)
plt.boxplot(x,whis = 1.5)
ax.get_xaxis().set_ticks([])
ax.set_xlim(xx)
ax.set_ylabel(r'Correlation  [-]')
ax.set_title('Lag-1 Correlation of Synthetic Time series')

plt.savefig('./Synthetic_Schematic.pdf',format='pdf',bbox_inches='tight')#Save the plot as a PDF



#4) For every synthetic streamflow relization, determine the combined storage of Lake Mead and Powell over the 50 years following 2014. At the begining of November 2014 the combined storage of 
# Lake Mead and Powell is about 24.5 MAF. Assume there is 15.0 MAF of water use every year. Create a graph of the probability that the reservoir system goes above 50 MAF from 2015 to 2064 
# based on the synthetic storage data.

ints = 24.5 # Initial Storage [MAF]
syrs = np.arange(nn)+2014+1 # Create array for future years
stor = np.zeros((nn,mm)) #Create array for storage
xs = ints *np.ones((mm)) #Create array for inital storage
pe = np.zeros((nn,)) #Create array for Probablity greater than 50 MAF
et = 1.7 #Annual evapotranspiration in MAF
wu = 0.0192*((i+2015)-2008) + 13.7 #MAF
for i in xrange(nn):
	stor[i,:] = xs + sflow[i,:] -1.7 - [0.0192*((i+2015)-2008)+13.7]
	xs = stor[i,:]
	idx = stor[i,:] < 0
	pe[i] = idx.sum()/float(mm)

 
#Make Storage Probabilty Plot
h = 11.0 #width of figure [inches]
w = 8.5 #height of figure [inches]
yfac = w/h
fig = plt.figure(figsize=(w,h))
ax = plt.axes([0.1,0.1,0.5,0.5*yfac])
ax.plot(syrs,pe,color=[1,0,0],linestyle='-',linewidth=2,marker='o',markerfacecolor=[1,0,0],markeredgecolor=[1,0,0],markersize=4)
ax.set_ylabel(r'Probability  [-]')
ax.set_xlabel(r'Water Year  [-]')
ax.set_title('Probability that Lakes Mead & Powell Go Dry')


plt.savefig('./Probability_Runs_Dry.pdf',format='pdf',bbox_inches='tight')#Save the plot as a PDF







plt.show()

