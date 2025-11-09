"""
TUPLES
======

Tuples are ordered, immutable (unchangeable) collections that can store multiple
items in a single variable. Once created, tuples cannot be modified.

Key Concepts:
- Creating tuples
- Accessing elements
- Tuple operations
- Immutability
- Tuple methods
- Packing and unpacking
- When to use tuples vs lists

Why use tuples?
- Faster than lists
- Protect data from modification
- Can be used as dictionary keys
- Good for fixed collections
"""

# Creating Tuples
print("CREATING TUPLES:")
print("=" * 50)

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")
print(f"Type: {type(empty_tuple)}")

# Tuple with parentheses
fruits = ("apple", "banana", "orange")
print(f"\nFruits: {fruits}")
print(f"Type: {type(fruits)}")

# Tuple without parentheses (tuple packing)
colors = "red", "green", "blue"
print(f"\nColors: {colors}")
print(f"Type: {type(colors)}")

# Single element tuple (comma is required!)
single = (5,)  # Correct
print(f"\nSingle element: {single}")
print(f"Type: {type(single)}")

not_tuple = (5)  # This is just an integer!
print(f"Without comma: {not_tuple}")
print(f"Type: {type(not_tuple)}")

# Tuple with mixed data types
mixed = (1, "hello", 3.14, True, None)
print(f"\nMixed types: {mixed}")

# Tuple with duplicates
duplicates = (1, 2, 2, 3, 3, 3, 4)
print(f"With duplicates: {duplicates}")

# Using tuple() constructor
from_list = tuple([1, 2, 3, 4, 5])
print(f"\nFrom list: {from_list}")

from_string = tuple("Python")
print(f"From string: {from_string}")

from_range = tuple(range(1, 6))
print(f"From range: {from_range}")

# Accessing Tuple Elements
print("\n" + "=" * 50)
print("ACCESSING ELEMENTS:")
print("=" * 50)

colors = ("red", "green", "blue", "yellow", "purple")
print(f"Tuple: {colors}")

# Positive indexing
print(f"\nFirst element [0]: {colors[0]}")
print(f"Second element [1]: {colors[1]}")
print(f"Third element [2]: {colors[2]}")

# Negative indexing
print(f"\nLast element [-1]: {colors[-1]}")
print(f"Second last [-2]: {colors[-2]}")
print(f"Third last [-3]: {colors[-3]}")

# Index visualization
print("\nIndex visualization:")
print("Positive: 0      1        2       3         4")
print(f"Tuple:    {colors}")
print("Negative: -5     -4       -3      -2        -1")

# Tuple Slicing
print("\n" + "=" * 50)
print("TUPLE SLICING:")
print("=" * 50)

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tuple: {numbers}")

# Basic slicing
print(f"\nnumbers[2:5]: {numbers[2:5]}")
print(f"numbers[0:3]: {numbers[0:3]}")
print(f"numbers[5:9]: {numbers[5:9]}")

# Omitting start or stop
print(f"\nnumbers[:5]: {numbers[:5]}")
print(f"numbers[5:]: {numbers[5:]}")
print(f"numbers[:]: {numbers[:]}")

# Negative indices
print(f"\nnumbers[-3:]: {numbers[-3:]}")
print(f"numbers[:-3]: {numbers[:-3]}")
print(f"numbers[-5:-2]: {numbers[-5:-2]}")

# Slicing with step
print(f"\nnumbers[::2]: {numbers[::2]}")
print(f"numbers[1::2]: {numbers[1::2]}")
print(f"numbers[::3]: {numbers[::3]}")
print(f"numbers[::-1]: {numbers[::-1]}")  # Reverse

# Tuple Immutability
print("\n" + "=" * 50)
print("IMMUTABILITY - Cannot Change Tuples:")
print("=" * 50)

coordinates = (10, 20, 30)
print(f"Original tuple: {coordinates}")

# This will cause an error!
try:
    coordinates[0] = 100
except TypeError as e:
    print(f"\n❌ Error trying to modify: {e}")

# Cannot append
try:
    coordinates.append(40)
except AttributeError as e:
    print(f"❌ Error trying to append: {e}")

# Cannot remove
try:
    coordinates.remove(20)
except AttributeError as e:
    print(f"❌ Error trying to remove: {e}")

# Cannot sort in place
try:
    coordinates.sort()
except AttributeError as e:
    print(f"❌ Error trying to sort: {e}")

print("\n✓ Tuples are immutable - this protects your data!")

# Workarounds if you need to "modify"
print("\n--- Workarounds for Modification ---")

