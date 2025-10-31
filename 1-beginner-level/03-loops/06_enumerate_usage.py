# FILE: 06_enumerate_usage.py
"""
ENUMERATE USAGE
===============

The enumerate() function adds a counter to an iterable and returns it as an
enumerate object. This makes it easy to get both the index and value while looping.

Syntax: enumerate(iterable, start=0)

Key Concepts:
- Basic enumerate usage
- Custom start index
- Enumerate with different data types
- Unpacking enumerate tuples
- Practical applications
"""

# Basic Enumerate
print("BASIC ENUMERATE:")
print("=" * 50)

fruits = ["apple", "banana", "orange", "grape"]

print("Without enumerate (using range):")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("\nWith enumerate (cleaner):")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Enumerate Returns Tuples
print("\n" + "=" * 50)
print("ENUMERATE RETURNS TUPLES:")
print("=" * 50)

colors = ["red", "green", "blue"]

print("Enumerate object:")
print(enumerate(colors))

print("\nConverting to list:")
print(list(enumerate(colors)))

print("\nIterating without unpacking:")
for item in enumerate(colors):
    print(f"Tuple: {item}, Type: {type(item)}")

print("\nIterating with unpacking:")
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

# Custom Start Index
print("\n" + "=" * 50)
print("CUSTOM START INDEX:")
print("=" * 50)

subjects = ["Math", "Science", "English", "History"]

print("Default start (0):")
for index, subject in enumerate(subjects):
    print(f"{index}. {subject}")

print("\nStart from 1:")
for index, subject in enumerate(subjects, start=1):
    print(f"{index}. {subject}")

print("\nStart from 10:")
for index, subject in enumerate(subjects, start=10):
    print(f"{index}. {subject}")

print("\nStart from 100:")
for index, subject in enumerate(subjects, start=100):
    print(f"ID-{index}: {subject}")

# Enumerate with Strings
print("\n" + "=" * 50)
print("ENUMERATE WITH STRINGS:")
print("=" * 50)

text = "Python"

print(f"String: {text}")
print("\nCharacter positions:")
for index, char in enumerate(text):
    print(f"Position {index}: '{char}'")

print("\nStarting from 1:")
for index, char in enumerate(text, 1):
    print(f"Character {index}: '{char}'")

# Enumerate with Tuples
print("\n" + "=" * 50)
print("ENUMERATE WITH TUPLES:")
print("=" * 50)

coordinates = (10, 20, 30, 40, 50)

print(f"Tuple: {coordinates}")
for index, value in enumerate(coordinates):
    print(f"Index {index}: {value}")

# Enumerate with Dictionaries
print("\n" + "=" * 50)
print("ENUMERATE WITH DICTIONARIES:")
print("=" * 50)

student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "city": "New York"
}

print("Enumerate keys:")
for index, key in enumerate(student.keys()):
    print(f"{index}: {key}")

print("\nEnumerate values:")
for index, value in enumerate(student.values()):
    print(f"{index}: {value}")

print("\nEnumerate items:")
for index, (key, value) in enumerate(student.items()):
    print(f"{index}: {key} = {value}")

print("\nEnumerate items (starting from 1):")
for index, (key, value) in enumerate(student.items(), 1):
    print(f"{index}. {key}: {value}")

# Finding Index of Elements
print("\n" + "=" * 50)
print("FINDING INDEX OF ELEMENTS:")
print("=" * 50)

numbers = [10, 20, 30, 40, 50, 30, 60]

print(f"List: {numbers}")
print("\nFind all indices of 30:")
for index, num in enumerate(numbers):
    if num == 30:
        print(f"Found 30 at index {index}")

print("\nFind first occurrence of 40:")
for index, num in enumerate(numbers):
    if num == 40:
        print(f"First occurrence of 40 at index {index}")
        break

# Enumerate with Conditions
print("\n" + "=" * 50)
print("ENUMERATE WITH CONDITIONS:")
print("=" * 50)

