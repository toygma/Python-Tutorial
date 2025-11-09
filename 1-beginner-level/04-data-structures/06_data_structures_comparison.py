"""
DATA STRUCTURES COMPARISON
==========================

This file compares Python's four main data structures: Lists, Tuples, Sets,
and Dictionaries. Understanding their differences helps you choose the right
tool for each task.

Comparison Points:
- Syntax and creation
- Mutability (changeable or not)
- Order (maintained or not)
- Duplicates (allowed or not)
- Access methods
- Performance characteristics
- Use cases
- When to use which one
"""

# Quick Overview Table
print("DATA STRUCTURES QUICK REFERENCE:")
print("=" * 80)
print(f"{'Feature':<20} {'List':<15} {'Tuple':<15} {'Set':<15} {'Dictionary':<15}")
print("-" * 80)
print(f"{'Syntax':<20} {'[1,2,3]':<15} {'(1,2,3)':<15} {'{1,2,3}':<15} {'{k:v}':<15}")
print(f"{'Ordered':<20} {'Yes':<15} {'Yes':<15} {'No':<15} {'No*':<15}")
print(f"{'Mutable':<20} {'Yes':<15} {'No':<15} {'Yes':<15} {'Yes':<15}")
print(f"{'Duplicates':<20} {'Yes':<15} {'Yes':<15} {'No':<15} {'Keys: No':<15}")
print(f"{'Indexing':<20} {'Yes':<15} {'Yes':<15} {'No':<15} {'By key':<15}")
print(f"{'Use Case':<20} {'General':<15} {'Fixed data':<15} {'Unique items':<15} {'Key-value':<15}")
print("=" * 80)
print("* Dictionaries preserve insertion order (Python 3.7+)\n")

# Side-by-Side Creation
print("CREATING DATA STRUCTURES:")
print("=" * 80)

# Lists - Mutable, ordered, allows duplicates
my_list = [1, 2, 3, 2, 1]
print(f"List:       {my_list}")
print(f"  Type:     {type(my_list)}")
print(f"  Ordered:  Yes")
print(f"  Mutable:  Yes")
print(f"  Allows duplicates: Yes")

# Tuples - Immutable, ordered, allows duplicates
my_tuple = (1, 2, 3, 2, 1)
print(f"\nTuple:      {my_tuple}")
print(f"  Type:     {type(my_tuple)}")
print(f"  Ordered:  Yes")
print(f"  Mutable:  No")
print(f"  Allows duplicates: Yes")

# Sets - Mutable, unordered, no duplicates
my_set = {1, 2, 3, 2, 1}  # Duplicates automatically removed
print(f"\nSet:        {my_set}")
print(f"  Type:     {type(my_set)}")
print(f"  Ordered:  No")
print(f"  Mutable:  Yes")
print(f"  Allows duplicates: No")

# Dictionaries - Mutable, ordered (3.7+), keys must be unique
my_dict = {"a": 1, "b": 2, "c": 3}
print(f"\nDictionary: {my_dict}")
print(f"  Type:     {type(my_dict)}")
print(f"  Ordered:  Yes (insertion order)")
print(f"  Mutable:  Yes")
print(f"  Keys unique: Yes")

# Mutability Comparison
print("\n" + "=" * 80)
print("MUTABILITY (Can it be changed?):")
print("=" * 80)

# List - Mutable
print("LIST - Mutable (can be changed):")
my_list = [1, 2, 3]
print(f"  Original: {my_list}")
my_list[0] = 999
print(f"  Modified: {my_list}")
my_list.append(4)
print(f"  Appended: {my_list}")

# Tuple - Immutable
print("\nTUPLE - Immutable (cannot be changed):")
my_tuple = (1, 2, 3)
print(f"  Original: {my_tuple}")
try:
    my_tuple[0] = 999
except TypeError as e:
    print(f"  Error: {e}")

# Set - Mutable
print("\nSET - Mutable (can be changed):")
my_set = {1, 2, 3}
print(f"  Original: {my_set}")
my_set.add(4)
print(f"  After add: {my_set}")
my_set.remove(1)
print(f"  After remove: {my_set}")

# Dictionary - Mutable
print("\nDICTIONARY - Mutable (can be changed):")
my_dict = {"a": 1, "b": 2}
print(f"  Original: {my_dict}")
my_dict["c"] = 3
print(f"  After add: {my_dict}")
my_dict["a"] = 999
print(f"  After update: {my_dict}")

# Ordering Comparison
print("\n" + "=" * 80)
print("ORDERING (Is position maintained?):")
print("=" * 80)

# List - Ordered
print("LIST - Ordered:")
list1 = [3, 1, 4, 1, 5]
print(f"  Created: {list1}")
print(f"  First element [0]: {list1[0]}")
print(f"  Last element [-1]: {list1[-1]}")
print(f"  Slice [1:3]: {list1[1:3]}")