original = (1, 2, 3, 4, 5)
print(f"Original: {original}")

# Convert to list, modify, convert back
temp_list = list(original)
temp_list[0] = 100
temp_list.append(6)
modified = tuple(temp_list)
print(f"'Modified' tuple: {modified}")

# Create new tuple with concatenation
original = (1, 2, 3)
new_tuple = original + (4, 5)
print(f"\nOriginal: {original}")
print(f"New tuple: {new_tuple}")

# Tuple with Mutable Objects
print("\n" + "=" * 50)
print("TUPLES WITH MUTABLE OBJECTS:")
print("=" * 50)

# Tuple containing a list
data = (1, 2, [3, 4, 5])
print(f"Original: {data}")

# Can't change tuple itself
try:
    data[0] = 100
except TypeError as e:
    print(f"❌ Can't change tuple: {e}")

# But CAN modify the list inside!
data[2].append(6)
print(f"After modifying list inside: {data}")

data[2][0] = 999
print(f"After changing list element: {data}")

print("\n⚠️  Tuple is immutable, but objects inside can be mutable!")

# Tuple Length
print("\n" + "=" * 50)
print("TUPLE LENGTH:")
print("=" * 50)

fruits = ("apple", "banana", "orange")
print(f"Tuple: {fruits}")
print(f"Length: {len(fruits)}")

empty = ()
print(f"\nEmpty tuple: {empty}")
print(f"Length: {len(empty)}")

single = (42,)
print(f"\nSingle element: {single}")
print(f"Length: {len(single)}")

# Tuple Membership
print("\n" + "=" * 50)
print("TUPLE MEMBERSHIP:")
print("=" * 50)

fruits = ("apple", "banana", "orange", "grape")
print(f"Tuple: {fruits}")

print(f"\n'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")
print(f"'kiwi' not in fruits: {'kiwi' not in fruits}")

# Tuple Concatenation
print("\n" + "=" * 50)
print("TUPLE CONCATENATION:")
print("=" * 50)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2
print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"combined: {combined}")

# Original tuples unchanged
print(f"\ntuple1 still: {tuple1}")
print(f"tuple2 still: {tuple2}")

# Can concatenate multiple tuples
result = (1, 2) + (3, 4) + (5, 6)
print(f"\n(1,2) + (3,4) + (5,6) = {result}")

# Tuple Repetition
print("\n" + "=" * 50)
print("TUPLE REPETITION:")
print("=" * 50)

zeros = (0,) * 5
print(f"(0,) * 5 = {zeros}")

pattern = (1, 2) * 3
print(f"(1, 2) * 3 = {pattern}")

chars = ('x',) * 10
print(f"('x',) * 10 = {chars}")

# Tuple Methods
print("\n" + "=" * 50)
print("TUPLE METHODS:")
print("=" * 50)

# Tuples have only 2 methods!

# count() - Count occurrences
numbers = (1, 2, 3, 2, 4, 2, 5, 2)
print(f"Tuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Count of 3: {numbers.count(3)}")
print(f"Count of 6: {numbers.count(6)}")  # Returns 0

# index() - Find position
fruits = ("apple", "banana", "orange", "grape", "banana")
print(f"\nTuple: {fruits}")
print(f"Index of 'orange': {fruits.index('orange')}")
print(f"Index of 'banana': {fruits.index('banana')}")  # First occurrence

# index() with start and end
numbers = (1, 2, 3, 4, 2, 5, 2, 6)
print(f"\nNumbers: {numbers}")
first_2 = numbers.index(2)
print(f"First 2 at index: {first_2}")
second_2 = numbers.index(2, first_2 + 1)
print(f"Second 2 at index: {second_2}")

# Tuple Comparison
print("\n" + "=" * 50)
print("TUPLE COMPARISON:")
print("=" * 50)

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)

print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"tuple3: {tuple3}")

print(f"\ntuple1 == tuple2: {tuple1 == tuple2}")
print(f"tuple1 == tuple3: {tuple1 == tuple3}")
print(f"tuple1 < tuple3: {tuple1 < tuple3}")  # Lexicographic comparison

# Tuple Unpacking
print("\n" + "=" * 50)
print("TUPLE UNPACKING:")
print("=" * 50)

# Basic unpacking
point = (10, 20)
x, y = point
print(f"point: {point}")
print(f"x = {x}, y = {y}")

# Unpacking with more elements
rgb = (255, 128, 0)
r, g, b = rgb
print(f"\nrgb: {rgb}")
print(f"r = {r}, g = {g}, b = {b}")

