# FILE: 05_range_function.py
"""
RANGE FUNCTION
==============

The range() function generates a sequence of numbers. It's commonly used
with for loops to iterate a specific number of times.

Syntax:
- range(stop)           → 0 to stop-1
- range(start, stop)    → start to stop-1
- range(start, stop, step) → start to stop-1 with step

Key Concepts:
- Basic range usage
- Start, stop, step parameters
- Negative steps (counting backwards)
- Range with different data types
- Converting range to list
"""

# Basic Range - range(stop)
print("BASIC RANGE - range(stop):")
print("=" * 50)

print("range(5) generates: 0, 1, 2, 3, 4")
for i in range(5):
    print(i, end=" ")
print("\n")

print("range(10) - first 10 numbers (0-9):")
for i in range(10):
    print(i, end=" ")
print("\n")

# Range with Start and Stop - range(start, stop)
print("\n" + "=" * 50)
print("RANGE WITH START - range(start, stop):")
print("=" * 50)

print("range(1, 6) generates: 1, 2, 3, 4, 5")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

print("range(5, 11) generates: 5, 6, 7, 8, 9, 10")
for i in range(5, 11):
    print(i, end=" ")
print("\n")

print("range(10, 20) generates numbers from 10 to 19:")
for i in range(10, 20):
    print(i, end=" ")
print("\n")

# Range with Step - range(start, stop, step)
print("\n" + "=" * 50)
print("RANGE WITH STEP - range(start, stop, step):")
print("=" * 50)

print("range(0, 10, 2) - even numbers from 0 to 8:")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

print("range(1, 10, 2) - odd numbers from 1 to 9:")
for i in range(1, 10, 2):
    print(i, end=" ")
print("\n")

print("range(0, 20, 3) - multiples of 3:")
for i in range(0, 20, 3):
    print(i, end=" ")
print("\n")

print("range(0, 50, 5) - multiples of 5:")
for i in range(0, 50, 5):
    print(i, end=" ")
print("\n")

# Negative Step (Counting Backwards)
print("\n" + "=" * 50)
print("NEGATIVE STEP - COUNTING BACKWARDS:")
print("=" * 50)