scores = [85, 92, 78, 95, 88, 73, 90]

print("Scores above 85:")
for index, score in enumerate(scores, 1):
    if score > 85:
        print(f"Student {index}: {score}")

print("\nScores below 80:")
for index, score in enumerate(scores, 1):
    if score < 80:
        print(f"Student {index}: {score} (needs improvement)")

# Real-world Example: Menu System
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: MENU SYSTEM")
print("=" * 50)

menu_items = [
    "View Profile",
    "Edit Settings",
    "Change Password",
    "Logout"
]

print("=== MAIN MENU ===")
for index, item in enumerate(menu_items, 1):
    print(f"{index}. {item}")

print("\nUser selects option 2:")
selected = 2
for index, item in enumerate(menu_items, 1):
    if index == selected:
        print(f"Selected: {item}")

# Real-world Example: Shopping Cart
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SHOPPING CART")
print("=" * 50)

cart = [
    {"item": "Laptop", "price": 999.99, "qty": 1},
    {"item": "Mouse", "price": 29.99, "qty": 2},
    {"item": "Keyboard", "price": 79.99, "qty": 1},
    {"item": "Monitor", "price": 299.99, "qty": 1}
]

print("=== SHOPPING CART ===")
print(f"{'#':<3} {'Item':<15} {'Price':>10} {'Qty':>5} {'Total':>10}")
print("-" * 50)

grand_total = 0
for index, product in enumerate(cart, 1):
    total = product["price"] * product["qty"]
    grand_total += total
    print(f"{index:<3} {product['item']:<15} ${product['price']:>9.2f} {product['qty']:>5} ${total:>9.2f}")

print("-" * 50)
print(f"{'Grand Total:':<34} ${grand_total:>9.2f}")

# Real-world Example: Student Ranking
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: STUDENT RANKING")
print("=" * 50)

students = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie", "score": 92},
    {"name": "Diana", "score": 97},
    {"name": "Eve", "score": 85}
]

# Sort by score (descending)
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

print("=== LEADERBOARD ===")
print(f"{'Rank':<6} {'Name':<15} {'Score':>8}")
print("-" * 32)

for rank, student in enumerate(sorted_students, 1):
    medal = ""
    if rank == 1:
        medal = "🥇"
    elif rank == 2:
        medal = "🥈"
    elif rank == 3:
        medal = "🥉"
    
    print(f"{rank:<6} {student['name']:<15} {student['score']:>8} {medal}")

# Real-world Example: File Processing
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: LOG FILE PROCESSING")
print("=" * 50)

log_lines = [
    "INFO: Application started",
    "DEBUG: Loading configuration",
    "ERROR: Failed to connect to database",
    "INFO: Retrying connection",
    "INFO: Connection successful",
    "WARNING: High memory usage detected",
    "ERROR: Timeout occurred"
]

print("Processing log file:")
error_count = 0
warning_count = 0

for line_num, line in enumerate(log_lines, 1):
    print(f"Line {line_num}: {line}")
    if "ERROR" in line:
        error_count += 1
    elif "WARNING" in line:
        warning_count += 1

print(f"\nSummary:")
print(f"Total lines: {len(log_lines)}")
print(f"Errors: {error_count}")
print(f"Warnings: {warning_count}")

# Real-world Example: To-Do List
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TO-DO LIST")
print("=" * 50)

tasks = [
    {"task": "Buy groceries", "completed": False},
    {"task": "Finish homework", "completed": True},
    {"task": "Call dentist", "completed": False},
    {"task": "Clean room", "completed": True},
    {"task": "Study Python", "completed": False}
]

print("=== MY TO-DO LIST ===")
for index, item in enumerate(tasks, 1):
    status = "✓" if item["completed"] else "☐"
    print(f"{index}. [{status}] {item['task']}")

print("\nPending tasks:")
for index, item in enumerate(tasks, 1):
    if not item["completed"]:
        print(f"  {index}. {item['task']}")

