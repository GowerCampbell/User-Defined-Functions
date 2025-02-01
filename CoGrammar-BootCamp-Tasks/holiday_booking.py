# Traveler's Holiday: Holiday Cost Calculator
# Written by Gower Campbell

# Objective: Demonstrate the use of Python functions, conditional logic, 
# and user interaction in a dynamic holiday cost calculator.

# ---- Key Features ----
# 1. Calculate specific costs using conditional logic within functions.
# 2. Utilize a dictionary to dynamically choose destinations and calculate costs.
# 3. Output holiday details in a clear, user-friendly format.

# HOLIDAY COST CALCULATOR PROGRAM

# < ----------------- Holiday Package Dictionary ----------------->
holiday_packages = {
    "Madrid": {
        "description": """Stay at the Villa Real Hotel in Madrid, a vibrant city with 
sightseeing, restaurants, and Christmas charm.""",
        "flight_cost": 700,  # Flight cost in GBP
    },
    "Rome": {
        "description": """Stay at the Madison Hotel in Rome, with rich city access, 
festive markets, and unique holiday gifts.""",
        "flight_cost": 600,  # Flight cost in GBP
    },
    "Prague": {
        "description": """Stay at the Don Giovanni Hotel in Prague, with access to 
historic markets, festive traditions, and snowy charm.""",
        "flight_cost": 470,  # Flight cost in GBP
    }
}

# < ----------------- Display Holiday Packages ----------------->
def display_holiday_packages():
    """Display available holiday packages with descriptions."""
    print("Available Holiday Packages:\n")
    for index, (city, details) in enumerate(holiday_packages.items(), start=1):
        print(f"{index}. {city}:")
        print(f"   {details['description']}")
        print(f"   Flight Cost: £{details['flight_cost']}\n")

# <-------------- Holiday Selection -------------------->
def choose_holiday():
    """Prompt the user to choose a holiday package."""
    while True:
        try:
            city_flight = int(input('''\nChoose your Holiday Package 
(1 | Madrid, 2 | Rome, 3 | Prague): '''))
            if city_flight in [1, 2, 3]:
                return list(holiday_packages.keys())[city_flight - 1]
            else:
                print("\nInvalid choice. Please select a number between 1 and 3.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

# <-------------- User Inputs | Hotel/Car/Plane Functions -------------------->

# 1. Function to calculate hotel cost
def hotel_cost(num_nights):
    """Calculate the total cost of the hotel stay."""
    price_per_night = 200  # Cost per night at the hotel
    return num_nights * price_per_night

# 2. Function to calculate car rental cost
def car_rental(rental_days):
    """Calculate the total cost of renting a car."""
    daily_rental_cost = 40  # Cost per day for car rental
    return rental_days * daily_rental_cost

# 3. Function to get flight cost
def plane_cost(city):
    """Return the flight cost for the chosen city."""
    return holiday_packages[city]["flight_cost"]

# 4. Function to calculate total holiday cost
def holiday_cost(num_nights, city, rental_days):
    """Calculate the total cost of the holiday."""
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city)
    total_car_rental = car_rental(rental_days)
    return total_hotel_cost + total_plane_cost + total_car_rental

# <-------------- Main Program Logic -------------------->

def main():
    # Display available holiday packages
    display_holiday_packages()

    # Let the user choose a holiday package
    chosen_holiday = choose_holiday()

    # Get the number of nights for the hotel stay
    while True:
        try:
            num_nights = int(input('''\nEnter your duration at our hotel package price:
(£200 per Night): '''))
            if num_nights >= 0:
                break
            else:
                print("\nInvalid input. Please enter a positive number.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

    # Get the number of days for car rental
    while True:
        try:
            rental_days = int(input('''\nEnter the number of days you will hire a car: 
(Enter 0 to skip): '''))
            if rental_days >= 0:
                break
            else:
                print("\nInvalid input. Please enter a positive number.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

    # Calculate total holiday cost
    total_cost = holiday_cost(num_nights, chosen_holiday, rental_days)

    # Display holiday details
    print("\nHoliday Details:")
    print(f"Destination: {chosen_holiday}")
    print(f"Nights at hotel: {num_nights} nights at £200 per night")
    print(f"Car rental: {rental_days} days at £40 per day")
    print(f"Flight cost: £{plane_cost(chosen_holiday)}")
    print(f"Total holiday cost: £{total_cost}\n")

# Run the program
if __name__ == "__main__":
    main()
