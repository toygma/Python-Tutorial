# ============================================================================
# FILE: 02_while_loop.py
"""
WHILE LOOP
==========

The while loop executes as long as a condition is True.

Key Concepts:
- Basic while loop
- Loop control with conditions
- Infinite loops and how to avoid them
- User input validation
"""

# Basic while loop
print("BASIC WHILE LOOP:")
print("=" * 50)

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Countdown example
print("\nCOUNTDOWN EXAMPLE:")
print("=" * 50)

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off! 🚀")

# While loop with user input
print("\n" + "=" * 50)
print("USER INPUT VALIDATION:")

# Simulated example (commented to avoid blocking)
"""
password = ""
while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password, try again!")
print("Access granted!")
"""

# Sum until condition
print("\nSUM UNTIL CONDITION:")
print("=" * 50)

total = 0
number = 1
while total < 100:
    total += number
    print(f"Added {number}, total now: {total}")
    number += 1

# While loop with break
print("\n" + "=" * 50)
print("WHILE WITH BREAK:")

count = 0
while True:  # Infinite loop
    print(f"Count: {count}")
    count += 1
    if count >= 5:
        break  # Exit the loop

# While loop with continue
print("\nWHILE WITH CONTINUE:")
print("=" * 50)

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:  # Skip even numbers
        continue
    print(number)

# Real-world example: ATM simulation
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: ATM SIMULATION")

balance = 1000
running = True

def atm_simulation():
    """Simple ATM simulation"""
    balance = 1000
    attempts = 0
    max_attempts = 3
    
    # Simulated transactions
    transactions = [
        ("check", 0),
        ("withdraw", 300),
        ("check", 0),
        ("withdraw", 1500),  # Exceeds balance
        ("deposit", 500),
        ("check", 0),
        ("exit", 0)
    ]
    
    for action, amount in transactions:
        if attempts >= max_attempts:
            print("Too many failed attempts. Card blocked.")
            break
        
        if action == "check":
            print(f"Current balance: ${balance}")
        elif action == "withdraw":
            if amount <= balance:
                balance -= amount
                print(f"Withdrew ${amount}. New balance: ${balance}")
            else:
                print(f"Insufficient funds. Balance: ${balance}")
                attempts += 1
        elif action == "deposit":
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
        elif action == "exit":
            print("Thank you for using our ATM!")
            break
        print()

atm_simulation()

# Real-world example: Number guessing game
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: NUMBER GUESSING GAME")

def guessing_game():
    """Number guessing game"""
    secret_number = 42
    max_attempts = 5
    attempt = 0
    
    print("I'm thinking of a number between 1 and 100")
    
    # Simulated guesses
    guesses = [50, 30, 40, 42]
    
    for guess in guesses:
        attempt += 1
        print(f"\nAttempt {attempt}: Guess {guess}")
        
        if guess == secret_number:
            print(f"🎉 Correct! You won in {attempt} attempts!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        if attempt >= max_attempts:
            print(f"Game over! The number was {secret_number}")
            break

guessing_game()

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a program that keeps asking for positive numbers until 0")
print("2. Make a simple login system with 3 attempts")
print("3. Build a menu-driven calculator that runs until user quits")
print("4. Implement a dice rolling game that continues until player wins")