print("range(10, 0, -1) - countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

print("range(20, 10, -1) - from 20 to 11:")
for i in range(20, 10, -1):
    print(i, end=" ")
print("\n")

print("range(10, 0, -2) - even numbers counting down:")
for i in range(10, 0, -2):
    print(i, end=" ")
print("\n")

print("Countdown sequence (5 to 1):")
for i in range(5, 0, -1):
    print(f"{i}...", end=" ")
print("Blast off! 🚀\n")

# Range with Negative Numbers
print("\n" + "=" * 50)
print("RANGE WITH NEGATIVE NUMBERS:")
print("=" * 50)

print("range(-5, 5) - from -5 to 4:")
for i in range(-5, 5):
    print(i, end=" ")
print("\n")

print("range(-10, 0) - negative numbers:")
for i in range(-10, 0):
    print(i, end=" ")
print("\n")

print("range(-20, -10) - negative range:")
for i in range(-20, -10):
    print(i, end=" ")
print("\n")

# Converting Range to List
print("\n" + "=" * 50)
print("CONVERTING RANGE TO LIST:")
print("=" * 50)

print("list(range(5)):", list(range(5)))
print("list(range(1, 11)):", list(range(1, 11)))
print("list(range(0, 20, 3)):", list(range(0, 20, 3)))
print("list(range(10, 0, -1)):", list(range(10, 0, -1)))

# Range Properties
print("\n" + "=" * 50)
print("RANGE PROPERTIES:")
print("=" * 50)

r = range(1, 11)
print(f"Range object: {r}")
print(f"Start: {r.start}")
print(f"Stop: {r.stop}")
print(f"Step: {r.step}")
print(f"Length: {len(r)}")

# Check membership
print(f"\n5 in range(1, 11): {5 in r}")
print(f"15 in range(1, 11): {15 in r}")

# Indexing range
print(f"\nFirst element r[0]: {r[0]}")
print(f"Last element r[-1]: {r[-1]}")
print(f"Third element r[2]: {r[2]}")

# Using Range in Common Scenarios
print("\n" + "=" * 50)
print("COMMON USE CASES:")
print("=" * 50)

# Example 1: Loop N times
print("Example 1: Execute code 5 times")
for i in range(5):
    print(f"  Iteration {i + 1}")

# Example 2: Generate sequence
print("\nExample 2: Generate squares of first 10 numbers")
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(f"Squares: {squares}")

# Example 3: Sum of numbers
print("\nExample 3: Sum of numbers 1 to 100")
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")

# Example 4: Multiplication table
print("\nExample 4: Multiplication table of 7")
for i in range(1, 11):
    print(f"7 × {i} = {7 * i}")

# Range with Lists
print("\n" + "=" * 50)
print("RANGE WITH LISTS:")
print("=" * 50)

fruits = ["apple", "banana", "orange", "grape", "mango"]

print("Using range with list length:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("\nAccessing every other element:")
for i in range(0, len(fruits), 2):
    print(f"Index {i}: {fruits[i]}")

print("\nReversing list with range:")
for i in range(len(fruits) - 1, -1, -1):
    print(f"Index {i}: {fruits[i]}")

# Real-world Example: Temperature Conversion
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TEMPERATURE CONVERSION")
print("=" * 50)

print("Celsius to Fahrenheit (0°C to 100°C, step 10):")
print(f"{'Celsius':>8} {'Fahrenheit':>12}")
print("-" * 22)
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:>8}°C {fahrenheit:>11.1f}°F")

# Real-world Example: Price List
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: BULK PRICING")
print("=" * 50)

base_price = 10
print(f"Base price: ${base_price}")
print(f"{'Quantity':>10} {'Unit Price':>12} {'Total':>10}")
print("-" * 35)

for quantity in range(1, 11):
    if quantity >= 5:
        unit_price = base_price * 0.9  # 10% discount
    else:
        unit_price = base_price
    
    total = unit_price * quantity
    print(f"{quantity:>10} ${unit_price:>11.2f} ${total:>9.2f}")

# Real-world Example: Password Generator
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SIMPLE NUMBER PASSWORDS")
print("=" * 50)

print("Generating 5 simple numeric passwords (4 digits):")
import random
random.seed(42)  # For consistent results

for i in range(5):
    password = ""
    for j in range(4):
        digit = random.randint(0, 9)
        password += str(digit)
    print(f"Password {i + 1}: {password}")

# Real-world Example: Progress Bar
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: PROGRESS BAR")
print("=" * 50)

import time

print("Loading...")
for i in range(0, 101, 10):
    bar = "█" * (i // 10) + "░" * (10 - i // 10)
    print(f"\r[{bar}] {i}%", end="", flush=True)
    # time.sleep(0.2)  # Uncomment to see animation
print("\n✓ Complete!")

# Real-world Example: Seating Numbers
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: EVENT SEATING")
print("=" * 50)

rows = 5
seats_per_row = 10
seat_number = 1

print("Seat numbering for event:")
for row in range(1, rows + 1):
    print(f"Row {row}: ", end="")
    for seat in range(seats_per_row):
        print(f"S{seat_number:03d}", end=" ")
        seat_number += 1
    print()

# Real-world Example: Age Groups
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: AGE GROUP CLASSIFICATION")
print("=" * 50)

print("Age group classifications:")
age_ranges = [
    (0, 13, "Child"),
    (13, 18, "Teenager"),
    (18, 65, "Adult"),
    (65, 100, "Senior")
]

for start, end, category in age_ranges:
    count = len(list(range(start, end)))
    print(f"{category:>10}: Ages {start}-{end-1} ({count} years)")

# Range Memory Efficiency
print("\n" + "=" * 50)
print("RANGE MEMORY EFFICIENCY:")
print("=" * 50)

import sys

# Range object
r = range(1000000)
print(f"Size of range(1000000): {sys.getsizeof(r)} bytes")

# List object
lst = list(range(1000))
print(f"Size of list(range(1000)): {sys.getsizeof(lst)} bytes")

print("\n✓ range() is memory efficient - generates numbers on demand")
print("✓ list(range()) creates all numbers in memory at once")

# Common Range Patterns
print("\n" + "=" * 50)
print("COMMON RANGE PATTERNS:")
print("=" * 50)

print("1. Count from 0 to n-1:")
print("   range(n)")
print("   Example: range(5) → 0, 1, 2, 3, 4\n")

print("2. Count from 1 to n:")
print("   range(1, n+1)")
print("   Example: range(1, 6) → 1, 2, 3, 4, 5\n")

print("3. Count backwards:")
print("   range(n, 0, -1)")
print("   Example: range(5, 0, -1) → 5, 4, 3, 2, 1\n")

print("4. Even numbers:")
print("   range(0, n, 2)")
print("   Example: range(0, 10, 2) → 0, 2, 4, 6, 8\n")

print("5. Odd numbers:")
print("   range(1, n, 2)")
print("   Example: range(1, 10, 2) → 1, 3, 5, 7, 9\n")

# Range Tricks
print("=" * 50)
print("RANGE TRICKS:")
print("=" * 50)

# Reverse iteration
print("1. Reverse iteration over list:")
items = ["a", "b", "c", "d", "e"]
for i in range(len(items) - 1, -1, -1):
    print(f"  {items[i]}", end=" ")
print()

# Skip elements
print("\n2. Process every 3rd element:")
numbers = list(range(20))
for i in range(0, len(numbers), 3):
    print(f"  {numbers[i]}", end=" ")
print()

# Nested range
print("\n3. Coordinate pairs:")
for x in range(3):
    for y in range(3):
        print(f"({x},{y})", end=" ")
    print()

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Use range to print all multiples of 7 between 1 and 100")
print("2. Create a countdown timer from 60 to 0 by 5s")
print("3. Generate a list of squares for numbers 1-20 using range")
print("4. Print a triangle pattern using nested ranges")
print("5. Use range to iterate backwards through a list")
print("6. Calculate factorial of a number using range")
print("7. Print all numbers divisible by both 3 and 5 up to 100")
print("8. Create a simple ASCII art using range and loops")