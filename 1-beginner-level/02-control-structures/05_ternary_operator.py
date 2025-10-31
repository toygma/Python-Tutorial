# FILE: 05_ternary_operator.py
"""
TERNARY OPERATOR
================

The ternary operator is a shorthand way to write simple if-else statements
in a single line. Also known as conditional expression.

Syntax: value_if_true if condition else value_if_false

Key Concepts:
- Basic ternary operator
- Nested ternary operators
- Ternary with functions
- When to use vs when to avoid
"""

# Basic Ternary Operator
print("BASIC TERNARY OPERATOR:")
print("=" * 50)

# Traditional if-else
age = 20
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(f"Traditional way: {status}")

# Ternary operator (one line)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Ternary way: {status}")

# More examples
print("\nMore examples:")
number = 10
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

temperature = 25
weather = "Hot" if temperature > 30 else "Pleasant"
print(f"Temperature {temperature}°C: {weather}")

is_raining = False
advice = "Take umbrella" if is_raining else "No umbrella needed"
print(advice)

# Ternary with Variables
print("\n" + "=" * 50)
print("TERNARY WITH VARIABLES:")

x = 15
y = 20
max_value = x if x > y else y
print(f"Maximum of {x} and {y}: {max_value}")

min_value = x if x < y else y
print(f"Minimum of {x} and {y}: {min_value}")

# Ternary with Functions
print("\n" + "=" * 50)
print("TERNARY WITH FUNCTIONS:")

def get_discount(is_member):
    return 20 if is_member else 5

print(f"Member discount: {get_discount(True)}%")
print(f"Non-member discount: {get_discount(False)}%")

# Ternary in return statements
def absolute_value(num):
    return num if num >= 0 else -num

print(f"\nAbsolute value of -5: {absolute_value(-5)}")
print(f"Absolute value of 10: {absolute_value(10)}")

# Ternary with Multiple Conditions (Nested)
print("\n" + "=" * 50)
print("NESTED TERNARY OPERATORS:")

# Simple grade system
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score {score}: Grade {grade}")

# Age category
age = 45
category = "Child" if age < 13 else "Teen" if age < 18 else "Adult" if age < 65 else "Senior"
print(f"Age {age}: {category}")

# Traffic light
light = "yellow"
action = "Stop" if light == "red" else "Caution" if light == "yellow" else "Go"
print(f"Light is {light}: {action}")

# Warning: Too many nested ternary operators become hard to read
# This is hard to read (avoid this):
x = 5
result = "tiny" if x < 1 else "small" if x < 5 else "medium" if x < 10 else "large" if x < 20 else "huge"
print(f"\nValue {x} is: {result}")

# Better: Use regular if-elif-else for complex logic
def categorize_size(x):
    if x < 1:
        return "tiny"
    elif x < 5:
        return "small"
    elif x < 10:
        return "medium"
    elif x < 20:
        return "large"
    else:
        return "huge"

print(f"Better approach: {categorize_size(5)}")

