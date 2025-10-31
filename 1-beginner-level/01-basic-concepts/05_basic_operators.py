# ============================================================================
# FILE: 05_basic_operators.py
"""
BASIC OPERATORS
===============

Operators are special symbols that perform operations on variables and values.

Key Concepts:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
"""

# Arithmetic Operators
print("ARITHMETIC OPERATORS:")
print("=" * 50)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")  # Returns float
print(f"Floor Division (a // b): {a // b}")  # Returns integer
print(f"Modulus (a % b): {a % b}")  # Remainder
print(f"Exponentiation (a ** b): {a ** b}")  # Power

# Assignment Operators
print("\n" + "=" * 50)
print("ASSIGNMENT OPERATORS:")

x = 5  # Simple assignment
print(f"x = {x}")

x += 3  # x = x + 3
print(f"After x += 3: {x}")

x -= 2  # x = x - 2
print(f"After x -= 2: {x}")

x *= 4  # x = x * 4
print(f"After x *= 4: {x}")

x /= 2  # x = x / 2
print(f"After x /= 2: {x}")

x //= 3  # x = x // 3
print(f"After x //= 3: {x}")

x %= 5  # x = x % 5
print(f"After x %= 5: {x}")

x **= 2  # x = x ** 2
print(f"After x **= 2: {x}")

# Comparison Operators
print("\n" + "=" * 50)
print("COMPARISON OPERATORS:")

a, b = 10, 5
print(f"a = {a}, b = {b}")
print(f"Equal (a == b): {a == b}")
print(f"Not equal (a != b): {a != b}")
print(f"Greater than (a > b): {a > b}")
print(f"Less than (a < b): {a < b}")
print(f"Greater or equal (a >= b): {a >= b}")
print(f"Less or equal (a <= b): {a <= b}")

# Logical Operators
print("\n" + "=" * 50)
print("LOGICAL OPERATORS:")

x, y = True, False
print(f"x = {x}, y = {y}")
print(f"AND (x and y): {x and y}")
print(f"OR (x or y): {x or y}")
print(f"NOT (!x): {not x}")

# Practical example
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"\nAge: {age}, Has license: {has_license}")
print(f"Can drive: {can_drive}")

# Identity Operators
print("\n" + "=" * 50)
print("IDENTITY OPERATORS:")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"a is b: {a is b}")  # False (different objects)
print(f"a is c: {a is c}")  # True (same object)
print(f"a == b: {a == b}")  # True (same values)

# Membership Operators
print("\n" + "=" * 50)
print("MEMBERSHIP OPERATORS:")

fruits = ['apple', 'banana', 'orange']
print(f"Fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

text = "Hello World"
print(f"\nText: '{text}'")
print(f"'Hello' in text: {'Hello' in text}")
print(f"'Python' in text: {'Python' in text}")

# Operator Precedence
print("\n" + "=" * 50)
print("OPERATOR PRECEDENCE:")
print("Parentheses > Exponentiation > Multiplication/Division > Addition/Subtraction")

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
result3 = 2 ** 3 + 4
result4 = 2 ** (3 + 4)

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")
print(f"2 ** 3 + 4 = {result3}")
print(f"2 ** (3 + 4) = {result4}")

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Calculate the area and perimeter of a rectangle")
print("2. Check if a number is even or odd using modulus")
print("3. Compare three numbers and find the largest")
print("4. Create a simple discount calculator")