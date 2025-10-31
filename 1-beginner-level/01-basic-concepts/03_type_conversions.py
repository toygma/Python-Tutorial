# ============================================================================
# FILE: 03_type_conversions.py
"""
TYPE CONVERSIONS
================

Type conversion is converting one data type to another. Python provides built-in
functions for type conversion.

Key Concepts:
- Implicit conversion (automatic)
- Explicit conversion (manual)
- Common conversion functions
"""

# Implicit type conversion (automatic)
print("Implicit Conversion:")
num_int = 10
num_float = 5.5
result = num_int + num_float  # int + float = float
print(f"{num_int} + {num_float} = {result}")
print(f"Result type: {type(result)}")

# Explicit type conversion
print("\n--- String to Number ---")
str_number = "100"
int_number = int(str_number)
float_number = float(str_number)

print(f"Original: '{str_number}' (type: {type(str_number)})")
print(f"To int: {int_number} (type: {type(int_number)})")
print(f"To float: {float_number} (type: {type(float_number)})")

print("\n--- Number to String ---")
age = 25
age_str = str(age)
print(f"Original: {age} (type: {type(age)})")
print(f"To string: '{age_str}' (type: {type(age_str)})")

print("\n--- Float to Integer ---")
price = 19.99
price_int = int(price)  # Truncates decimal part
print(f"Original: {price} (type: {type(price)})")
print(f"To int: {price_int} (type: {type(price_int)})")

print("\n--- Boolean Conversions ---")
# To boolean
print(f"bool(0): {bool(0)}")  # False
print(f"bool(1): {bool(1)}")  # True
print(f"bool(''): {bool('')}")  # False (empty string)
print(f"bool('text'): {bool('text')}")  # True
print(f"bool([]): {bool([])}")  # False (empty list)
print(f"bool([1,2,3]): {bool([1,2,3])}")  # True

# From boolean
true_val = True
print(f"int(True): {int(true_val)}")  # 1
print(f"str(True): '{str(true_val)}'")  # 'True'

print("\n--- List, Tuple, Set Conversions ---")
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
my_set = set(my_list)

print(f"List: {my_list} (type: {type(my_list)})")
print(f"To tuple: {my_tuple} (type: {type(my_tuple)})")
print(f"To set: {my_set} (type: {type(my_set)})")

# String to list
text = "Hello"
char_list = list(text)
print(f"\nString to list: {char_list}")

# Common conversion errors
print("\n--- Handling Conversion Errors ---")
try:
    invalid = int("abc")  # This will raise ValueError
except ValueError as e:
    print(f"Error: Cannot convert 'abc' to integer - {e}")

# Safe conversion with validation
user_input = "25"
if user_input.isdigit():
    number = int(user_input)
    print(f"Successfully converted: {number}")
else:
    print("Invalid input: not a number")

# Practice Exercises:
print("\n--- EXERCISES ---")
print("1. Convert the string '3.14' to a float and multiply it by 2")
print("2. Convert the number 100 to a string and concatenate with ' dollars'")
print("3. Create a list [1,2,3] and convert it to a tuple and a set")
print("4. Take a user input as string and convert it to integer safely")