# Ternary in List Comprehensions
print("\n" + "=" * 50)
print("TERNARY IN LIST COMPREHENSIONS:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(f"Numbers: {numbers}")
print(f"Labels: {labels}")

# Categorize temperatures
temperatures = [15, 25, 35, 5, 20]
categories = ["Cold" if t < 15 else "Hot" if t > 30 else "Moderate" for t in temperatures]
print(f"\nTemperatures: {temperatures}")
print(f"Categories: {categories}")

# Real-world Example: Price Calculation
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: PRICE CALCULATION")

def calculate_price(base_price, is_member, quantity):
    """Calculate final price with ternary operators"""
    discount = 0.2 if is_member else 0.1 if quantity > 10 else 0
    final_price = base_price * (1 - discount)
    return final_price

print(f"Member buying 1 item: ${calculate_price(100, True, 1):.2f}")
print(f"Non-member buying 15 items: ${calculate_price(100, False, 15):.2f}")
print(f"Non-member buying 5 items: ${calculate_price(100, False, 5):.2f}")

# Real-world Example: Status Messages
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: STATUS MESSAGES")

def get_status_message(progress):
    """Get status message based on progress"""
    return ("Complete!" if progress >= 100 else 
            f"{progress}% - Almost there!" if progress >= 75 else
            f"{progress}% - Good progress" if progress >= 50 else
            f"{progress}% - Keep going")

for progress in [25, 50, 75, 100]:
    print(get_status_message(progress))

# Real-world Example: User Greeting
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: USER GREETING")

def greet_user(name, time_hour):
    """Generate greeting based on time"""
    greeting = ("Good morning" if time_hour < 12 else
                "Good afternoon" if time_hour < 18 else
                "Good evening")
    return f"{greeting}, {name}!"

print(greet_user("Alice", 9))   # Morning
print(greet_user("Bob", 14))    # Afternoon
print(greet_user("Charlie", 20)) # Evening

# Real-world Example: Validation
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: INPUT VALIDATION")

def validate_input(value):
    """Validate input with ternary operator"""
    return "Valid" if value and len(value) >= 3 else "Too short" if value else "Empty"

inputs = ["", "ab", "valid_input"]
for inp in inputs:
    result = validate_input(inp)
    print(f"Input '{inp}': {result}")

# Ternary with Boolean Operations
print("\n" + "=" * 50)
print("TERNARY WITH BOOLEAN OPERATIONS:")

# Set default values
username = ""
display_name = username if username else "Guest"
print(f"Display name: {display_name}")

username = "john_doe"
display_name = username if username else "Guest"
print(f"Display name: {display_name}")

# Safe division
def safe_divide(a, b):
    return a / b if b != 0 else 0

print(f"\n10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# Ternary vs Dictionary Mapping
print("\n" + "=" * 50)
print("ALTERNATIVES TO NESTED TERNARY:")

# Instead of nested ternary for many conditions, use dictionary
day = "Monday"

# Ternary (gets messy with many conditions)
# message = "Work" if day == "Monday" else "Work" if day == "Tuesday" else ...

# Better: Dictionary mapping
day_messages = {
    "Monday": "Start of work week",
    "Tuesday": "Keep going",
    "Wednesday": "Midweek",
    "Thursday": "Almost there",
    "Friday": "TGIF!",
    "Saturday": "Weekend!",
    "Sunday": "Relax"
}

message = day_messages.get(day, "Unknown day")
print(f"{day}: {message}")

# Real-world Example: Eligibility Check
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: ELIGIBILITY CHECK")

def check_eligibility(age, has_license, has_car):
    """Check driving eligibility"""
    return ("Can drive own car" if has_car else "Can drive with rental") if has_license and age >= 18 else "Not eligible"

scenarios = [
    (25, True, True, "Adult with license and car"),
    (25, True, False, "Adult with license, no car"),
    (25, False, True, "Adult, no license"),
    (16, False, False, "Minor"),
]

for age, has_license, has_car, description in scenarios:
    result = check_eligibility(age, has_license, has_car)
    print(f"{description}: {result}")

# Ternary with Tuples (Advanced)
print("\n" + "=" * 50)
print("TERNARY WITH TUPLES (ADVANCED):")

# Using tuple indexing (not recommended, just for knowledge)
condition = True
result = ("False value", "True value")[condition]
print(f"Using tuple indexing: {result}")

# Better to use standard ternary
result = "True value" if condition else "False value"
print(f"Standard ternary: {result}")

# Practical Examples
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES:")

# Example 1: Password strength
password = "mypass"
strength = "Strong" if len(password) >= 8 else "Weak"
print(f"Password strength: {strength}")

# Example 2: Stock status
stock = 5
status = "In Stock" if stock > 0 else "Out of Stock"
print(f"Stock status: {status}")

# Example 3: Voting eligibility
age = 17
can_vote = "Yes" if age >= 18 else "No"
print(f"Can vote (age {age}): {can_vote}")

# Example 4: Temperature warning
temp = 38
warning = "Fever!" if temp > 37.5 else "Normal"
print(f"Temperature {temp}°C: {warning}")

# Example 5: Assignment deadline
days_left = 3
urgency = "Urgent!" if days_left <= 2 else "On track"
print(f"Days left: {days_left} - {urgency}")

# When to Use Ternary vs If-Else
print("\n" + "=" * 50)
print("WHEN TO USE TERNARY OPERATOR:")
print("""
✓ Use ternary when:
  - Simple condition with single line result
  - Assigning values based on condition
  - Making code more concise and readable
  
✗ Avoid ternary when:
  - Multiple conditions (use if-elif-else)
  - Complex logic requiring multiple statements
  - Code becomes hard to read
  - Need to perform actions, not just return values
""")

# Practice Exercises:
print("=" * 50)
print("--- EXERCISES ---")
print("1. Write a ternary to check if a number is positive or negative")
print("2. Create a function using ternary to return 'Pass' or 'Fail' based on score")
print("3. Use ternary to categorize BMI (underweight, normal, overweight)")
print("4. Make a list comprehension with ternary to filter and transform data")
print("5. Write a function that returns shipping cost using nested ternary")