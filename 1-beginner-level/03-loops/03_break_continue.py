# FILE: 03_break_continue.py
"""
BREAK AND CONTINUE STATEMENTS
==============================

break: Exits the loop completely
continue: Skips the current iteration and moves to the next one

Key Concepts:
- Using break to exit loops
- Using continue to skip iterations
- break and continue in nested loops
- Practical use cases
"""

# BREAK Statement
print("BREAK STATEMENT:")
print("=" * 50)
print("Break exits the loop completely\n")

# Basic break example
print("Example 1: Stop at 5")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("\nLoop stopped at 5")

# Break with while loop
print("\nExample 2: Search for a number")
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
search = 9

for num in numbers:
    if num == search:
        print(f"Found {search}!")
        break
    print(f"Checking {num}...")
else:
    print(f"{search} not found")

# Break on condition
print("\nExample 3: Stop when sum exceeds 100")
total = 0
for i in range(1, 50):
    total += i
    if total > 100:
        print(f"Sum exceeded 100 at i={i}, total={total}")
        break

# CONTINUE Statement
print("\n" + "=" * 50)
print("CONTINUE STATEMENT:")
print("=" * 50)
print("Continue skips current iteration\n")

# Basic continue example
print("Example 1: Skip even numbers")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n(Only odd numbers printed)")

# Continue with while loop
print("\nExample 2: Skip negative numbers")
numbers = [5, -3, 8, -1, 10, -7, 15]
for num in numbers:
    if num < 0:
        continue
    print(num, end=" ")
print("\n(Negative numbers skipped)")

# Continue with multiple conditions
print("\nExample 3: Skip multiples of 3 and 5")
for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i, end=" ")
print()

# BREAK vs CONTINUE Comparison
print("\n" + "=" * 50)
print("BREAK vs CONTINUE COMPARISON:")
print("=" * 50)

print("\nWith BREAK (stops completely):")
for i in range(10):
    if i == 5:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}", end=" ")
print()

print("\nWith CONTINUE (skips only 5):")
for i in range(10):
    if i == 5:
        print(f"  Skipping {i}")
        continue
    print(f"  {i}", end=" ")
print()

# BREAK in Nested Loops
print("\n" + "=" * 50)
print("BREAK IN NESTED LOOPS:")
print("=" * 50)
print("Break only exits the innermost loop\n")

print("Example: 2D array search")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

search_value = 5
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"Checking position ({i},{j}): {matrix[i][j]}")
        if matrix[i][j] == search_value:
            print(f"Found {search_value} at position ({i},{j})")
            found = True
            break
    if found:
        break  # Break outer loop too

# Using flags for nested loops
print("\nExample: Breaking both loops with flag")
for i in range(3):
    should_break = False
    for j in range(3):
        print(f"({i},{j})", end=" ")
        if i == 1 and j == 1:
            should_break = True
            break
    if should_break:
        print("\n  Breaking both loops")
        break
    print()

# CONTINUE in Nested Loops
print("\n" + "=" * 50)
print("CONTINUE IN NESTED LOOPS:")
print("=" * 50)

print("Multiplication table (skip when i or j is 5)")
for i in range(1, 6):
    if i == 3:
        continue  # Skip row 3
    for j in range(1, 6):
        if j == 3:
            continue  # Skip column 3
        print(f"{i}x{j}={i*j:2}", end="  ")
    print()

# Real-world Example: Input Validation
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: INPUT VALIDATION")
print("=" * 50)

def get_valid_age():
    """Get valid age with break"""
    max_attempts = 3
    attempt = 0
    
    # Simulated inputs
    test_inputs = ["abc", "-5", "25"]
    
    while attempt < max_attempts:
        user_input = test_inputs[attempt]
        print(f"Attempt {attempt + 1}: Input = '{user_input}'")
        
        try:
            age = int(user_input)
            if age < 0 or age > 120:
                print("  Invalid: Age must be between 0 and 120")
            else:
                print(f"  Valid age: {age}")
                return age
                break  # Exit on valid input
        except ValueError:
            print("  Invalid: Please enter a number")
        
        attempt += 1
    
    print("  Maximum attempts reached")
    return None

result = get_valid_age()

# Real-world Example: Processing Data with Skip
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: DATA PROCESSING")
print("=" * 50)

transactions = [
    {"id": 1, "amount": 100, "status": "approved"},
    {"id": 2, "amount": 50, "status": "pending"},
    {"id": 3, "amount": 200, "status": "approved"},
    {"id": 4, "amount": 0, "status": "approved"},
    {"id": 5, "amount": 150, "status": "rejected"},
    {"id": 6, "amount": 75, "status": "approved"},
]

print("Processing approved transactions (skip pending/rejected):")
total = 0

