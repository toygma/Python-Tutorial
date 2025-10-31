# FILE: 03_comparison_operators.py
"""
COMPARISON OPERATORS
====================

Comparison operators are used to compare two values and return a boolean result.

Key Concepts:
- Equality and inequality
- Greater than / Less than
- Greater than or equal / Less than or equal
- Chaining comparisons
- Comparing different data types
"""

# Basic Comparison Operators
print("BASIC COMPARISON OPERATORS:")
print("=" * 50)

a = 10
b = 5

print(f"a = {a}, b = {b}\n")

# Equal to (==)
print(f"a == b: {a == b}")  # False
print(f"5 == 5: {5 == 5}")  # True

# Not equal to (!=)
print(f"\na != b: {a != b}")  # True
print(f"5 != 5: {5 != 5}")  # False

# Greater than (>)
print(f"\na > b: {a > b}")  # True
print(f"5 > 10: {5 > 10}")  # False

# Less than (<)
print(f"\na < b: {a < b}")  # False
print(f"5 < 10: {5 < 10}")  # True

# Greater than or equal to (>=)
print(f"\na >= b: {a >= b}")  # True
print(f"5 >= 5: {5 >= 5}")  # True
print(f"3 >= 5: {3 >= 5}")  # False

# Less than or equal to (<=)
print(f"\na <= b: {a <= b}")  # False
print(f"5 <= 5: {5 <= 5}")  # True
print(f"5 <= 3: {5 <= 3}")  # False

# Comparing Strings
print("\n" + "=" * 50)
print("COMPARING STRINGS:")

str1 = "apple"
str2 = "banana"
str3 = "apple"

print(f"str1 = '{str1}', str2 = '{str2}', str3 = '{str3}'\n")

print(f"str1 == str2: {str1 == str2}")  # False
print(f"str1 == str3: {str1 == str3}")  # True
print(f"str1 < str2: {str1 < str2}")  # True (alphabetically)
print(f"str2 > str1: {str2 > str1}")  # True

# String comparison is case-sensitive
print(f"\n'Apple' == 'apple': {'Apple' == 'apple'}")  # False
print(f"'Apple'.lower() == 'apple': {'Apple'.lower() == 'apple'}")  # True

# Comparing different types
print("\n" + "=" * 50)
print("COMPARING DIFFERENT TYPES:")

# Number comparisons
print(f"10 == 10.0: {10 == 10.0}")  # True (value comparison)
print(f"10 is 10.0: {10 is 10.0}")  # False (identity comparison)

# Boolean comparisons
print(f"\nTrue == 1: {True == 1}")  # True
print(f"False == 0: {False == 0}")  # True
print(f"True > False: {True > False}")  # True

# Comparing with None
value = None
print(f"\nvalue is None: {value is None}")  # True
print(f"value == None: {value == None}")  # True (but 'is' is preferred)

# Chaining Comparisons
print("\n" + "=" * 50)
print("CHAINING COMPARISONS:")

x = 15
print(f"x = {x}\n")

# Multiple comparisons in one line
print(f"10 < x < 20: {10 < x < 20}")  # True
print(f"10 < x < 15: {10 < x < 15}")  # False
print(f"10 <= x <= 20: {10 <= x <= 20}")  # True

# Equivalent to using 'and'
print(f"\n10 < x and x < 20: {10 < x and x < 20}")  # Same as above

# Multiple chain
age = 25
print(f"\nage = {age}")
print(f"18 <= age <= 65: {18 <= age <= 65}")  # True

# Comparing Lists, Tuples, Sets
print("\n" + "=" * 50)
print("COMPARING COLLECTIONS:")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}\n")

print(f"list1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 == list3: {list1 == list3}")  # False
print(f"list1 < list3: {list1 < list3}")  # True (lexicographic comparison)

# Tuple comparison
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(f"\ntuple1 < tuple2: {tuple1 < tuple2}")  # True

# Set comparison
set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {1, 2}
print(f"\nset1 == set2: {set1 == set2}")  # True
print(f"set3 < set1: {set3 < set1}")  # True (subset)

# Real-world Example: Grade Checker
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: GRADE CHECKER")

def check_grade(score):
    """Determine grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 87, 73, 61, 45]
for score in scores:
    grade = check_grade(score)
    print(f"Score {score}: Grade {grade}")

# Real-world Example: Age Validator
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: AGE VALIDATOR")

def validate_age(age):
    """Validate age for different categories"""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

ages = [-5, 8, 16, 30, 70]
for age in ages:
    category = validate_age(age)
    print(f"Age {age}: {category}")

# Real-world Example: Password Strength
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: PASSWORD STRENGTH")

def check_password_strength(password):
    """Check password strength based on length"""
    length = len(password)
    
    if length < 6:
        return "Weak"
    elif length < 10:
        return "Medium"
    else:
        return "Strong"

passwords = ["abc", "pass123", "myStrongPass2024"]
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"Password '{pwd}' (length {len(pwd)}): {strength}")

# Real-world Example: Price Comparison
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: PRICE COMPARISON")

def compare_prices(price1, price2, product1="Product A", product2="Product B"):
    """Compare two prices"""
    if price1 < price2:
        savings = price2 - price1
        return f"{product1} is cheaper by ${savings:.2f}"
    elif price1 > price2:
        savings = price1 - price2
        return f"{product2} is cheaper by ${savings:.2f}"
    else:
        return "Both products have the same price"

print(compare_prices(19.99, 24.99))
print(compare_prices(50.00, 45.00))
print(compare_prices(10.00, 10.00))

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Write a function to check if a number is between 1 and 100")
print("2. Create a function to compare three numbers and find the largest")
print("3. Build a temperature converter that checks if temp is valid range")
print("4. Make a function that checks if a year is a leap year")