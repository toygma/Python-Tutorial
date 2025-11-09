"""
LIST METHODS
============

Lists have many built-in methods that allow you to modify and work with them.
This file covers all important list methods with practical examples.

Key Methods:
- append()    - Add item to end
- insert()    - Add item at specific position
- extend()    - Add multiple items
- remove()    - Remove specific item
- pop()       - Remove and return item
- clear()     - Remove all items
- index()     - Find position of item
- count()     - Count occurrences
- sort()      - Sort list in place
- reverse()   - Reverse list in place
- copy()      - Create shallow copy
"""

# append() - Add item to end of list
print("APPEND() - Add to End:")
print("=" * 50)

fruits = ["apple", "banana", "orange"]
print(f"Original: {fruits}")

fruits.append("grape")
print(f"After append('grape'): {fruits}")

fruits.append("mango")
print(f"After append('mango'): {fruits}")

# Append different types
numbers = [1, 2, 3]
numbers.append(4)
numbers.append(5)
print(f"\nNumbers: {numbers}")

# Can append any type
mixed = [1, "hello"]
mixed.append(3.14)
mixed.append(True)
mixed.append([1, 2, 3])  # Can even append a list!
print(f"Mixed: {mixed}")

# insert() - Add item at specific position
print("\n" + "=" * 50)
print("INSERT() - Add at Specific Position:")
print("=" * 50)

colors = ["red", "green", "blue"]
print(f"Original: {colors}")

colors.insert(1, "yellow")  # Insert at index 1
print(f"After insert(1, 'yellow'): {colors}")

colors.insert(0, "purple")  # Insert at beginning
print(f"After insert(0, 'purple'): {colors}")

colors.insert(len(colors), "orange")  # Insert at end (like append)
print(f"After insert(len(colors), 'orange'): {colors}")

# Negative indices work too
numbers = [1, 2, 3, 4, 5]
numbers.insert(-1, 99)  # Insert before last element
print(f"\nNumbers after insert(-1, 99): {numbers}")

# extend() - Add multiple items from iterable
print("\n" + "=" * 50)
print("EXTEND() - Add Multiple Items:")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"list1: {list1}")
print(f"list2: {list2}")

list1.extend(list2)
print(f"After list1.extend(list2): {list1}")
print(f"list2 unchanged: {list2}")

# Extend with different iterables
letters = ['a', 'b', 'c']
print(f"\nletters: {letters}")

letters.extend(['d', 'e'])
print(f"After extend(['d', 'e']): {letters}")

letters.extend("xyz")  # Can extend with string
print(f"After extend('xyz'): {letters}")

letters.extend(range(1, 4))  # Can extend with range
print(f"After extend(range(1, 4)): {letters}")

# Difference between append and extend
print("\n--- Append vs Extend ---")
list_a = [1, 2, 3]
list_a.append([4, 5])
print(f"append([4, 5]): {list_a}")  # Adds list as single element

list_b = [1, 2, 3]
list_b.extend([4, 5])
print(f"extend([4, 5]): {list_b}")  # Adds each element

# remove() - Remove first occurrence of value
print("\n" + "=" * 50)
print("REMOVE() - Remove Specific Item:")
print("=" * 50)

fruits = ["apple", "banana", "orange", "banana", "grape"]
print(f"Original: {fruits}")

fruits.remove("banana")  # Removes first "banana"
print(f"After remove('banana'): {fruits}")

fruits.remove("orange")
print(f"After remove('orange'): {fruits}")

# remove() only removes first occurrence
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"\nNumbers: {numbers}")
numbers.remove(2)
print(f"After remove(2): {numbers}")  # Only first 2 is removed

# ValueError if item not found
print("\n--- Handling remove() errors ---")
colors = ["red", "green", "blue"]
print(f"colors: {colors}")

try:
    colors.remove("yellow")
except ValueError as e:
    print(f"Error: {e}")

# Safe remove
if "yellow" in colors:
    colors.remove("yellow")
else:
    print("'yellow' not in list, skipping remove")

# pop() - Remove and return item at index
print("\n" + "=" * 50)
print("POP() - Remove and Return Item:")
print("=" * 50)

stack = [1, 2, 3, 4, 5]
print(f"Original: {stack}")

