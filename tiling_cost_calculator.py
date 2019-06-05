# A simple program to calculate the cost of tiling a specified square footage of floorspace


def main():
    """A function to serve as the main menu"""
    print("~~~Welcome to the Python Tiling Cost Estimator~~~")
    print("I can help you estimate the cost to tile your new home to the nearest $.01")
    print("Simply enter the floorspace dimensions and tiling cost for each room.")
    print("And I'll calculate the total cost.")
    start_prompt = input("Shall we begin?(Y/N): ")

    if start_prompt.title() == "N":
        print("So long!")

    else:
        roomcosts = []
        while True:
            roomcosts = room_calculate(roomcosts)
            continue_prompt = input("Would you like to add another room?(Y/N): ")
            if continue_prompt.title() == "N":
                show_results(roomcosts)
                break
            else:
                continue


def room_calculate(array):
    """A function to calculate the flooring cost for each room"""
    width = input("Please enter the width of your floorspace in meters: ")
    height = input("Please enter the height of your floorspace in meters: ")
    price = input("Please enter the price of your tiling: ")
    cost = float(width) * float(height) * float(price)
    array.append(cost)
    return array


def show_results(array):
    """A function to show the final results of the calculation"""
    final = sum(array)
    print("The grand total to tile your home is: $" + str(round(final, 2)))


main()
