# A simple program to calculate the cost of tiling a specified square footage of floorspace


def main():
    """A function to serve as the main menu"""
    while True:
        print("\n~~~Welcome to the Python Tiling Cost Estimator~~~")
        print("For a given floorspace, I can estimate the cost to tile it to the nearest $.01")
        print("To exit at any time, simply type 'Q'.")
        width = input("Please enter the width of your floorspace in meters: ")
        if width.title() == "Q":
            break
        height = input("Please enter the height of your floorspace in meters: ")
        if height.title() == "Q":
            break
        opt_pricing = ("Tile here cost $50/m2. Would you like to enter a different price(Y/N)? ")
        if opt_pricing.title() == "Y":
            new_price = input("Please enter the new price you'd like to use: ")
