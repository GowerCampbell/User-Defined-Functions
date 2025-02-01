
# Programming with User-defined Functions
# Written By Gower Campbell

# To create my own functions to tackle complex tasks.
# Compute certain values using list elements and text file content.

def add_one(x):  # Function called add_one has one parameter, x
    y = x + 1
    return y

# Defined by the keyword 'def' followed by the function name 'add_one'.
# It takes the parameter x as input.
# (A parameter is a variable declared in the function.)
# Imperative (declarative language means coding everything explicitly).
# It defines what needs to happen.

# Computes the new variable, y, which is the value stored in variable x with 1 added.
# It will then return y.

# Encapsulate: A set of instructions.
# Function definition (function name and parentheses).
# Arguments can be passed into functions.
# Return values are used to send back results to the part of the program that called the function.

# The code indented under `def add_one` is the logic of the function.
# It defines what happens when the function is called.

# Modules of Code: Hiding away the "how" and making functions reusable.

# Syntax:
# def functionName(parameters):
#     statements
#     return (expression)

# Define: Use `def`, provide a function name, and specify input parameters.
# Execute: The function takes input and returns a result based on the input values.
# Explanation: Functions are reusable blocks of code that perform specific tasks.

# When used in OOP (Object-Oriented Programming) classes, functions are called methods.
# Functions help organize code, make it more readable, and facilitate debugging and maintenance.
# Useful for abstraction and using built-in functions like `print()` and `len()`.

# The value after the `return` statement is the result of the expression.
# The """docstring""" can be used to describe the function's purpose.
# Note that the `return` keyword doesn't have to be included in a function.
# `return` sends back a value to the caller of the function.

# PRINT Versus RETURN
# [print outputs data to the console] (useful for debugging and displaying information).
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: "Hello, Alice"

# [return sends data back to the caller of the function]
# (useful for reusing the result of a function elsewhere in the program).
def add(a, b):
    return a + b

result = add(3, 4)  # Assign the value 7 to the result.
print(result)  # Print 7 to the console.

# In summary:
# - `print` is for displaying information.
# - `return` is for passing data from a function to the rest of the program.
#   The result can be stored in a variable, used elsewhere, or printed to the console.

# Calling a Function
# Define all my functions so that I can call them later in the file.
# Use the function name followed by the values you want to pass in as arguments.
# The values passed to the function are referred to as arguments.

def add_one(x):  # Function called add_one has one parameter, x
    y = x + 1
    return y

result_num = add_one(5)  # Call the function with the argument 5.
# The function adds one to the argument (5 + 1) and returns 6.
# The result is assigned to the variable result_num.

print(result_num)  # Prints 6

# The code indented under `def add_one` will not execute unless the function is called.
# For example, calling `add_one(5)` executes the function.

# Working with Function Parameters
# Parameters are defined between the parentheses after the function name.
# Use commas to separate multiple parameters.
# Remember: What you pass to the function is an argument.

result_num = add_one(5)  # Call the function with the argument 5.

# Example:
# Here, we pass the value 10 as the argument for the function `add_one`.
# The parameter x is assigned the value 10.

def add_one(x):
    y = x + 1
    return y

num_plus_one = add_one(10)  # Call the function with the argument 10.
# The result is stored in the variable num_plus_one.

print("10 plus 1 is equal to: " + str(num_plus_one) + ".")

# Alternatively:
num = 10
print("10 plus 1 is equal to: " + str(add_one(num)) + ".")
# Note: You can call the function and print the result in a single statement.

# Functions act as placeholders for computations.
# When called, the function runs its code and returns the result.

# Example: Adding one to the argument but not returning anything.
def add_one(x):  # Parameter: x
    y = x + 1
    print(y)  # Prints the result but does not return it.

add_one(3)  # Calls the function with the argument 3.
# Output: 4
# If you try to store the result, it will be `None`.

# Transitioning from Sequential to Procedural Programming
# You can define a function anywhere in your file.
# The statements under the function are executed when the function is called.

# Why Use Functions?
# - Create reusable code.
# - Avoid repetitive code.
# - Simplify error checking and validation.
# - Divide code into manageable chunks for easier understanding and troubleshooting.
# - Enable modular programming (a set of functions).
# - Facilitate rapid application development and easier maintenance.

# SCOPE
# Scope refers to the ability to find and use variables in a program.
# It acts like a one-way glass mirror: code inside a function can see/use variables outside,
# but code outside cannot see/use variables inside the function.

def adding(a, b):
    total = a + b
    return description + str(total)  # Accesses the global variable `description`.

x = 2
y = 3
description = "Total: "
sum_result = adding(x, y)
print(sum_result)  # Output: Total: 5

# The function uses the `description` variable from outside the function.

# Example of Scope Error:
def adding(a, b):
    total = a + b
    description = "Total: "  # Local variable
    return str(total)

x = 2
y = 3
sum_result = adding(x, y)
print(description + sum_result)  # Error: `description` is not defined globally.

# DEFAULT VALUES
# I can create default arguments for functions.

def multiply(num1, num2=5):  # Default value of 5 for num2
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")

times_5 = multiply(6)  # Uses the default value for num2 (5).
# Output: 6 * 5 = 30

# Overriding the Default Value:
times_7 = multiply(6, 7)  # Overrides the default value for num2.
# Output: 6 * 7 = 42

# Using Keyword Arguments:
times_9 = multiply(num2=6, num1=9)  # Order doesn't matter with keyword arguments.
# Output: 9 * 6 = 54

# Example with Multiple Defaults:
def multiply(num1=6, num2=5):  # Both parameters have default values.
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")

multiply()  # Uses both defaults. Output: 6 * 5 = 30
multiply(1)  # Overrides num1. Output: 1 * 5 = 5
multiply(2, 7)  # Overrides both defaults. Output: 2 * 7 = 14
multiply(num2=8, num1=7)  # Uses keyword arguments. Output: 7 * 8 = 56

# Error Example:
# multiply(num2=8, 7)  # SyntaxError: positional argument follows keyword argument.


