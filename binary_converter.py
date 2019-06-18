# A program to convert any user-provided decimal value into binary form and vice versa


class Stack:
    """A class to simulate the stack data structure"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def main():
    """A function to serve as the main menu"""
    while True:
        print("\n~~~Welcome to the Python Binary Digit Converter~~~")
        print("Please select an option from the menu below: ")
        choice = input("1) Decimal -> Binary \n2) Binary -> Decimal \n3) Exit program\n:")

        if choice == '1':
            dec_to_bin()
            continue

        elif choice == '2':
            bin_to_dec()
            continue

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid input. Returning to main...")
            continue


def dec_to_bin():
    """A function to convert a decimal value into its binary representation"""
    value = grab_input('a')
    original = value
    bin_stack = Stack()

    while value > 0:
        remainder = value % 2
        bin_stack.push(remainder)
        value = value // 2

    result = ''
    while bin_stack.size() > 0:
        result = result + str(bin_stack.pop())

    show_results(original, result, 'a')


def bin_to_dec():
    """A function to convert a binary value into its decimal representation"""
    original = grab_input('b')
    value = [int(x) for x in str(original)]
    print(value)
    positional = [2**i for i in range(0, len(value))]
    print(positional)
    product = []
    for i in range(0, len(value)):
        product.append(positional[-(1 + i)] * value[i])

    final = sum(product)
    show_results(original, final, 'b')


def grab_input(conversion):
    """A function to grab the value input from the user"""

    if conversion == 'a':
        while True:
            value = input("Please enter the decimal number you'd like to convert: ")
            try:
                int(value)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            else:
                value = int(value)
                break
        return value

    else:
        while True:
            value = input("Please enter the binary number you'd like to convert: ")
            try:
                int(value)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            else:
                value = int(value)
                break
        return value


def show_results(original, value, conversion):
    """A function to share the results of the conversion with the user"""
    if conversion == 'a':
        print("The binary representation of " + str(original) + " is : " + value)
    else:
        print("The decimal representation of " + str(original) + " is: " + str(value))


main()