# Unpacking with * (rest)
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(f"\nnumbers: {numbers}")
print(f"first: {first}")
print(f"middle: {middle}")  # This becomes a list!
print(f"last: {last}")

first, second, *rest = numbers
print(f"\nfirst: {first}, second: {second}, rest: {rest}")

# Swapping variables
a = 10
b = 20
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a  # Tuple unpacking magic!
print(f"After swap:  a = {a}, b = {b}")

# Multiple return values
def get_user_info():
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city  # Returns a tuple

name, age, city = get_user_info()
print(f"\nUser: {name}, Age: {age}, City: {city}")

# Tuple Packing
print("\n" + "=" * 50)
print("TUPLE PACKING:")
print("=" * 50)

# Automatic tuple creation
coordinates = 10, 20, 30  # No parentheses needed
print(f"coordinates: {coordinates}")
print(f"Type: {type(coordinates)}")

# Useful in return statements
def get_min_max(numbers):
    return min(numbers), max(numbers)  # Returns tuple

result = get_min_max([1, 5, 3, 9, 2])
print(f"\nMin-Max result: {result}")
print(f"Type: {type(result)}")

# Unpack immediately
minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")

# Nested Tuples
print("\n" + "=" * 50)
print("NESTED TUPLES:")
print("=" * 50)

# Tuple of tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matrix:")
for row in matrix:
    print(row)

# Accessing nested elements
print(f"\nFirst row: {matrix[0]}")
print(f"Element [0][0]: {matrix[0][0]}")
print(f"Element [1][2]: {matrix[1][2]}")
print(f"Element [2][1]: {matrix[2][1]}")

# Complex nested structure
students = (
    ("Alice", 20, (85, 90, 88)),
    ("Bob", 21, (78, 82, 80)),
    ("Charlie", 19, (92, 95, 90))
)

print("\nStudent data:")
for student in students:
    name, age, scores = student
    print(f"{name}, age {age}, scores: {scores}")

# Min, Max, Sum
print("\n" + "=" * 50)
print("MIN, MAX, SUM:")
print("=" * 50)

numbers = (45, 23, 67, 12, 89, 34, 56)
print(f"Numbers: {numbers}")

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# Sorted and Reversed
print("\n" + "=" * 50)
print("SORTED AND REVERSED:")
print("=" * 50)

numbers = (3, 1, 4, 1, 5, 9, 2, 6)
print(f"Original: {numbers}")

# sorted() returns a list
sorted_list = sorted(numbers)
print(f"Sorted (list): {sorted_list}")

# Convert back to tuple if needed
sorted_tuple = tuple(sorted(numbers))
print(f"Sorted (tuple): {sorted_tuple}")

# reversed() returns an iterator
reversed_tuple = tuple(reversed(numbers))
print(f"Reversed: {reversed_tuple}")

# Tuple Iteration
print("\n" + "=" * 50)
print("TUPLE ITERATION:")
print("=" * 50)

fruits = ("apple", "banana", "orange", "grape")

print("Method 1: Direct iteration")
for fruit in fruits:
    print(f"  {fruit}")

print("\nMethod 2: With index")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

print("\nMethod 3: With enumerate")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Tuples vs Lists
print("\n" + "=" * 50)
print("TUPLES vs LISTS:")
print("=" * 50)

print("LISTS:")
print("  ✓ Mutable (can change)")
print("  ✓ Methods: append, insert, remove, sort, etc.")
print("  ✓ Use when data needs to change")
print("  ✓ Slower than tuples")
print("  ✗ Cannot be dictionary keys")

print("\nTUPLES:")
print("  ✓ Immutable (cannot change)")
print("  ✓ Only 2 methods: count, index")
print("  ✓ Use for fixed data")
print("  ✓ Faster than lists")
print("  ✓ Can be dictionary keys")
print("  ✓ Safer - data is protected")

# Memory comparison
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"\nMemory size:")
print(f"List:  {sys.getsizeof(my_list)} bytes")
print(f"Tuple: {sys.getsizeof(my_tuple)} bytes")

# Tuples as Dictionary Keys
print("\n" + "=" * 50)
print("TUPLES AS DICTIONARY KEYS:")
print("=" * 50)

# Tuples can be dictionary keys (lists cannot!)
coordinates = {
    (0, 0): "Origin",
    (1, 0): "Right",
    (0, 1): "Up",
    (-1, 0): "Left",
    (0, -1): "Down"
}

print("Coordinate map:")
for coord, direction in coordinates.items():
    print(f"  {coord}: {direction}")

print(f"\nPoint (1, 0): {coordinates[(1, 0)]}")