# Tuple - Ordered
print("\nTUPLE - Ordered:")
tuple1 = (3, 1, 4, 1, 5)
print(f"  Created: {tuple1}")
print(f"  First element [0]: {tuple1[0]}")
print(f"  Last element [-1]: {tuple1[-1]}")
print(f"  Slice [1:3]: {tuple1[1:3]}")

# Set - Unordered
print("\nSET - Unordered:")
set1 = {3, 1, 4, 5, 9}
print(f"  Created: {set1}")
print(f"  Cannot use indexing!")
try:
    print(set1[0])
except TypeError as e:
    print(f"  Error: {e}")

# Dictionary - Ordered (insertion order, Python 3.7+)
print("\nDICTIONARY - Ordered (insertion order):")
dict1 = {"c": 3, "a": 1, "b": 2}
print(f"  Created: {dict1}")
print(f"  Access by key ['a']: {dict1['a']}")
print(f"  Keys maintain insertion order")

# Duplicates Comparison
print("\n" + "=" * 80)
print("DUPLICATES (Are duplicates allowed?):")
print("=" * 80)

# List - Allows duplicates
print("LIST - Allows duplicates:")
my_list = [1, 2, 2, 3, 3, 3]
print(f"  {my_list}")
print(f"  Count of 3: {my_list.count(3)}")

# Tuple - Allows duplicates
print("\nTUPLE - Allows duplicates:")
my_tuple = (1, 2, 2, 3, 3, 3)
print(f"  {my_tuple}")
print(f"  Count of 3: {my_tuple.count(3)}")

# Set - No duplicates
print("\nSET - No duplicates (automatically removed):")
my_set = {1, 2, 2, 3, 3, 3}
print(f"  Input: {{1, 2, 2, 3, 3, 3}}")
print(f"  Actual: {my_set}")

# Dictionary - Keys must be unique
print("\nDICTIONARY - Keys must be unique (last value wins):")
my_dict = {"a": 1, "b": 2, "a": 3}
print(f"  Input: {{'a': 1, 'b': 2, 'a': 3}}")
print(f"  Actual: {my_dict}")

# Access Methods Comparison
print("\n" + "=" * 80)
print("ACCESS METHODS:")
print("=" * 80)

# List - Index access
print("LIST - Access by index:")
my_list = ["a", "b", "c", "d"]
print(f"  List: {my_list}")
print(f"  my_list[0]: {my_list[0]}")
print(f"  my_list[-1]: {my_list[-1]}")
print(f"  my_list[1:3]: {my_list[1:3]}")

# Tuple - Index access
print("\nTUPLE - Access by index:")
my_tuple = ("a", "b", "c", "d")
print(f"  Tuple: {my_tuple}")
print(f"  my_tuple[0]: {my_tuple[0]}")
print(f"  my_tuple[-1]: {my_tuple[-1]}")
print(f"  my_tuple[1:3]: {my_tuple[1:3]}")

# Set - No index access (iterate or check membership)
print("\nSET - No index access (iterate or membership):")
my_set = {"a", "b", "c", "d"}
print(f"  Set: {my_set}")
print(f"  'a' in my_set: {'a' in my_set}")
print(f"  'z' in my_set: {'z' in my_set}")
print(f"  Iterate: {list(my_set)}")

# Dictionary - Access by key
print("\nDICTIONARY - Access by key:")
my_dict = {"name": "Alice", "age": 25, "city": "Paris"}
print(f"  Dict: {my_dict}")
print(f"  my_dict['name']: {my_dict['name']}")
print(f"  my_dict.get('age'): {my_dict.get('age')}")
print(f"  my_dict.get('country', 'N/A'): {my_dict.get('country', 'N/A')}")

# Performance Comparison
print("\n" + "=" * 80)
print("PERFORMANCE CHARACTERISTICS:")
print("=" * 80)

import time

# Create large collections
size = 100000
test_list = list(range(size))
test_tuple = tuple(range(size))
test_set = set(range(size))
test_dict = {i: i for i in range(size)}

# Search for last element
search_value = size - 1

# List search
start = time.time()
search_value in test_list
list_time = time.time() - start

# Tuple search
start = time.time()
search_value in test_tuple
tuple_time = time.time() - start

# Set search
start = time.time()
search_value in test_set
set_time = time.time() - start

# Dict search
start = time.time()
search_value in test_dict
dict_time = time.time() - start

print(f"Membership test for {size:,} elements:")
print(f"  List:       {list_time:.6f} seconds")
print(f"  Tuple:      {tuple_time:.6f} seconds")
print(f"  Set:        {set_time:.6f} seconds  ⚡ FASTEST")
print(f"  Dictionary: {dict_time:.6f} seconds  ⚡ FASTEST")

