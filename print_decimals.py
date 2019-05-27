# A simple program to print the numbers pi or e to n number of digits provided by the user

import math as math

prompt1 = "Please enter your menu choice: "
prompt2 = "Please enter your choice of decimal places: "
menulist = ["A", "B", "C"]

while True:
    # Printing welcome message and main menu
    print("\n---Welcome to the Python decimal machine!---")
    print("Here, you can view various numbers to your choice of deimcal places.")
    print("""
        a. Pi
        b. e
        c. both
        d. exit
        """)

    # Grabbing user input for menu choice and exiting if necessary
    # Also controlling for user input, accepting only menu options
    choice_num = input("Please select a menu option: ")
    if choice_num.title() == "D":
        break
    elif choice_num.title() not in menulist:
        print("\nSorry, that isn't a valid menu selection. Please try again.")
        continue

    # Grabbing user input for decimal selection
    while True:
        decimal_num = input("\nPlease choose the number of decimal places you'd like to see: ")
        # Ensuring that the program only accepts integers between 0 and 50
        try:
            int(decimal_num)
        except ValueError:
            print("\nYou typed a letter. Please type an integer")
        else:
            decimal_num = int(decimal_num)

        if decimal_num not in range(0, 51):
            print("\nThis number is out of range. Please enter an integer between 0 and 50.")
        else:
            break

    # Printing appropriate outputs
    if choice_num.title() == "A":
        print("{:.{}f}".format(math.pi, decimal_num))
    elif choice_num.title() == "B":
        print("{:.{}f}".format(math.e, decimal_num))
    else:
        print("{:.{}f}".format(math.pi, decimal_num))
        print("{:.{}f}".format(math.e, decimal_num))
