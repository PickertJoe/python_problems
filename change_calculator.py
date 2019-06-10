# A simple program to calculate the correct change for a given payment and total cost


def main():
    """A funtion to serve as the main menu"""
    while True:
        print("\n~~~Welcome to the Python Change Calculator!~~~")
        print("For a given price and payment, I can return the correct amount of change owed.")

        start_input = input("Would you like to begin?(Y/N): ")
        if start_input.title() == 'N':
            print("So long!")
            break

        else:
            price = input("Please enter the total price of your purchase: ")
            while True:
                payment = input("Please enter the amount you paid: ")

                # Ensuring that the user paid an appropriate amount for their goods
                if price <= payment:
                    break
                elif price == payment:
                    print("No need for change, you're already evened up!")
                    continue
                else:
                    print("That's not enough money to pay for your goods! Please pay an appropriate amount.")

            change_list = get_change(price, payment)
            show_change(change_list, price, payment)


def get_change(price, payment):
    """A function to calculate the appropriate amount of change for the specified price and payment"""
    # Creating a list of the values of all possible change units
    denomination_value = [100, 20, 10, 5, 1, .25, .1, .05, .01]
    # Creating a list to store the number of units per denomination
    change_list = []
    difference = round(float(payment), 2) - round(float(price), 2)

    # Running through each change denomination and calculating their respective values

    for number in denomination_value:
        denom_number = difference // number
        difference = difference - (denom_number * number)
        change_list.append(denom_number)

    return change_list


def show_change(change_list, price, payment):
    """A function to print out the change returned"""
    denom_keys = ['Hundreds', 'Twenties', 'Tens', 'Fives', 'Ones', 'Quarters', 'Dimes', 'Nickels', 'Pennies']
    denom_dict = dict(zip(denom_keys, change_list))

    print("The price was $" + price)
    print("You paid $" + payment)
    print("Your change is: ")
    for key, value in denom_dict.items():
        if value > 0:
            print(str(int(value)) + " " + key)


main()