print(f"\n💡 Sets and Dictionaries use hash tables = O(1) lookup")
print(f"💡 Lists and Tuples scan sequentially = O(n) lookup")

# Memory Comparison
print("\n" + "=" * 80)
print("MEMORY USAGE:")
print("=" * 80)

import sys

# Small collections
data = [1, 2, 3, 4, 5]

list_size = sys.getsizeof(data)
tuple_size = sys.getsizeof(tuple(data))
set_size = sys.getsizeof(set(data))
dict_size = sys.getsizeof({i: i for i in data})

print(f"Memory for 5 elements:")
print(f"  List:       {list_size} bytes")
print(f"  Tuple:      {tuple_size} bytes  ⚡ SMALLEST")
print(f"  Set:        {set_size} bytes")
print(f"  Dictionary: {dict_size} bytes")

print(f"\n💡 Tuples are more memory efficient")
print(f"💡 Dictionaries use most memory (store keys + values)")

# When to Use Each Structure
print("\n" + "=" * 80)
print("WHEN TO USE EACH STRUCTURE:")
print("=" * 80)

print("📋 USE LIST WHEN:")
print("  ✓ You need an ordered collection")
print("  ✓ Items need to be changed/modified")
print("  ✓ Duplicates are meaningful")
print("  ✓ You need to access by index/position")
print("  ✓ Example: Shopping list, todo list, test scores")

print("\n📦 USE TUPLE WHEN:")
print("  ✓ Data should not be modified (immutable)")
print("  ✓ You need a fixed set of values")
print("  ✓ Want to use as dictionary key")
print("  ✓ Need better performance than list")
print("  ✓ Example: Coordinates (x,y), RGB colors, database records")

print("\n🎯 USE SET WHEN:")
print("  ✓ You only care about unique items")
print("  ✓ Order doesn't matter")
print("  ✓ Need fast membership testing")
print("  ✓ Performing set operations (union, intersection)")
print("  ✓ Example: Unique tags, unique visitors, removing duplicates")

print("\n📖 USE DICTIONARY WHEN:")
print("  ✓ You need key-value pairs")
print("  ✓ Fast lookup by key is important")
print("  ✓ Data has named fields")
print("  ✓ Creating mappings or associations")
print("  ✓ Example: User profiles, config settings, word counts, database")

# Conversion Between Structures
print("\n" + "=" * 80)
print("CONVERTING BETWEEN STRUCTURES:")
print("=" * 80)

# Starting data
original_list = [1, 2, 3, 2, 1]
print(f"Original list: {original_list}")

# List to others
to_tuple = tuple(original_list)
to_set = set(original_list)  # Removes duplicates
to_dict = {i: i**2 for i in original_list}

print(f"\nConversions from list:")
print(f"  to tuple: {to_tuple}")
print(f"  to set: {to_set}")
print(f"  to dict: {to_dict}")

# Tuple to others
original_tuple = (1, 2, 3, 2, 1)
print(f"\nOriginal tuple: {original_tuple}")

to_list = list(original_tuple)
to_set = set(original_tuple)

print(f"Conversions from tuple:")
print(f"  to list: {to_list}")
print(f"  to set: {to_set}")

# Set to others
original_set = {1, 2, 3, 4, 5}
print(f"\nOriginal set: {original_set}")

to_list = list(original_set)
to_tuple = tuple(original_set)

print(f"Conversions from set:")
print(f"  to list: {to_list}")
print(f"  to tuple: {to_tuple}")

# Dictionary conversions
original_dict = {"a": 1, "b": 2, "c": 3}
print(f"\nOriginal dict: {original_dict}")

keys_list = list(original_dict.keys())
values_list = list(original_dict.values())
items_list = list(original_dict.items())

print(f"Conversions from dict:")
print(f"  keys to list: {keys_list}")
print(f"  values to list: {values_list}")
print(f"  items to list: {items_list}")

# Real-World Scenario Comparison
print("\n" + "=" * 80)
print("REAL-WORLD SCENARIO: STUDENT GRADES")
print("=" * 80)

print("🎯 Scenario: Managing student test scores\n")

# Using List - Good for ordered scores with duplicates
print("LIST - When scores can repeat and order matters:")
test_scores = [85, 92, 78, 92, 85, 95]
print(f"  Scores: {test_scores}")
print(f"  Average: {sum(test_scores) / len(test_scores):.2f}")
print(f"  Highest: {max(test_scores)}")
print(f"  First score: {test_scores[0]}")

# Using Tuple - Good for fixed record
print("\nTUPLE - When score record should not change:")
final_grades = (85, 92, 78, 95)
print(f"  Final grades: {final_grades}")
print(f"  Cannot be modified (immutable)")
print(f"  Can be used as dict key")