last = stack.pop()  # Remove and return last item
print(f"Popped: {last}")
print(f"After pop(): {stack}")

last = stack.pop()
print(f"Popped: {last}")
print(f"After pop(): {stack}")

# Pop from specific index
numbers = [10, 20, 30, 40, 50]
print(f"\nNumbers: {numbers}")

first = numbers.pop(0)  # Remove first
print(f"Popped index 0: {first}")
print(f"After pop(0): {numbers}")

middle = numbers.pop(1)  # Remove at index 1
print(f"Popped index 1: {middle}")
print(f"After pop(1): {numbers}")

# Pop with negative index
last = numbers.pop(-1)  # Remove last
print(f"Popped index -1: {last}")
print(f"After pop(-1): {numbers}")

# Stack behavior (LIFO - Last In First Out)
print("\n--- Stack Example (LIFO) ---")
stack = []
print(f"Empty stack: {stack}")

stack.append(1)
stack.append(2)
stack.append(3)
print(f"After pushing 1, 2, 3: {stack}")

print(f"Pop: {stack.pop()}")  # 3
print(f"Pop: {stack.pop()}")  # 2
print(f"Stack now: {stack}")

# Queue behavior (FIFO - First In First Out)
print("\n--- Queue Example (FIFO) ---")
queue = []
print(f"Empty queue: {queue}")

queue.append(1)
queue.append(2)
queue.append(3)
print(f"After enqueuing 1, 2, 3: {queue}")

print(f"Dequeue: {queue.pop(0)}")  # 1
print(f"Dequeue: {queue.pop(0)}")  # 2
print(f"Queue now: {queue}")

# clear() - Remove all items
print("\n" + "=" * 50)
print("CLEAR() - Remove All Items:")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

numbers.clear()
print(f"After clear(): {numbers}")

# Alternative ways to clear
fruits = ["apple", "banana", "orange"]
fruits = []  # Creates new empty list
print(f"Using fruits = []: {fruits}")

colors = ["red", "green", "blue"]
del colors[:]  # Deletes all elements
print(f"Using del colors[:]: {colors}")

# index() - Find position of first occurrence
print("\n" + "=" * 50)
print("INDEX() - Find Item Position:")
print("=" * 50)

fruits = ["apple", "banana", "orange", "grape", "banana"]
print(f"List: {fruits}")

pos = fruits.index("orange")
print(f"Index of 'orange': {pos}")

pos = fruits.index("banana")  # Returns first occurrence
print(f"Index of 'banana': {pos}")

# index() with start and end
print("\n--- index() with range ---")
numbers = [1, 2, 3, 4, 2, 5, 2, 6]
print(f"Numbers: {numbers}")

first_2 = numbers.index(2)
print(f"First 2 at index: {first_2}")

second_2 = numbers.index(2, first_2 + 1)  # Start searching after first
print(f"Second 2 at index: {second_2}")

third_2 = numbers.index(2, second_2 + 1)  # Start after second
print(f"Third 2 at index: {third_2}")

# ValueError if not found
print("\n--- Handling index() errors ---")
colors = ["red", "green", "blue"]

try:
    pos = colors.index("yellow")
except ValueError as e:
    print(f"Error: {e}")

# Safe index check
if "yellow" in colors:
    pos = colors.index("yellow")
else:
    print("'yellow' not found in list")

# count() - Count occurrences of value
print("\n" + "=" * 50)
print("COUNT() - Count Occurrences:")
print("=" * 50)

numbers = [1, 2, 2, 3, 2, 4, 2, 5, 2]
print(f"List: {numbers}")

count_2 = numbers.count(2)
print(f"Count of 2: {count_2}")

count_3 = numbers.count(3)
print(f"Count of 3: {count_3}")

count_6 = numbers.count(6)  # Returns 0 if not found
print(f"Count of 6: {count_6}")

# Real example: Vote counting
print("\n--- Vote Counting Example ---")
votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Alice"]
print(f"Votes: {votes}")
print(f"Alice: {votes.count('Alice')} votes")
print(f"Bob: {votes.count('Bob')} votes")
print(f"Charlie: {votes.count('Charlie')} votes")

# sort() - Sort list in place
print("\n" + "=" * 50)
print("SORT() - Sort List In Place:")
print("=" * 50)

