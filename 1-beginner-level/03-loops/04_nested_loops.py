# FILE: 04_nested_loops.py
"""
NESTED LOOPS
============

Nested loops are loops inside other loops. The inner loop completes all its
iterations for each iteration of the outer loop.

Key Concepts:
- Loop inside loop structure
- Execution order
- 2D data processing
- Pattern printing
- Performance considerations
"""

# Basic Nested Loop
print("BASIC NESTED LOOP:")
print("=" * 50)

print("Example 1: Simple nested loop")
for i in range(3):
    print(f"Outer loop iteration {i}")
    for j in range(2):
        print(f"  Inner loop iteration {j}")
    print()

# Execution count demonstration
print("Example 2: How many times does inner loop run?")
count = 0
for i in range(3):
    for j in range(4):
        count += 1
        print(f"({i},{j})", end=" ")
    print()
print(f"Total iterations: {count}")

# Multiplication Table
print("\n" + "=" * 50)
print("MULTIPLICATION TABLE:")
print("=" * 50)

print("5x5 Multiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{result:3}", end=" ")
    print()

# With labels
print("\nWith row and column labels:")
print("    ", end="")
for j in range(1, 6):
    print(f"{j:3}", end=" ")
print()
print("    " + "----" * 5)

for i in range(1, 6):
    print(f"{i} | ", end="")
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# Pattern Printing
print("\n" + "=" * 50)
print("PATTERN PRINTING:")
print("=" * 50)

# Pattern 1: Right triangle
print("Pattern 1: Right triangle")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 2: Inverted right triangle
print("\nPattern 2: Inverted right triangle")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 3: Pyramid
print("\nPattern 3: Pyramid")
n = 5
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Pattern 4: Diamond
print("\nPattern 4: Diamond")
n = 5
# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Pattern 5: Number pyramid
print("\nPattern 5: Number pyramid")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# Working with 2D Lists (Matrices)
print("\n" + "=" * 50)
print("WORKING WITH 2D LISTS:")
print("=" * 50)

# Creating a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    for element in row:
        print(f"{element:3}", end=" ")
    print()

# Accessing elements
print("\nAccessing all elements:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# Sum of all elements
print("\nSum of all elements:")
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Total: {total}")

# Matrix Operations
print("\n" + "=" * 50)
print("MATRIX OPERATIONS:")
print("=" * 50)

# Matrix addition
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nMatrix Addition (Matrix1 + Matrix2):")
result = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[i])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

for row in result:
    print(row)

# Matrix transpose
print("\nMatrix Transpose:")
original = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Original (2x3):")
for row in original:
    print(row)

transpose = []
for j in range(len(original[0])):
    row = []
    for i in range(len(original)):
        row.append(original[i][j])
    transpose.append(row)

print("\nTransposed (3x2):")
for row in transpose:
    print(row)

# Nested Loop with Break
print("\n" + "=" * 50)
print("NESTED LOOPS WITH BREAK:")
print("=" * 50)

