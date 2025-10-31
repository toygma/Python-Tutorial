# ============================================================================
# FILE: 04_user_input.py
"""
USER INPUT
==========

The input() function allows you to get input from users. It always returns a string,
so type conversion is often needed.

Key Concepts:
- Getting user input
- Processing input
- Input validation
- Type conversion of input
"""

# Basic input
print("Basic Input Example:")
print("=" * 40)
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Input with type conversion
print("\n" + "=" * 40)
print("Type Conversion Example:")
# age_str = input("Enter your age: ")
# age = int(age_str)
# print(f"You are {age} years old")
# print(f"Next year you will be {age + 1}")

# Multiple inputs in one line
print("\n" + "=" * 40)
print("Multiple Inputs Example:")
# data = input("Enter your name and age (separated by space): ")
# name, age_str = data.split()
# age = int(age_str)
# print(f"{name} is {age} years old")

# Calculator example
print("\n" + "=" * 40)
print("Simple Calculator:")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")

# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Invalid operation"

# print(f"Result: {result}")

# Input validation example
print("\n" + "=" * 40)
print("Input Validation Example:")

def get_valid_age():
    """Get a valid age from user with error handling"""
    while True:
        try:
            age = int(input("Enter your age (1-120): "))
            if 1 <= age <= 120:
                return age
            else:
                print("Age must be between 1 and 120")
        except ValueError:
            print("Invalid input! Please enter a number")

# Uncomment to test:
# valid_age = get_valid_age()
# print(f"Valid age entered: {valid_age}")

# Yes/No input
print("\n" + "=" * 40)
print("Yes/No Input Example:")

def get_yes_no(question):
    """Get yes/no answer from user"""
    while True:
        answer = input(f"{question} (yes/no): ").lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Please answer yes or no")

# Uncomment to test:
# likes_python = get_yes_no("Do you like Python?")
# if likes_python:
#     print("Great! Python is awesome!")
# else:
#     print("Give it a try, you might like it!")

# Menu selection
print("\n" + "=" * 40)
print("Menu Selection Example:")

def show_menu():
    """Display a menu and get user choice"""
    print("\n--- MENU ---")
    print("1. View Profile")
    print("2. Edit Settings")
    print("3. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Choice must be 1, 2, or 3")
        except ValueError:
            print("Please enter a number")

# Uncomment to test:
# choice = show_menu()
# print(f"You selected option {choice}")

# Practice Exercises:
print("\n" + "=" * 40)
print("--- EXERCISES ---")
print("1. Create a program that asks for name, age, and city")
print("2. Build a BMI calculator that takes height and weight")
print("3. Make a quiz program with 3 questions")
print("4. Create a number guessing game with input validation")