# Sort numbers ascending
numbers = [45, 12, 78, 23, 56, 34]
print(f"Original: {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

# Sort descending
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Sort strings
fruits = ["banana", "apple", "orange", "grape", "mango"]
print(f"\nOriginal: {fruits}")

fruits.sort()
print(f"After sort(): {fruits}")

fruits.sort(reverse=True)
print(f"After sort(reverse=True): {fruits}")

# Case-sensitive sorting
words = ["Banana", "apple", "Orange", "grape"]
print(f"\nOriginal: {words}")

words.sort()  # Uppercase comes before lowercase
print(f"After sort(): {words}")

words.sort(key=str.lower)  # Case-insensitive sort
print(f"After sort(key=str.lower): {words}")

# Sort by length
words = ["banana", "fig", "apple", "strawberry", "kiwi"]
print(f"\nOriginal: {words}")

words.sort(key=len)
print(f"After sort(key=len): {words}")

# Sort custom objects
print("\n--- Sorting with custom key ---")
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78],
    ["Diana", 95]
]
print("Original:")
for s in students:
    print(f"  {s}")

students.sort(key=lambda x: x[1])  # Sort by score
print("Sorted by score:")
for s in students:
    print(f"  {s}")

students.sort(key=lambda x: x[0])  # Sort by name
print("Sorted by name:")
for s in students:
    print(f"  {s}")

# Note: sort() returns None
numbers = [3, 1, 4, 1, 5]
result = numbers.sort()
print(f"\nnumbers.sort() returns: {result}")  # None
print(f"But numbers is now: {numbers}")

# sorted() creates new sorted list
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(f"\nOriginal: {numbers}")
print(f"Sorted copy: {sorted_numbers}")

# reverse() - Reverse list in place
print("\n" + "=" * 50)
print("REVERSE() - Reverse List In Place:")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

numbers.reverse()
print(f"After reverse(): {numbers}")

# Works with any type
fruits = ["apple", "banana", "orange", "grape"]
print(f"\nOriginal: {fruits}")

fruits.reverse()
print(f"After reverse(): {fruits}")

# Note: reverse() returns None
numbers = [1, 2, 3, 4, 5]
result = numbers.reverse()
print(f"\nnumbers.reverse() returns: {result}")  # None
print(f"But numbers is now: {numbers}")

# Alternative: slicing creates new reversed list
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(f"\nOriginal: {numbers}")
print(f"Reversed copy: {reversed_numbers}")

# copy() - Create shallow copy
print("\n" + "=" * 50)
print("COPY() - Create Shallow Copy:")
print("=" * 50)

original = [1, 2, 3, 4, 5]
print(f"Original: {original}")

copy = original.copy()
print(f"Copy: {copy}")

# Modify copy
copy[0] = 999
print(f"\nAfter copy[0] = 999:")
print(f"Original: {original}")  # Unchanged
print(f"Copy: {copy}")

# Shallow copy with nested lists
print("\n--- Shallow Copy with Nested Lists ---")
original = [[1, 2], [3, 4], [5, 6]]
copy = original.copy()

print(f"Original: {original}")
print(f"Copy: {copy}")

# Modify nested list
copy[0][0] = 999
print(f"\nAfter copy[0][0] = 999:")
print(f"Original: {original}")  # Also changed!
print(f"Copy: {copy}")

# Deep copy for nested structures
import copy as copy_module

original = [[1, 2], [3, 4], [5, 6]]
deep_copy = copy_module.deepcopy(original)

deep_copy[0][0] = 999
print(f"\nWith deep copy:")
print(f"Original: {original}")  # Unchanged
print(f"Deep copy: {deep_copy}")

# Method Chaining
print("\n" + "=" * 50)
print("METHOD CHAINING:")
print("=" * 50)

# Most list methods return None, so can't chain
# But can chain sorted(), reversed() functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# This creates new lists, doesn't modify original
result = sorted(numbers, reverse=True)
print(f"sorted(numbers, reverse=True): {result}")
print(f"Original unchanged: {numbers}")

# Real-world Example: Task Manager
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TASK MANAGER")
print("=" * 50)

tasks = []

# Add tasks
tasks.append("Buy groceries")
tasks.append("Finish homework")
tasks.append("Call dentist")
tasks.append("Clean room")

