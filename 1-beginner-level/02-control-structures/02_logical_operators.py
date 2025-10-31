# ============================================================================
# FILE: 02_logical_operators.py
"""
LOGICAL OPERATORS
=================

Logical operators are used to combine conditional statements.

Key Concepts:
- AND operator
- OR operator
- NOT operator
- Operator precedence
- Short-circuit evaluation
"""

# AND operator
print("AND OPERATOR:")
print("=" * 50)
print("Both conditions must be True")

age = 25
has_license = True

if age >= 18 and has_license:
    print("✓ You can drive")

# Truth table for AND
print("\nAND Truth Table:")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

# OR operator
print("\n" + "=" * 50)
print("OR OPERATOR:")
print("At least one condition must be True")

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("✓ You can relax!")

# Truth table for OR
print("\nOR Truth Table:")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

# NOT operator
print("\n" + "=" * 50)
print("NOT OPERATOR:")
print("Inverts the boolean value")

is_raining = False
if not is_raining:
    print("✓ You don't need an umbrella")

print(f"\nnot True = {not True}")
print(f"not False = {not False}")

# Combining logical operators
print("\n" + "=" * 50)
print("COMBINING LOGICAL OPERATORS:")

age = 25
is_student = True
has_id = True

# Complex condition
if (age >= 18 and age <= 65) or (is_student and has_id):
    print("✓ You get a discount")

# Operator precedence: NOT > AND > OR
print("\nOperator Precedence (NOT > AND > OR):")
result = True or False and False
print(f"True or False and False = {result}")  # True (AND evaluated first)

result = (True or False) and False
print(f"(True or False) and False = {result}")  # False (parentheses first)

# Short-circuit evaluation
print("\n" + "=" * 50)
print("SHORT-CIRCUIT EVALUATION:")
print("Python stops evaluating as soon as the result is determined")

def expensive_check():
    """Simulates an expensive operation"""
    print("  → Expensive check called!")
    return True

# AND short-circuit
print("\nAND with False (second condition not evaluated):")
result = False and expensive_check()
print(f"Result: {result}")

print("\nAND with True (second condition evaluated):")
result = True and expensive_check()
print(f"Result: {result}")

# OR short-circuit
print("\nOR with True (second condition not evaluated):")
result = True or expensive_check()
print(f"Result: {result}")

print("\nOR with False (second condition evaluated):")
result = False or expensive_check()
print(f"Result: {result}")

# Real-world example: Form validation
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: FORM VALIDATION")

def validate_registration(email, password, age, terms_accepted):
    """Validate user registration"""
    errors = []
    
    # Email validation
    if not email or '@' not in email:
        errors.append("Invalid email address")
    
    # Password validation
    if not password or len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    # Age validation
    if not (13 <= age <= 120):
        errors.append("Age must be between 13 and 120")
    
    # Terms validation
    if not terms_accepted:
        errors.append("You must accept terms and conditions")
    
    # Check if valid
    if not errors:
        return True, "Registration successful!"
    else:
        return False, errors

# Test cases
print("\nTest 1: Valid registration")
valid, message = validate_registration("user@email.com", "password123", 25, True)
print(f"Valid: {valid}, Message: {message}")

print("\nTest 2: Invalid registration")
valid, message = validate_registration("invalid-email", "12", 150, False)
print(f"Valid: {valid}")
print("Errors:")
for error in message:
    print(f"  - {error}")

# Real-world example: Access control
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: ACCESS CONTROL")

def check_access(user_role, is_authenticated, resource_level):
    """Check if user can access a resource"""
    # Admin can access everything
    if user_role == "admin" and is_authenticated:
        return True
    
    # Manager can access basic and intermediate
    if user_role == "manager" and is_authenticated:
        return resource_level in ["basic", "intermediate"]
    
    # User can only access basic
    if user_role == "user" and is_authenticated:
        return resource_level == "basic"
    
    # Not authenticated or invalid role
    return False

# Test access control
print(check_access("admin", True, "advanced"))  # True
print(check_access("manager", True, "advanced"))  # False
print(check_access("user", True, "basic"))  # True
print(check_access("user", False, "basic"))  # False

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a password strength checker using multiple conditions")
print("2. Build a movie ticket eligibility checker (age, time, ticket type)")
print("3. Make a weather advisory system (temperature, humidity, wind)")
print("4. Implement a shopping cart discount system with multiple rules")