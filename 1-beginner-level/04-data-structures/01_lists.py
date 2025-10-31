# FILE: 01_lists.py
"""
LISTS
=====

Lists are ordered, mutable (changeable) collections that can store multiple
items in a single variable. Lists can contain items of different data types.

Key Concepts:
- Creating lists
- Accessing elements (indexing)
- List slicing
- Modifying lists
- List operations
- Nested lists
"""

# Creating Lists
print("CREATING LISTS:")
print("=" * 50)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with integers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# List with strings
fruits = ["apple", "banana", "orange", "grape"]
print(f"Fruits: {fruits}")

# List with mixed data types
mixed = [1, "hello", 3.14, True, None]
print(f"Mixed types: {mixed}")

# List with duplicates
duplicates = [1, 2, 2, 3, 3, 3, 4]
print(f"With duplicates: {duplicates}")

# Using list() constructor
chars = list("Python")
print(f"From string: {chars}")

range_list = list(range(1, 6))
print(f"From range: {range_list}")

# Accessing List Elements (Indexing)
print("\n" + "=" * 50)
print("ACCESSING ELEMENTS:")
print("=" * 50)

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"List: {colors}")

# Positive indexing (starts at 0)
print(f"\nFirst element [0]: {colors[0]}")
print(f"Second element [1]: {colors[1]}")
print(f"Third element [2]: {colors[2]}")

# Negative indexing (starts from end)
print(f"\nLast element [-1]: {colors[-1]}")
print(f"Second last [-2]: {colors[-2]}")
print(f"Third last [-3]: {colors[-3]}")

# Visual representation
print("\nIndex visualization:")
print("Positive: 0      1        2       3         4")
print(f"List:     {colors}")
print("Negative: -5     -4       -3      -2        -1")

# List Slicing
print("\n" + "=" * 50)
print("LIST SLICING:")
print("=" * 50)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List: {numbers}")

# Basic slicing [start:stop]
print(f"\nnumbers[2:5]: {numbers[2:5]}")  # Elements at index 2, 3, 4
print(f"numbers[0:3]: {numbers[0:3]}")    # First 3 elements
print(f"numbers[5:9]: {numbers[5:9]}")    # Elements 5 to 8

# Omitting start or stop
print(f"\nnumbers[:5]: {numbers[:5]}")    # From beginning to index 4
print(f"numbers[5:]: {numbers[5:]}")      # From index 5 to end
print(f"numbers[:]: {numbers[:]}")        # Entire list (copy)

# Negative indices in slicing
print(f"\nnumbers[-3:]: {numbers[-3:]}")  # Last 3 elements
print(f"numbers[:-3]: {numbers[:-3]}")    # All except last 3
print(f"numbers[-5:-2]: {numbers[-5:-2]}")  # From -5 to -3

# Slicing with step [start:stop:step]
print(f"\nnumbers[::2]: {numbers[::2]}")    # Every 2nd element
print(f"numbers[1::2]: {numbers[1::2]}")   # Every 2nd starting from index 1
print(f"numbers[::3]: {numbers[::3]}")     # Every 3rd element
print(f"numbers[::-1]: {numbers[::-1]}")   # Reverse the list

# Modifying Lists
print("\n" + "=" * 50)
print("MODIFYING LISTS:")
print("=" * 50)

# Changing single element
shopping = ["milk", "bread", "eggs", "butter"]
print(f"Original: {shopping}")

shopping[1] = "whole wheat bread"
print(f"After change: {shopping}")

# Changing multiple elements with slicing
numbers = [1, 2, 3, 4, 5]
print(f"\nOriginal: {numbers}")
numbers[1:4] = [20, 30, 40]
print(f"After slice modification: {numbers}")

# Replace with different length
letters = ['a', 'b', 'c', 'd', 'e']
print(f"\nOriginal: {letters}")
letters[1:4] = ['x', 'y']
print(f"After replacement: {letters}")

