# A simple program to automatically generate prime numbers <1,000,000


def main():
    """A function to serve as the main menu and call child functions as necessary"""
    print("\n~~~Welcome to the Python Prime Number Generator!~~~")
    print("I can produce prime numbers less than 1,000,000 for as long as you like.")
    start_input = input("Shall I begin?(Y/N): ")
    if start_input.title() == "N":
        print("So long!")
    else:
        prime_array = []
        while True:
            prime_array = generate_prime(prime_array)
            next_input = input("\nWould you like to see the next prime number?(Y/N): ")
            if next_input.title() == "N":
                print("So long!")
                break
            else:
                continue


def generate_prime(prime_array):
    """A function to generate and print the next prime number in sequence"""
    if not prime_array:
        print(str(1))
        prime_array.append(1)
    elif len(prime_array) == 1:
        print(str(2))
        prime_array.append(2)
    else:
        for number_1 in range(3, 1000000):
            for number_2 in range(2, number_1):
                if number_1 % number_2 == 0:
                    break
            else:
                if number_1 in prime_array:
                    continue
                else:
                    print(number_1)
                    prime_array.append(number_1)
                    break
    return prime_array


main()
