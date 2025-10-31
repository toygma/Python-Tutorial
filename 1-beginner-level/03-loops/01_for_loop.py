# FILE: 01_for_loop.py
"""
FOR LOOP
========

The for loop is used for iterating over a sequence (list, tuple, string, etc.)

Key Concepts:
- Iterating over sequences
- range() function
- Loop with index
- Nested loops
"""

# Basic for loop with list
print("BASIC FOR LOOP:")
print("=" * 50)

fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with string
print("\nLOOP THROUGH STRING:")
print("=" * 50)

word = "Python"
for letter in word:
    print(letter, end=" ")
print()  # New line

# For loop with range()
print("\nFOR LOOP WITH RANGE:")
print("=" * 50)

# range(stop) - from 0 to stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop) - from start to stop-1
print("\nrange(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()

# range(start, stop, step) - with step
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Loop with index using enumerate()
print("\n" + "=" * 50)
print("LOOP WITH INDEX:")

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Starting enumerate from different number
print("\nStarting from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Nested loops
print("\n" + "=" * 50)
print("NESTED LOOPS:")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()  # New line after inner loop

# Print multiplication table
print("\nMultiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# Loop through dictionary
print("\n" + "=" * 50)
print("LOOP THROUGH DICTIONARY:")

student = {"name": "John", "age": 20, "grade": "A"}

print("Keys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# Real-world example: Sum of numbers
print("\n" + "=" * 50)
print("EXAMPLE: SUM OF NUMBERS")

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Real-world example: Find maximum
print("\nEXAMPLE: FIND MAXIMUM")

numbers = [15, 42, 8, 23, 67, 91, 34]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Print all even numbers from 1 to 20")
print("2. Calculate factorial of a number using for loop")
print("3. Count vowels in a string")
print("4. Print a pyramid pattern using nested loops")