# List Length
print("\n" + "=" * 50)
print("LIST LENGTH:")
print("=" * 50)

fruits = ["apple", "banana", "orange"]
print(f"List: {fruits}")
print(f"Length: {len(fruits)}")

empty = []
print(f"\nEmpty list: {empty}")
print(f"Length: {len(empty)}")

# Checking if List is Empty
print("\n" + "=" * 50)
print("CHECKING IF LIST IS EMPTY:")
print("=" * 50)

list1 = []
list2 = [1, 2, 3]

print(f"list1 = {list1}")
print(f"Is empty (using len): {len(list1) == 0}")
print(f"Is empty (using not): {not list1}")

print(f"\nlist2 = {list2}")
print(f"Is empty: {not list2}")

# List Membership (in operator)
print("\n" + "=" * 50)
print("LIST MEMBERSHIP:")
print("=" * 50)

fruits = ["apple", "banana", "orange", "grape"]
print(f"List: {fruits}")

print(f"\n'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")
print(f"'kiwi' not in fruits: {'kiwi' not in fruits}")

# List Concatenation
print("\n" + "=" * 50)
print("LIST CONCATENATION:")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"combined: {combined}")

# Original lists unchanged
print(f"\nlist1 still: {list1}")
print(f"list2 still: {list2}")

# List Repetition
print("\n" + "=" * 50)
print("LIST REPETITION:")
print("=" * 50)

zeros = [0] * 5
print(f"[0] * 5 = {zeros}")

pattern = [1, 2] * 3
print(f"[1, 2] * 3 = {pattern}")

chars = ['x'] * 10
print(f"['x'] * 10 = {chars}")

# Nested Lists (Lists within Lists)
print("\n" + "=" * 50)
print("NESTED LISTS:")
print("=" * 50)

# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Accessing nested list elements
print(f"\nFirst row: {matrix[0]}")
print(f"Second row: {matrix[1]}")
print(f"Element at [0][0]: {matrix[0][0]}")
print(f"Element at [1][2]: {matrix[1][2]}")
print(f"Element at [2][1]: {matrix[2][1]}")

# Mixed nested list
students = [
    ["Alice", 20, [85, 90, 88]],
    ["Bob", 21, [78, 82, 80]],
    ["Charlie", 19, [92, 95, 90]]
]

print("\nStudents data:")
for student in students:
    name, age, scores = student
    print(f"{name}, age {age}, scores: {scores}")

# List Comparison
print("\n" + "=" * 50)
print("LIST COMPARISON:")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

print(f"\nlist1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")    # False (different objects)
print(f"list1 == list3: {list1 == list3}")    # False
print(f"list1 < list3: {list1 < list3}")      # True (lexicographic)

# Copying Lists
print("\n" + "=" * 50)
print("COPYING LISTS:")
print("=" * 50)

original = [1, 2, 3, 4, 5]
print(f"Original: {original}")

# Shallow copy methods
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

print(f"copy1 (using .copy()): {copy1}")
print(f"copy2 (using list()): {copy2}")
print(f"copy3 (using [:]): {copy3}")

# Modify original
original[0] = 999
print(f"\nAfter modifying original[0] = 999:")
print(f"Original: {original}")
print(f"copy1: {copy1}")  # Unchanged
print(f"copy2: {copy2}")  # Unchanged

# Reference (not a copy!)
reference = original
print(f"\nreference = original")
print(f"reference: {reference}")
original[0] = 111
print(f"After changing original[0] = 111:")
print(f"Original: {original}")
print(f"reference: {reference}")  # Changed too!

# List Iteration
print("\n" + "=" * 50)
print("LIST ITERATION:")
print("=" * 50)

fruits = ["apple", "banana", "orange", "grape"]

print("Method 1: Direct iteration")
for fruit in fruits:
    print(f"  {fruit}")

print("\nMethod 2: With index using range")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

print("\nMethod 3: With enumerate")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Min, Max, Sum
print("\n" + "=" * 50)
print("MIN, MAX, SUM:")
print("=" * 50)