print("Current tasks:")
for i, task in enumerate(tasks, 1):
    print(f"  {i}. {task}")

# Complete a task
completed = tasks.pop(1)
print(f"\n✓ Completed: {completed}")

# Add urgent task at beginning
tasks.insert(0, "Prepare presentation")
print("\nUpdated tasks:")
for i, task in enumerate(tasks, 1):
    print(f"  {i}. {task}")

# Remove specific task
tasks.remove("Call dentist")
print(f"\nRemoved 'Call dentist'")

# Sort tasks alphabetically
tasks.sort()
print("\nSorted tasks:")
for i, task in enumerate(tasks, 1):
    print(f"  {i}. {task}")

print(f"\nTotal tasks: {len(tasks)}")

# Real-world Example: Shopping Cart
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SHOPPING CART")
print("=" * 50)

cart = []

# Add items
cart.extend(["Milk", "Bread", "Eggs"])
cart.append("Butter")
cart.append("Cheese")

print("Shopping Cart:")
for item in cart:
    print(f"  - {item}")

# Count items
print(f"\nTotal items: {len(cart)}")

# Check for item
if "Milk" in cart:
    print("✓ Milk is in cart")

# Remove item
cart.remove("Eggs")
print(f"\nRemoved Eggs from cart")

# Sort cart
cart.sort()
print("\nSorted cart:")
for item in cart:
    print(f"  - {item}")

# Clear cart
cart.clear()
print(f"\nCart after checkout: {cart}")

# Real-world Example: Playlist
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: MUSIC PLAYLIST")
print("=" * 50)

playlist = []

# Add songs
playlist.append("Bohemian Rhapsody")
playlist.append("Imagine")
playlist.append("Hotel California")
playlist.append("Stairway to Heaven")

print("🎵 My Playlist:")
for i, song in enumerate(playlist, 1):
    print(f"  {i}. {song}")

# Play (remove) first song
now_playing = playlist.pop(0)
print(f"\n▶ Now playing: {now_playing}")

# Add song to front
playlist.insert(0, "Sweet Child O' Mine")
print(f"⏭ Next up: {playlist[0]}")

# Shuffle (reverse as simple shuffle)
playlist.reverse()
print("\n🔀 Shuffled playlist:")
for i, song in enumerate(playlist, 1):
    print(f"  {i}. {song}")

print(f"\nTotal songs: {len(playlist)}")

# Real-world Example: High Scores
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: GAME HIGH SCORES")
print("=" * 50)

scores = [1500, 2300, 1800, 3200, 2100, 1900, 2800]

print(f"All scores: {scores}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {sum(scores) / len(scores):.2f}")

# Sort to find top 3
scores.sort(reverse=True)
print("\nTop 3 scores:")
for i, score in enumerate(scores[:3], 1):
    print(f"  {i}. {score}")

# Common Patterns
print("\n" + "=" * 50)
print("COMMON PATTERNS:")
print("=" * 50)

# Remove all occurrences of a value
numbers = [1, 2, 3, 2, 4, 2, 5, 2]
print(f"Original: {numbers}")

while 2 in numbers:
    numbers.remove(2)
print(f"After removing all 2s: {numbers}")

# Remove duplicates (preserve order)
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(f"\nOriginal: {numbers}")
print(f"Unique (ordered): {unique}")

# Remove duplicates (unordered, using set)
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique = list(set(numbers))
print(f"Unique (unordered): {unique}")

# Find and remove item by condition
numbers = [10, 25, 30, 45, 50, 15, 20]
print(f"\nOriginal: {numbers}")

# Remove first number greater than 40
for i, num in enumerate(numbers):
    if num > 40:
        numbers.pop(i)
        break
print(f"After removing first > 40: {numbers}")

# Practice Exercises
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a list and add 5 items using different methods")
print("2. Remove items using remove(), pop(), and del")
print("3. Sort a list of names alphabetically")
print("4. Count how many times a number appears in a list")
print("5. Reverse a list and compare with [::-1]")
print("6. Create a to-do list with add, complete, and sort features")
print("7. Build a simple inventory system (add, remove, search items)")
print("8. Implement a stack (push/pop) and queue (enqueue/dequeue)")
print("\n" + "=" * 50)