# This would cause an error with lists:
# wrong = {[0, 0]: "Origin"}  # TypeError!

# Real-world Example: RGB Colors
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: RGB COLORS")
print("=" * 50)

# RGB colors as tuples (immutable)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

print(f"RED: {RED}")
print(f"GREEN: {GREEN}")
print(f"BLUE: {BLUE}")

# Unpack color
r, g, b = RED
print(f"\nRed color - R: {r}, G: {g}, B: {b}")

# Store in dictionary
colors = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
    "white": WHITE,
    "black": BLACK
}

print("\nColor palette:")
for name, rgb in colors.items():
    print(f"  {name}: {rgb}")

# Real-world Example: Database Records
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: DATABASE RECORDS")
print("=" * 50)

# Tuples for read-only database records
records = (
    (1, "Alice", "alice@email.com", 25),
    (2, "Bob", "bob@email.com", 30),
    (3, "Charlie", "charlie@email.com", 28),
    (4, "Diana", "diana@email.com", 22)
)

print(f"{'ID':<5} {'Name':<10} {'Email':<20} {'Age':<5}")
print("-" * 45)
for record in records:
    id, name, email, age = record
    print(f"{id:<5} {name:<10} {email:<20} {age:<5}")

# Access specific record
user = records[1]
print(f"\nUser at index 1: {user}")
user_id, name, email, age = user
print(f"Name: {name}, Email: {email}")

# Real-world Example: Coordinates
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: GPS COORDINATES")
print("=" * 50)

# GPS coordinates as tuples
locations = {
    "home": (40.7128, -74.0060),      # New York
    "work": (34.0522, -118.2437),     # Los Angeles
    "vacation": (48.8566, 2.3522)     # Paris
}

print("Saved locations:")
for name, coords in locations.items():
    lat, lon = coords
    print(f"  {name}: {lat}°N, {lon}°W")

# Calculate distance between two points
def calculate_distance(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2
    # Simplified distance calculation
    return ((lat2 - lat1)**2 + (lon2 - lon1)**2)**0.5

home = locations["home"]
work = locations["work"]
distance = calculate_distance(home, work)
print(f"\nDistance home to work: {distance:.2f} units")

# Real-world Example: Function Arguments
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: FUNCTION WITH TUPLE RETURN")
print("=" * 50)

def analyze_scores(scores):
    """Analyze test scores and return statistics as tuple"""
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    return minimum, maximum, average  # Returns tuple

test_scores = [85, 92, 78, 95, 88, 73, 90]
min_score, max_score, avg_score = analyze_scores(test_scores)

print(f"Test Scores: {test_scores}")
print(f"Minimum: {min_score}")
print(f"Maximum: {max_score}")
print(f"Average: {avg_score:.2f}")

# Real-world Example: Date and Time
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: DATE REPRESENTATION")
print("=" * 50)

# Dates as tuples (immutable)
birthday = (1995, 6, 15)  # Year, Month, Day
year, month, day = birthday

print(f"Birthday: {birthday}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Formatted: {day:02d}/{month:02d}/{year}")

# Multiple dates
important_dates = (
    (1995, 6, 15),
    (2000, 12, 31),
    (2024, 1, 1)
)

print("\nImportant dates:")
for date in important_dates:
    y, m, d = date
    print(f"  {d:02d}/{m:02d}/{y}")

# Common Patterns
print("\n" + "=" * 50)
print("COMMON PATTERNS:")
print("=" * 50)

# Return multiple values
def get_stats(numbers):
    return len(numbers), sum(numbers), sum(numbers) / len(numbers)

count, total, avg = get_stats([1, 2, 3, 4, 5])
print(f"Count: {count}, Total: {total}, Average: {avg}")

# Swap multiple variables
a, b, c = 1, 2, 3
print(f"\nBefore: a={a}, b={b}, c={c}")
a, b, c = c, a, b  # Rotate values
print(f"After:  a={a}, b={b}, c={c}")

# Named tuple (better readability)
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(f"\nNamed tuple: {p}")
print(f"Access by name: x={p.x}, y={p.y}")
print(f"Access by index: x={p[0]}, y={p[1]}")

# Convert between tuple and list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
back_to_tuple = tuple(my_list)

print(f"\nTuple: {my_tuple}")
print(f"To List: {my_list}")
print(f"Back to Tuple: {back_to_tuple}")

# Practice Exercises
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a tuple of your favorite books")
print("2. Access first and last book using indexing")
print("3. Try to modify the tuple (observe the error)")
print("4. Create a tuple of coordinates and unpack them")
print("5. Write a function that returns mult=")