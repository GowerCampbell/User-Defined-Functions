# area_calculator.py
# A menu-driven program to calculate the area of geometric shapes.

import math

# Function to calculate the area of a square
def square_area(length):
    """
    Calculate the area of a square.

    Parameters:
    length (float): The length of one side of the square.

    Returns:
    float: The area of the square.
    """
    return length ** 2

# Function to calculate the area of a rectangle
def rectangle_area(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return width * height

# Function to calculate the area of a circle
def circle_area(radius):
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * (radius ** 2)

# Function to display the menu options
def display_menu():
    """
    Display the available options for calculating the area of different shapes.
    """
    print("\n--- Area Calculator ---")
    print("1. Calculate the area of a square.")
    print("2. Calculate the area of a rectangle.")
    print("3. Calculate the area of a circle.")
    print("4. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Calculate area of a square
            length = float(input("Enter the length of the square: "))
            area = square_area(length)
            print(f"The area of the square is: {area:.2f}")

        elif choice == "2":
            # Calculate area of a rectangle
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            area = rectangle_area(width, height)
            print(f"The area of the rectangle is: {area:.2f}")

        elif choice == "3":
            # Calculate area of a circle
            radius = float(input("Enter the radius of the circle: "))
            area = circle_area(radius)
            print(f"The area of the circle is: {area:.2f}")

        elif choice == "4":
            # Exit the program
            print("Thank you for using the Area Calculator. Goodbye!")
            break

        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
