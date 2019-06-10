# A program to solve a variety of mortgage calculation problems for the user


def main():
    """A function to serve as the main menu of the program"""
    while True:
        print("\n~~~Welcome to the Python Mortgage calculator!~~~")
        print("Depending on the information available, I can calculate two things: ")
        print("1) Your monthly mortgage payment")
        print("2) How much time is left on your mortgage")

        answer = ''
        choice_input = input("Please select one of the two options (or 'Q' to quit): ")

        if choice_input.title() == "Q":
            break
        elif choice_input.title() == "1":
            answer = get_payment()
        elif choice_input.title() == "2":
            answer = get_term_length()
        else:
            print("\nInvalid input, returning to main...")
            continue

        show_results(answer, choice_input)


def get_payment():
    """A function to calculate the user's monthly mortgage payment"""
    principal, interest_rate, compound_interval, length = get_info("1")
    interest_rate = float(interest_rate) / 100
    principal = float(principal)
    length = float(length)
    if compound_interval == '1':
        payment = principal * (((interest_rate / 12) * (1 + interest_rate / 12)**(length * 12)) /
                               ((1 + interest_rate / 12)**(length * 12) - 1))
        return payment
    elif compound_interval == '2':
        r = (1 + (interest_rate / 52))**(52 / 12) - 1
        payment = principal * ((r * (1 + r)**(length * 12)) /
                               ((1 + r)**(length * 12) - 1))
        return payment
    elif compound_interval == '3':
        r = (1 + (interest_rate / 365))**(365 / 12) - 1
        payment = principal * ((r * (1 + r)**(length * 12)) /
                               ((1 + r)**(length * 12) - 1))
        return payment
    else:
        print("Invalid compounding interval. Returning to main...")
        return


def get_term_length():
    """A function to calculate the time left of a user's mortgage"""
    # principal, interest_rate, compound_interval, payment = get_info("2")
    print("This functionality coming soon! Stay tuned...")
    return


def get_info(option):
    """A bifurcated function to collect necessary information from the user"""
    principal = input("Please enter the principal left on your mortgage: ")
    interest_rate = input("Please enter your interest rate(%): ")
    compound_interval = input("Does your mortgage compound: \n1) Monthly\n2) Weekly\n3) Daily\n: ")
    if option == "1":
        length = input("Please enter the length of your mortgage (years): ")
        return principal, interest_rate, compound_interval, length
    else:
        payment = input("Please enter your monthly payment: ")
        return principal, interest_rate, compound_interval, payment


def show_results(answer, choice_input):
    """A function to print out the desired answer"""
    if choice_input == "1":
        print("Your monthly mortgage payment will be: $" + str(round(answer, 2)))
    else:
        print("You have " + str(answer) + " months left until your mortgage is paid off!")


main()
