# A simple program to return all prime factors of a user-provided whole number


def main():
    """A function to serve as the main menu and call children functions as necessary"""
    while True:
        print("\n~~~Welcome to the Python Prime Factorization Machine!~~~")
        print("When given a value, I can show you all the prime factors of that number.")
        print("To exit at any time, simply type 'Q'.")
        test_input = input("Please enter a positive integer <1,000,000 you'd like to test: ")

        # Exiting from program if necessary
        if test_input.title() == 'Q':
            print("Exiting program...")
            break

        # Screening user input for non-numeric entries
        try:
            int(test_input)
        except ValueError:
            print("Non-numeric input. Returning to main...")
            continue
        else:
            test_number = int(test_input)

        # Setting a limit on the range of possible user inputs
        if test_number < 1 or test_number > 1000000:
            print("Number out of range. Returning to main...")
            continue

        prime_factors = []
        if test_number % 2 == 0 and test_number != 2:
            prime_factors.append(2)
        for number_1 in range(3, test_number):
            if test_number % number_1 == 0:
                for number_2 in range(2, number_1):
                    if number_1 % number_2 == 0:
                        break
                    elif number_1 in prime_factors:
                        break
                    else:
                        prime_factors.append(number_1)
        show_results(test_number, prime_factors)


def show_results(user_input, array):
    """Simple function to show the final results of the program"""
    if len(array) > 1:
        print("The prime factors of " + str(user_input) + " are:")
        print(array)
    else:
        print(str(user_input) + " is either already a prime number number or has no direct prime factors!")


main()