numbers = [45, 23, 67, 12, 89, 34, 56]
print(f"Numbers: {numbers}")

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# Works with strings too
words = ["zebra", "apple", "banana", "mango"]
print(f"\nWords: {words}")
print(f"Min (alphabetically): {min(words)}")
print(f"Max (alphabetically): {max(words)}")

# List Unpacking
print("\n" + "=" * 50)
print("LIST UNPACKING:")
print("=" * 50)

# Basic unpacking
coordinates = [10, 20]
x, y = coordinates
print(f"coordinates: {coordinates}")
print(f"x = {x}, y = {y}")

# Unpacking with more elements
rgb = [255, 128, 0]
r, g, b = rgb
print(f"\nrgb: {rgb}")
print(f"r = {r}, g = {g}, b = {b}")

# Unpacking with * (rest)
numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print(f"\nnumbers: {numbers}")
print(f"first: {first}")
print(f"middle: {middle}")
print(f"last: {last}")

first, second, *rest = numbers
print(f"\nfirst: {first}, second: {second}, rest: {rest}")

# Real-world Example: Shopping List
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SHOPPING LIST")
print("=" * 50)

shopping_list = ["milk", "bread", "eggs", "butter", "cheese"]

print("My Shopping List:")
for index, item in enumerate(shopping_list, 1):
    print(f"{index}. {item}")

print(f"\nTotal items: {len(shopping_list)}")
print(f"First item to buy: {shopping_list[0]}")
print(f"Last item: {shopping_list[-1]}")

# Check if item is on list
if "eggs" in shopping_list:
    print("\n✓ Don't forget to buy eggs!")

# Real-world Example: Test Scores
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TEST SCORES")
print("=" * 50)

scores = [85, 92, 78, 95, 88, 73, 90]

print(f"Test Scores: {scores}")
print(f"Number of tests: {len(scores)}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {sum(scores) / len(scores):.2f}")

print("\nScores above 85:")
for index, score in enumerate(scores, 1):
    if score > 85:
        print(f"  Test {index}: {score}")

# Real-world Example: To-Do List
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TO-DO LIST")
print("=" * 50)

tasks = [
    "Buy groceries",
    "Finish homework",
    "Call dentist",
    "Clean room"
]

print("TODAY'S TASKS:")
for i, task in enumerate(tasks, 1):
    print(f"[ ] {i}. {task}")

print(f"\nTasks remaining: {len(tasks)}")

# List of Lists Example: Student Records
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: STUDENT RECORDS")
print("=" * 50)

students = [
    ["Alice", 20, "A"],
    ["Bob", 21, "B"],
    ["Charlie", 19, "A"],
    ["Diana", 22, "C"]
]

print(f"{'Name':<12} {'Age':>5} {'Grade':>8}")
print("-" * 28)
for student in students:
    name, age, grade = student
    print(f"{name:<12} {age:>5} {grade:>8}")

# Common List Patterns
print("\n" + "=" * 50)
print("COMMON LIST PATTERNS:")
print("=" * 50)

# Create list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Create list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# Reverse a list
numbers = [1, 2, 3, 4, 5]
reversed_nums = numbers[::-1]
print(f"Original: {numbers}")
print(f"Reversed: {reversed_nums}")

# Get first n elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_five = numbers[:5]
print(f"First 5: {first_five}")

# Get last n elements
last_three = numbers[-3:]
print(f"Last 3: {last_three}")

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a list of your 5 favorite movies")
print("2. Access and print the first and last movie")
print("3. Add a new movie to the list")
print("4. Create a list of numbers 1-20 and extract even numbers")
print("5. Create a 2D list representing a 3x3 tic-tac-toe board")
print("6. Calculate the sum of all numbers from 1 to 100 using a list")
print("7. Create a list of temperatures and find the average")
print("8. Reverse a list without using [::-1] or reverse()")