print("Finding a value in 2D array:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

search = 5
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"Checking position ({i},{j}): {matrix[i][j]}")
        if matrix[i][j] == search:
            print(f"✓ Found {search} at position ({i},{j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"✗ {search} not found")

# Real-world Example: Seating Arrangement
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SEATING ARRANGEMENT")
print("=" * 50)

# Create seating chart (5 rows, 6 seats per row)
seats = []
for row in range(5):
    seat_row = []
    for seat in range(6):
        seat_row.append("O")  # O = available
    seats.append(seat_row)

# Book some seats
seats[0][2] = "X"  # X = booked
seats[1][3] = "X"
seats[2][1] = "X"
seats[2][4] = "X"
seats[3][0] = "X"

print("Theater Seating Chart:")
print("  ", end="")
for seat_num in range(6):
    print(f"S{seat_num+1}", end=" ")
print()

for i, row in enumerate(seats):
    print(f"R{i+1}", end=" ")
    for seat in row:
        print(f" {seat}", end=" ")
    print()

print("\nO = Available, X = Booked")

# Count available seats
available = 0
for row in seats:
    for seat in row:
        if seat == "O":
            available += 1
print(f"\nAvailable seats: {available}")

# Real-world Example: Grade Sheet
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: GRADE SHEET")
print("=" * 50)

# Students and their test scores
students = ["Alice", "Bob", "Charlie", "Diana"]
scores = [
    [85, 90, 88],  # Alice's scores
    [78, 82, 80],  # Bob's scores
    [92, 95, 90],  # Charlie's scores
    [70, 75, 72]   # Diana's scores
]

print("Student Grade Report:")
print(f"{'Name':<10}", end="")
for i in range(len(scores[0])):
    print(f"Test{i+1:>6}", end="")
print(f"{'Average':>8}")
print("-" * 40)

for i in range(len(students)):
    print(f"{students[i]:<10}", end="")
    total = 0
    for j in range(len(scores[i])):
        print(f"{scores[i][j]:>6}", end="")
        total += scores[i][j]
    average = total / len(scores[i])
    print(f"{average:>8.1f}")

# Class averages per test
print("\nTest Averages:")
for j in range(len(scores[0])):
    total = 0
    for i in range(len(scores)):
        total += scores[i][j]
    average = total / len(scores)
    print(f"Test {j+1}: {average:.1f}")

# Real-world Example: Tic-Tac-Toe Board
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TIC-TAC-TOE")
print("=" * 50)

# Create game board
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

print("Tic-Tac-Toe Board:")
print("  0   1   2")
for i in range(3):
    print(i, end=" ")
    for j in range(3):
        print(f"{board[i][j]}", end="")
        if j < 2:
            print(" | ", end="")
    print()
    if i < 2:
        print(" ---+---+---")

# Check for winner (simplified)
print("\nChecking rows for winner:")
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
        print(f"Row {i}: {board[i][0]} wins!")

# Real-world Example: Calendar
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: MONTHLY CALENDAR")
print("=" * 50)

# Simple calendar for a 30-day month starting on Wednesday (day 2)
print("Mo Tu We Th Fr Sa Su")
print("               ", end="")  # First week starts on Wednesday

day = 1
# First week (starting Wednesday)
for i in range(5):  # Wed to Sun
    print(f"{day:2} ", end="")
    day += 1
print()

# Full weeks
while day <= 30:
    for i in range(7):
        if day <= 30:
            print(f"{day:2} ", end="")
            day += 1
        else:
            print("   ", end="")
    print()

# Real-world Example: Product Inventory
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: INVENTORY CHECK")
print("=" * 50)

# Warehouses and their product stock
warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]
products = ["Laptop", "Mouse", "Keyboard"]
inventory = [
    [10, 25, 15],  # Warehouse A
    [5, 30, 20],   # Warehouse B
    [0, 15, 10]    # Warehouse C
]

print("Inventory Report:")
print(f"{'Product':<12}", end="")
for warehouse in warehouses:
    print(f"{warehouse:>15}", end="")
print(f"{'Total':>10}")
print("-" * 60)

for i in range(len(products)):
    print(f"{products[i]:<12}", end="")
    total = 0
    for j in range(len(warehouses)):
        print(f"{inventory[j][i]:>15}", end="")
        total += inventory[j][i]
    print(f"{total:>10}")

# Check for out of stock items
print("\nOut of Stock Items:")
for i in range(len(products)):
    for j in range(len(warehouses)):
        if inventory[j][i] == 0:
            print(f"  {products[i]} at {warehouses[j]}")

# Nested Loop Performance
print("\n" + "=" * 50)
print("PERFORMANCE CONSIDERATION:")
print("=" * 50)
print("""
Time Complexity of Nested Loops:
- Single loop: O(n)
- Two nested loops: O(n²)
- Three nested loops: O(n³)

Example:
for i in range(n):      # Runs n times
    for j in range(n):  # Runs n times for each i
        # Code here runs n × n = n² times
""")

# Practice Exercises:
print("=" * 50)
print("--- EXERCISES ---")
print("1. Create a program to print Pascal's triangle")
print("2. Write a nested loop to find all prime numbers up to 100")
print("3. Build a times table (1-12) with proper formatting")
print("4. Create a checkerboard pattern using nested loops")
print("5. Make a program to rotate a matrix 90 degrees")
print("6. Write code to find all pairs in an array that sum to a target")
print("7. Create a nested loop to simulate a simple game grid")
print("8. Build a program to print a hollow square pattern")