# FILE: 01_if_else_elif.py
"""
IF, ELSE, ELIF STATEMENTS
=========================

Control structures allow you to execute different code based on conditions.

Key Concepts:
- if statement
- else statement
- elif (else if) statement
- Nested conditions
"""

# Basic if statement
print("BASIC IF STATEMENT:")
print("=" * 50)

age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
print("\nIF-ELSE STATEMENT:")
print("=" * 50)

temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else statement
print("\nIF-ELIF-ELSE STATEMENT:")
print("=" * 50)

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Multiple conditions
print("\nMULTIPLE CONDITIONS:")
print("=" * 50)

age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the concert")
elif age >= 18 and not has_ticket:
    print("You need to buy a ticket")
else:
    print("You are too young to enter")

# Nested if statements
print("\nNESTED IF STATEMENTS:")
print("=" * 50)

username = "admin"
password = "12345"

if username == "admin":
    if password == "12345":
        print("Login successful!")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# Real-world example: Login system
print("\nREAL-WORLD EXAMPLE: LOGIN SYSTEM")
print("=" * 50)

def login_system(username, password, is_verified):
    """Simple login system with multiple checks"""
    if not username:
        return "Username cannot be empty"
    
    if not password:
        return "Password cannot be empty"
    
    if username == "admin" and password == "admin123":
        if is_verified:
            return "Login successful!"
        else:
            return "Please verify your email first"
    else:
        return "Invalid credentials"

# Test cases
print(login_system("admin", "admin123", True))
print(login_system("admin", "admin123", False))
print(login_system("user", "pass", True))
print(login_system("", "pass", True))

# Real-world example: Discount calculator
print("\nREAL-WORLD EXAMPLE: DISCOUNT CALCULATOR")
print("=" * 50)

def calculate_discount(amount, customer_type, has_coupon):
    """Calculate discount based on multiple conditions"""
    discount = 0
    
    if customer_type == "VIP":
        discount = 25
    elif customer_type == "Member":
        discount = 15
    elif customer_type == "Regular":
        discount = 5
    
    if has_coupon:
        discount += 10
    
    final_discount = min(discount, 50)  # Max 50% discount
    discounted_price = amount * (1 - final_discount / 100)
    
    return discounted_price, final_discount

price = 100
final_price, discount = calculate_discount(100, "VIP", True)
print(f"Original price: ${price}")
print(f"Discount: {discount}%")
print(f"Final price: ${final_price}")

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a program to check if a number is positive, negative, or zero")
print("2. Make a BMI calculator that categorizes health status")
print("3. Build a simple ATM withdrawal system with balance checks")
print("4. Create a ticket pricing system based on age and day of week")
