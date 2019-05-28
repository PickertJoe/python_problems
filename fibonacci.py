# A simple program to generate a Fibonacci sequence to N number of iterations


def main():
    """The main menu of the program, prompts for user input and passes it to later functions"""
    while True:
        print("\n---Welcome to the Python Fibonacci machine!---")
        print("If you'd like to exit, simply type 'q'.")
        iterations = input("\nPlease enter the number of iterations you'd like to generate: ")
        if iterations.title() == "Q":
            break

        else:
            try:
                int(iterations)
            except ValueError:
                print("\nInvalid input. Please type an integer")
            else:
                iterations = int(iterations)
                if iterations <= 0:
                    print("\nInvalid input. Please type a number greater than zero.")
                elif iterations > 100:
                    print("\nWoah there, that's a pretty large number! No need to crash your computer.")
                    print("How about a number less than 100?")
                else:
                    sequence = gen_fibonacci(iterations)
                    print_fibonacci(sequence)


def gen_fibonacci(number):
    """A specific function to generate an array of the Fibonacci sequence to n number of iterations"""
    fib = [0, 1]
    index = 1
    if number == 1:
        fib.pop(index)
        return fib
    else:
        while len(fib) < number:
            new_fib = fib[index] + fib[index - 1]
            fib.append(new_fib)
            index += 1
        return fib


def print_fibonacci(sequence):
    """Prints the resulting array containing the desired Fibonacci sequnce"""
    print("Generating Fibonacci sequence...")
    print(sequence, sep=", ")


main()