# Real-world Example: Table Generation
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: EMPLOYEE TABLE")
print("=" * 50)

employees = [
    {"name": "John Doe", "position": "Manager", "salary": 75000},
    {"name": "Jane Smith", "position": "Developer", "salary": 65000},
    {"name": "Bob Johnson", "position": "Designer", "salary": 60000},
    {"name": "Alice Brown", "position": "Developer", "salary": 68000}
]

print(f"{'ID':<5} {'Name':<20} {'Position':<15} {'Salary':>10}")
print("=" * 55)

for emp_id, employee in enumerate(employees, 1001):
    print(f"{emp_id:<5} {employee['name']:<20} {employee['position']:<15} ${employee['salary']:>9,}")

# Enumerate with List Comprehension
print("\n" + "=" * 50)
print("ENUMERATE WITH LIST COMPREHENSION:")
print("=" * 50)

words = ["hello", "world", "python", "programming"]

# Create list of tuples (index, word)
indexed_words = [(i, word) for i, word in enumerate(words)]
print(f"Indexed words: {indexed_words}")

# Create list with position labels
labeled_words = [f"{i+1}. {word}" for i, word in enumerate(words)]
print(f"Labeled words: {labeled_words}")

# Filter with index
print("\nWords at even indices:")
even_index_words = [word for i, word in enumerate(words) if i % 2 == 0]
print(even_index_words)

# Enumerate vs Range Comparison
print("\n" + "=" * 50)
print("ENUMERATE vs RANGE COMPARISON:")
print("=" * 50)

items = ["a", "b", "c", "d", "e"]

print("Using range (old way):")
for i in range(len(items)):
    print(f"  {i}: {items[i]}")

print("\nUsing enumerate (Pythonic way):")
for i, item in enumerate(items):
    print(f"  {i}: {item}")

print("\nEnumerate is:")
print("  ✓ More readable")
print("  ✓ More Pythonic")
print("  ✓ Less error-prone")
print("  ✓ Works with any iterable")

# Modifying List with Enumerate
print("\n" + "=" * 50)
print("MODIFYING LIST WITH ENUMERATE:")
print("=" * 50)

numbers = [10, 20, 30, 40, 50]
print(f"Original: {numbers}")

# Double all values
for index, value in enumerate(numbers):
    numbers[index] = value * 2

print(f"Doubled: {numbers}")

# Add index to each value
for index, value in enumerate(numbers):
    numbers[index] = value + index

print(f"Added index: {numbers}")

# Enumerate with Multiple Lists (zip + enumerate)
print("\n" + "=" * 50)
print("ENUMERATE WITH MULTIPLE LISTS:")
print("=" * 50)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

print("Combined data:")
for index, (name, age, city) in enumerate(zip(names, ages, cities), 1):
    print(f"{index}. {name}, {age} years old, from {city}")

# Common Patterns
print("\n" + "=" * 50)
print("COMMON ENUMERATE PATTERNS:")
print("=" * 50)

data = ["first", "second", "third", "fourth", "fifth"]

print("1. Standard enumeration:")
for i, item in enumerate(data):
    print(f"  {i}: {item}")

print("\n2. Start from 1:")
for i, item in enumerate(data, 1):
    print(f"  {i}. {item}")

print("\n3. With condition:")
for i, item in enumerate(data):
    if i % 2 == 0:
        print(f"  Even index {i}: {item}")

print("\n4. Reverse enumeration:")
for i, item in enumerate(reversed(data)):
    print(f"  {i}: {item}")

# Practice Exercises:
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a numbered list of your favorite movies (starting from 1)")
print("2. Find all positions of letter 'a' in a string using enumerate")
print("3. Build a contacts list with numbered entries")
print("4. Create a quiz program with numbered questions")
print("5. Make a playlist where each song has a track number")
print("6. Process a list and print both index and value for even indices only")
print("7. Create an invoice with line numbers for each item")
print("8. Build a table of contents with page numbers using enumerate")