for transaction in transactions:
    # Skip pending transactions
    if transaction["status"] == "pending":
        print(f"  Transaction {transaction['id']}: Skipped (pending)")
        continue
    
    # Skip rejected transactions
    if transaction["status"] == "rejected":
        print(f"  Transaction {transaction['id']}: Skipped (rejected)")
        continue
    
    # Skip zero amount
    if transaction["amount"] == 0:
        print(f"  Transaction {transaction['id']}: Skipped (zero amount)")
        continue
    
    # Process approved transaction
    total += transaction["amount"]
    print(f"  Transaction {transaction['id']}: Processed ${transaction['amount']}")

print(f"\nTotal processed: ${total}")

# Real-world Example: Menu System
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: MENU SYSTEM")
print("=" * 50)

def menu_system():
    """Simple menu with break to exit"""
    # Simulated user choices
    choices = ["1", "2", "3", "4"]
    choice_index = 0
    
    while choice_index < len(choices):
        choice = choices[choice_index]
        print(f"\n--- MENU ---")
        print("1. View profile")
        print("2. Edit settings")
        print("3. Help")
        print("4. Exit")
        print(f"\nUser selected: {choice}")
        
        if choice == "1":
            print("  → Viewing profile...")
        elif choice == "2":
            print("  → Editing settings...")
        elif choice == "3":
            print("  → Showing help...")
        elif choice == "4":
            print("  → Exiting program...")
            break
        else:
            print("  → Invalid choice")
        
        choice_index += 1
    
    print("Program ended")

menu_system()

# Real-world Example: Finding Prime Numbers
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: PRIME NUMBER FINDER")
print("=" * 50)

def is_prime(n):
    """Check if number is prime using break"""
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Not prime, exit early
    
    return True

print("Prime numbers from 1 to 30:")
primes = []
for num in range(1, 31):
    if is_prime(num):
        primes.append(num)

print(primes)

# Real-world Example: Filtering List
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: FILTERING WITH CONTINUE")
print("=" * 50)

students = [
    {"name": "Alice", "grade": 85, "attendance": 95},
    {"name": "Bob", "grade": 65, "attendance": 70},
    {"name": "Charlie", "grade": 90, "attendance": 50},
    {"name": "David", "grade": 75, "attendance": 85},
    {"name": "Eve", "grade": 55, "attendance": 60},
]

print("Students eligible for honors (grade >= 80 AND attendance >= 80):")
honors_list = []

for student in students:
    # Skip if grade too low
    if student["grade"] < 80:
        print(f"  {student['name']}: Skipped (grade too low)")
        continue
    
    # Skip if attendance too low
    if student["attendance"] < 80:
        print(f"  {student['name']}: Skipped (attendance too low)")
        continue
    
    # Student qualifies
    honors_list.append(student["name"])
    print(f"  {student['name']}: ✓ Qualified")

print(f"\nHonors list: {honors_list}")

# Real-world Example: Password Attempts
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: PASSWORD VERIFICATION")
print("=" * 50)

def verify_password():
    """Password verification with limited attempts"""
    correct_password = "secret123"
    max_attempts = 3
    
    # Simulated password attempts
    attempts_list = ["wrong1", "wrong2", "secret123"]
    
    for attempt in range(max_attempts):
        password = attempts_list[attempt]
        print(f"\nAttempt {attempt + 1}/{max_attempts}")
        print(f"  Entered: {password}")
        
        if password == correct_password:
            print("  ✓ Access granted!")
            return True
            break
        else:
            print("  ✗ Incorrect password")
            remaining = max_attempts - attempt - 1
            if remaining > 0:
                print(f"  {remaining} attempt(s) remaining")
    
    print("\n✗ Account locked - too many failed attempts")
    return False

verify_password()

# Real-world Example: Search with Early Exit
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SEARCH WITH EARLY EXIT")
print("=" * 50)

def search_product(products, search_term):
    """Search for product and exit early when found"""
    print(f"Searching for: '{search_term}'")
    
    for i, product in enumerate(products, 1):
        print(f"  Checking product {i}: {product}")
        
        if search_term.lower() in product.lower():
            print(f"  ✓ Found match!")
            return product
            break
    
    return None

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
result = search_product(products, "key")
print(f"Result: {result}")

# Using pass statement
print("\n" + "=" * 50)
print("PASS STATEMENT (Bonus):")
print("=" * 50)
print("pass does nothing - placeholder for future code\n")

for i in range(5):
    if i == 3:
        pass  # TODO: Add logic here later
    print(i, end=" ")
print("\n")

# Practice Exercises:
print("=" * 50)
print("--- EXERCISES ---")
print("1. Write a program to find the first number divisible by 7 in a list")
print("2. Create a loop that processes only positive numbers (skip negatives)")
print("3. Build a game loop that breaks when player health reaches 0")
print("4. Make a program that validates multiple inputs and breaks on 'quit'")
print("5. Write a nested loop that finds pairs of numbers summing to 10")