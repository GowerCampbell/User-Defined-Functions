# Traveler's Holiday: Holiday Cost Calculator  
**Author:** Gower Campbell  

This document explains the **Traveler's Holiday** program, a Python application that calculates the total cost of a holiday based on user inputs. The program demonstrates the use of **user-defined functions**, **dictionaries**, and **conditional logic** to create a dynamic and interactive holiday cost calculator.

---

## Table of Contents  
1. [Introduction](#introduction)  
2. [Code Overview](#code-overview)  
   - [Holiday Package Dictionary](#holiday-package-dictionary)  
   - [Displaying Holiday Packages](#displaying-holiday-packages)  
   - [Choosing a Holiday](#choosing-a-holiday)  
   - [Calculating Costs](#calculating-costs)  
   - [Displaying Holiday Details](#displaying-holiday-details)  
3. [How It Works](#how-it-works)  
4. [Key Features](#key-features)  
5. [Future Improvements](#future-improvements)  

---

## 1. Introduction  
The **Traveler's Holiday** program is a Python application that helps users calculate the total cost of their holiday. It allows users to:  
- Choose from a list of holiday destinations.  
- Specify the number of nights they will stay at a hotel.  
- Specify the number of days they will rent a car.  
- View a detailed breakdown of their holiday costs.  

The program uses **user-defined functions** to modularize the code and **dictionaries** to store holiday package details. It also includes **error handling** to ensure a smooth user experience.

---

## 2. Code Overview  

### Holiday Package Dictionary  
The program uses a dictionary called `holiday_packages` to store details about each destination:  
```python
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
```  
- **Purpose**: Stores details about each destination, including a description and flight cost.  
- **Flexibility**: New destinations can be added easily by updating the dictionary.  

---

### Displaying Holiday Packages  
The `display_holiday_packages()` function displays the available holiday packages:  
```python
def display_holiday_packages():
    """Display available holiday packages with descriptions."""
    print("Available Holiday Packages:\n")
    for index, (city, details) in enumerate(holiday_packages.items(), start=1):
        print(f"{index}. {city}:")
        print(f"   {details['description']}")
        print(f"   Flight Cost: £{details['flight_cost']}\n")
```  
- **Purpose**: Provides a clear and organized display of available options.  
- **Reusability**: This function can be called anytime the menu needs to be displayed.  

---

### Choosing a Holiday  
The `choose_holiday()` function prompts the user to select a holiday package:  
```python
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
```  
- **Purpose**: Ensures the user selects a valid holiday package.  
- **Error Handling**: Handles invalid inputs (e.g., non-numeric values or out-of-range numbers).  

---

### Calculating Costs  
The program uses three functions to calculate costs:  

#### `hotel_cost(num_nights)`  
```python
def hotel_cost(num_nights):
    """Calculate the total cost of the hotel stay."""
    price_per_night = 200  # Cost per night at the hotel
    return num_nights * price_per_night
```  
- **Purpose**: Calculates the total cost of the hotel stay.  

#### `car_rental(rental_days)`  
```python
def car_rental(rental_days):
    """Calculate the total cost of renting a car."""
    daily_rental_cost = 40  # Cost per day for car rental
    return rental_days * daily_rental_cost
```  
- **Purpose**: Calculates the total cost of renting a car.  

#### `plane_cost(city)`  
```python
def plane_cost(city):
    """Return the flight cost for the chosen city."""
    return holiday_packages[city]["flight_cost"]
```  
- **Purpose**: Retrieves the flight cost for the chosen city.  

---

### Displaying Holiday Details  
The program displays a detailed breakdown of the holiday costs:  
```python
print("\nHoliday Details:")
print(f"Destination: {chosen_holiday}")
print(f"Nights at hotel: {num_nights} nights at £200 per night")
print(f"Car rental: {rental_days} days at £40 per day")
print(f"Flight cost: £{plane_cost(chosen_holiday)}")
print(f"Total holiday cost: £{total_cost}\n")
```  
- **Purpose**: Provides a clear and user-friendly summary of the holiday costs.  

---

## 3. How It Works  
1. The program starts by displaying available holiday packages.  
2. The user selects a holiday package by entering a number (1, 2, or 3).  
3. The user specifies the number of nights they will stay at the hotel and the number of days they will rent a car.  
4. The program calculates the total cost of the holiday and displays a detailed breakdown.  

---

## 4. Key Features  
1. **Modular Design**: Each function has a single responsibility, making the code easy to read and maintain.  
2. **Error Handling**: Ensures the program doesn’t crash due to invalid user inputs.  
3. **User-Friendly Interface**: Clear prompts and error messages guide the user through the process.  
4. **Dynamic Calculations**: Costs are calculated dynamically based on user inputs.  

---

## 5. Future Improvements  
1. **Currency Formatting**: Use Python’s `locale` module to format currency (e.g., £1,820 instead of £1820).  
2. **Graphical Interface**: Create a GUI using `tkinter` or `PyQt` for a more interactive experience.  
3. **Additional Features**: Add options for travel insurance, meals, or activities.  
4. **Data Persistence**: Save user inputs and holiday details to a file for future reference.  

---

## Example Output  

```
Available Holiday Packages:

1. Madrid:
   Stay at the Villa Real Hotel in Madrid, a vibrant city with 
sightseeing, restaurants, and Christmas charm.
   Flight Cost: £700

2. Rome:
   Stay at the Madison Hotel in Rome, with rich city access, 
festive markets, and unique holiday gifts.
   Flight Cost: £600

3. Prague:
   Stay at the Don Giovanni Hotel in Prague, with access to 
historic markets, festive traditions, and snowy charm.
   Flight Cost: £470


Choose your Holiday Package 
(1 | Madrid, 2 | Rome, 3 | Prague): 1

Enter your duration at our hotel package price:
(£200 per Night): 5

Enter the number of days you will hire a car: 
(Enter 0 to skip): 3

Holiday Details:
Destination: Madrid
Nights at hotel: 5 nights at £200 per night
Car rental: 3 days at £40 per day
Flight cost: £700
Total holiday cost: £1820
```

