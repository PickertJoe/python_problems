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

        factor_array = []
        prime_array = []

        # Calling get_factors function to fill the factors array
        factor_array = get_factors(test_number, factor_array)

        # Calling get_prime function to find all the prime factors
        prime_array = get_prime(test_number, factor_array, prime_array)

#        for number_1 in range(3, test_number):
 #           if test_number % number_1 == 0:
  #              for number_2 in range(2, number_1):
   #                 if number_1 % number_2 == 0:
    #                    break
     #               elif number_1 in prime_factors:
      #                  break
       #             else:
        #                prime_factors.append(number_1)
        show_results(test_number, factor_array, prime_array)


def get_factors(user_input, array):
    """A function to find all possible factors for the given number"""
    for number in range(2, user_input):
        if user_input % number == 0:
            array.append(number)
    return array


def get_prime(user_input, factor_array, prime_array):
    """A function to sort through factor array to find all primes"""
    for factor in factor_array:
        testing = True
        while testing:
            for number in range(2, factor):
                if factor % number == 0:
                    testing = False
                    break
        prime_array.append(factor)
    return prime_array


def show_results(user_input, factor_array, prime_array):
    """Simple function to show the final results of the program"""
    if factor_array:
        print("The factors of " + str(user_input) + " are: " + str(factor_array))
        if not prime_array:
            print("The number " + str(user_input) + " has not prime factors!")
        else:
            print("The prime factors of " + str(user_input) + " are:")
            print(prime_array)
    else:
        print("The number " + str(user_input) + " is already prime!")


main()