# Using Set - Good for unique scores
print("\nSET - When you only care about unique scores:")
unique_scores = {85, 92, 78, 92, 85, 95}
print(f"  Unique scores: {unique_scores}")
print(f"  Number of different scores: {len(unique_scores)}")

# Using Dictionary - Good for student-score mapping
print("\nDICTIONARY - When you need student-to-score mapping:")
student_scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95
}
print(f"  Scores: {student_scores}")
print(f"  Alice's score: {student_scores['Alice']}")
print(f"  All students: {list(student_scores.keys())}")

# Common Operations Comparison
print("\n" + "=" * 80)
print("COMMON OPERATIONS:")
print("=" * 80)

# Adding elements
print("ADDING ELEMENTS:")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

print(f"  List:   {my_list} → append(4) → ", end="")
my_list.append(4)
print(my_list)

print(f"  Tuple:  {my_tuple} → Cannot add (immutable)")

print(f"  Set:    {my_set} → add(4) → ", end="")
my_set.add(4)
print(my_set)

print(f"  Dict:   {my_dict} → ['c'] = 3 → ", end="")
my_dict['c'] = 3
print(my_dict)

# Removing elements
print("\nREMOVING ELEMENTS:")
my_list = [1, 2, 3, 4]
my_set = {1, 2, 3, 4}
my_dict = {"a": 1, "b": 2, "c": 3}

print(f"  List:   {my_list} → remove(2) → ", end="")
my_list.remove(2)
print(my_list)

print(f"  Tuple:  Cannot remove (immutable)")

print(f"  Set:    {my_set} → remove(2) → ", end="")
my_set.remove(2)
print(my_set)

print(f"  Dict:   {my_dict} → del ['b'] → ", end="")
del my_dict['b']
print(my_dict)

# Checking membership
print("\nCHECKING MEMBERSHIP:")
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {"a": 1, "b": 2, "c": 3}

print(f"  List:   3 in {my_list} = {3 in my_list}")
print(f"  Tuple:  3 in {my_tuple} = {3 in my_tuple}")
print(f"  Set:    3 in {my_set} = {3 in my_set}")
print(f"  Dict:   'b' in {my_dict} = {'b' in my_dict}")

# Practical Decision Tree
print("\n" + "=" * 80)
print("DECISION TREE - WHICH ONE TO USE?")
print("=" * 80)

print("""
START: What do you need?
│
├─ Need key-value pairs?
│  └─ YES → Use DICTIONARY 📖
│
├─ Need unique items only?
│  └─ YES → Use SET 🎯
│
├─ Need to modify items?
│  ├─ YES → Use LIST 📋
│  └─ NO → Use TUPLE 📦
│
└─ Need specific order?
   ├─ YES → Use LIST 📋 or TUPLE 📦
   └─ NO → Use SET 🎯
""")

# Summary Table
print("\n" + "=" * 80)
print("SUMMARY - CHOOSE YOUR WEAPON:")
print("=" * 80)

print("""
╔════════════╦═══════════╦════════════╦═══════════╦═════════════╗
║  Feature   ║   List    ║   Tuple    ║    Set    ║ Dictionary  ║
╠════════════╬═══════════╬════════════╬═══════════╬═════════════╣
║ Ordered    ║    ✓      ║     ✓      ║     ✗     ║  ✓ (3.7+)   ║
║ Mutable    ║    ✓      ║     ✗      ║     ✓     ║     ✓       ║
║ Duplicates ║    ✓      ║     ✓      ║     ✗     ║  Keys: ✗    ║
║ Indexing   ║    ✓      ║     ✓      ║     ✗     ║  By key     ║
║ Speed      ║  O(n)     ║   O(n)     ║   O(1)    ║   O(1)      ║
║ Memory     ║  Medium   ║   Small    ║  Medium   ║   Large     ║
╚════════════╩═══════════╩════════════╩═══════════╩═════════════╝

💡 Quick Tips:
  • Default choice: List 📋
  • Need immutable: Tuple 📦
  • Need unique: Set 🎯
  • Need lookups: Dictionary 📖
""")

# Practice Exercises
print("\n" + "=" * 80)
print("--- EXERCISES ---")
print("1. Convert a list with duplicates to a set, then back to a sorted list")
print("2. Create a tuple of coordinates and try to modify it")
print("3. Compare performance of 'in' operator for list vs set")
print("4. Build a dictionary from two lists (keys and values)")
print("5. Store student data - which structure for name vs grades?")
print("6. Implement a shopping cart - list, set, or dict?")
print("7. Remove duplicates from a list without changing order")
print("8. When would you choose tuple over list? Give 3 examples")
print("=" * 80)