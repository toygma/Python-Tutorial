"""
SETS
====

Sets are unordered collections of unique elements. Sets automatically remove
duplicates and are optimized for membership testing and mathematical set
operations (union, intersection, difference).

Key Concepts:
- Creating sets
- Set operations (union, intersection, difference, symmetric difference)
- Set methods
- Set comprehensions
- Frozen sets (immutable sets)
- When to use sets

Why use sets?
- Automatic duplicate removal
- Fast membership testing
- Mathematical set operations
- Unordered collection when order doesn't matter
"""

# Creating Sets
print("CREATING SETS:")
print("=" * 50)

# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type: {type(empty_set)}")

# Note: {} creates an empty dictionary, not a set!
empty_dict = {}


# Set with values
numbers = {1, 2, 3, 4, 5}
print(f"\nNumbers: {numbers}")

# Set with mixed types
mixed = {1, "hello", 3.14, True}
print(f"Mixed types: {mixed}")

# Note: True and 1 are considered equal (also False and 0)
with_bool = {1, 2, True, 3, False, 0}
print(f"\nWith boolean: {with_bool}")  # Duplicates removed

# Set from string (each character becomes element)
char_set = set("hello")
print(f"\nFrom 'hello': {char_set}")  # Removes duplicate 'l'

# Set from list
from_list = set([1, 2, 3, 2, 4, 1, 5])
print(f"From list [1,2,3,2,4,1,5]: {from_list}")  # Duplicates removed

# Set from tuple
from_tuple = set((1, 2, 3, 4, 5))
print(f"From tuple: {from_tuple}")

# Set from range
from_range = set(range(1, 6))
print(f"From range(1,6): {from_range}")

# Sets Are Unordered
print("\n" + "=" * 50)
print("SETS ARE UNORDERED:")
print("=" * 50)

numbers = {5, 2, 8, 1, 9, 3}
print(f"Set: {numbers}")
print("Order may vary each time you run the program!")
print("Sets do NOT support indexing or slicing")

# Cannot access by index
try:
    print(numbers[0])
except TypeError as e:
    print(f"Error: {e}")

# Automatic Duplicate Removal
print("\n" + "=" * 50)
print("AUTOMATIC DUPLICATE REMOVAL:")
print("=" * 50)

# Duplicates in set literal
numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"Input: {{1, 2, 2, 3, 3, 3, 4, 4, 4, 4}}")
print(f"Actual set: {numbers}")

# Remove duplicates from list
fruits_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
print(f"\nList with duplicates: {fruits_list}")

unique_fruits = set(fruits_list)
print(f"As set: {unique_fruits}")

# Convert back to list if needed
unique_list = list(unique_fruits)
print(f"Back to list: {unique_list}")

# Set Length
print("\n" + "=" * 50)
print("SET LENGTH:")
print("=" * 50)

colors = {"red", "green", "blue", "yellow"}
print(f"Set: {colors}")
print(f"Length: {len(colors)}")

empty = set()
print(f"\nEmpty set: {empty}")
print(f"Length: {len(empty)}")

# Set Membership (Very Fast!)
print("\n" + "=" * 50)
print("SET MEMBERSHIP:")
print("=" * 50)

fruits = {"apple", "banana", "orange", "grape"}
print(f"Set: {fruits}")

print(f"\n'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")

# Membership is faster in sets than lists
import time

# Create large list and set
large_list = list(range(100000))
large_set = set(range(100000))

# Test membership in list
start = time.time()
99999 in large_list
list_time = time.time() - start

# Test membership in set
start = time.time()
99999 in large_set
set_time = time.time() - start

print(f"\nMembership test for 99999:")
print(f"List time: {list_time:.6f} seconds")
print(f"Set time: {set_time:.6f} seconds")
print(f"Set is ~{list_time/set_time:.0f}x faster!")

# Adding Elements
print("\n" + "=" * 50)
print("ADDING ELEMENTS:")
print("=" * 50)

# add() - Add single element
fruits = {"apple", "banana"}
print(f"Original: {fruits}")

fruits.add("orange")
print(f"After add('orange'): {fruits}")

fruits.add("grape")
print(f"After add('grape'): {fruits}")

# Adding duplicate has no effect
fruits.add("apple")
print(f"After add('apple') again: {fruits}")

# update() - Add multiple elements
numbers = {1, 2, 3}
print(f"\nOriginal: {numbers}")

numbers.update([4, 5, 6])
print(f"After update([4, 5, 6]): {numbers}")

numbers.update({7, 8}, [9, 10])
print(f"After update({{7,8}}, [9,10]): {numbers}")

# Can update with any iterable
letters = {'a', 'b'}
letters.update("cde")
print(f"\nAfter update('cde'): {letters}")

# Removing Elements
print("\n" + "=" * 50)
print("REMOVING ELEMENTS:")
print("=" * 50)

# remove() - Remove element (raises error if not found)
colors = {"red", "green", "blue", "yellow"}
print(f"Original: {colors}")

colors.remove("blue")
print(f"After remove('blue'): {colors}")

try:
    colors.remove("purple")
except KeyError as e:
    print(f"Error: {e}")

# discard() - Remove element (no error if not found)
colors = {"red", "green", "blue", "yellow"}
print(f"\nOriginal: {colors}")

colors.discard("blue")
print(f"After discard('blue'): {colors}")

colors.discard("purple")  # No error!
print(f"After discard('purple'): {colors}")

# pop() - Remove and return arbitrary element
numbers = {1, 2, 3, 4, 5}
print(f"\nOriginal: {numbers}")

removed = numbers.pop()
print(f"Popped: {removed}")
print(f"After pop(): {numbers}")

# Error if set is empty
empty_set = set()
try:
    empty_set.pop()
except KeyError as e:
    print(f"Error on empty set: {e}")

# clear() - Remove all elements
colors = {"red", "green", "blue"}
print(f"\nOriginal: {colors}")

colors.clear()
print(f"After clear(): {colors}")

# Set Operations - Union
print("\n" + "=" * 50)
print("SET UNION (|):")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")

# Using | operator
union1 = set1 | set2
print(f"\nset1 | set2: {union1}")

# Using union() method
union2 = set1.union(set2)
print(f"set1.union(set2): {union2}")

# Union with multiple sets
set3 = {5, 6, 7, 8}
union3 = set1 | set2 | set3
print(f"\nset1 | set2 | set3: {union3}")

# Visual representation
print("\n--- Visual ---")
print("set1:        {1, 2, 3, 4}")
print("set2:              {3, 4, 5, 6}")
print("Union:       {1, 2, 3, 4, 5, 6}")

# Set Operations - Intersection
print("\n" + "=" * 50)
print("SET INTERSECTION (&):")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")

# Using & operator
intersection1 = set1 & set2
print(f"\nset1 & set2: {intersection1}")

# Using intersection() method
intersection2 = set1.intersection(set2)
print(f"set1.intersection(set2): {intersection2}")

# Intersection with multiple sets
set3 = {2, 3, 4, 7}
intersection3 = set1 & set2 & set3
print(f"\nset1 & set2 & set3: {intersection3}")

# Visual representation
print("\n--- Visual ---")
print("set1:        {1, 2, 3, 4}")
print("set2:              {3, 4, 5, 6}")
print("Intersection:      {3, 4}")

# Set Operations - Difference
print("\n" + "=" * 50)
print("SET DIFFERENCE (-):")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")

# Using - operator
diff1 = set1 - set2
print(f"\nset1 - set2: {diff1}")

diff2 = set2 - set1
print(f"set2 - set1: {diff2}")

# Using difference() method
diff3 = set1.difference(set2)
print(f"\nset1.difference(set2): {diff3}")

# Visual representation
print("\n--- Visual ---")
print("set1:        {1, 2, 3, 4}")
print("set2:              {3, 4, 5, 6}")
print("set1 - set2: {1, 2}")
print("set2 - set1:             {5, 6}")

# Set Operations - Symmetric Difference
print("\n" + "=" * 50)
print("SET SYMMETRIC DIFFERENCE (^):")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")

# Using ^ operator
sym_diff1 = set1 ^ set2
print(f"\nset1 ^ set2: {sym_diff1}")

# Using symmetric_difference() method
sym_diff2 = set1.symmetric_difference(set2)
print(f"set1.symmetric_difference(set2): {sym_diff2}")

# Visual representation
print("\n--- Visual ---")
print("set1:             {1, 2, 3, 4}")
print("set2:                   {3, 4, 5, 6}")
print("Symmetric diff:   {1, 2,       5, 6}")
print("(Elements in either set, but not both)")

# Set Relationships
print("\n" + "=" * 50)
print("SET RELATIONSHIPS:")
print("=" * 50)

# Subset
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(f"set1: {set1}")
print(f"set2: {set2}")

print(f"\nset1.issubset(set2): {set1.issubset(set2)}")
print(f"set1 <= set2: {set1 <= set2}")

# Proper subset
print(f"\nset1 < set2: {set1 < set2}")  # True (proper subset)
print(f"set1 < set1: {set1 < set1}")  # False (not proper)

# Superset
print(f"\nset2.issuperset(set1): {set2.issuperset(set1)}")
print(f"set2 >= set1: {set2 >= set1}")

# Proper superset
print(f"\nset2 > set1: {set2 > set1}")  # True

# Disjoint (no common elements)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

print(f"\nset1: {set1}")
print(f"set2: {set2}")
print(f"set3: {set3}")

print(f"\nset1.isdisjoint(set2): {set1.isdisjoint(set2)}")  # True
print(f"set1.isdisjoint(set3): {set1.isdisjoint(set3)}")  # False

# Set Comprehensions
print("\n" + "=" * 50)
print("SET COMPREHENSIONS:")
print("=" * 50)

# Basic comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
evens = {x for x in range(10) if x % 2 == 0}
print(f"Evens: {evens}")

# String manipulation
words = ["hello", "world", "python", "sets"]
upper_words = {word.upper() for word in words}
print(f"\nOriginal: {words}")
print(f"Uppercase: {upper_words}")

# Remove duplicates and apply transformation
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
doubled = {x * 2 for x in numbers}
print(f"\nOriginal: {numbers}")
print(f"Doubled (unique): {doubled}")

# Frozen Sets (Immutable Sets)
print("\n" + "=" * 50)
print("FROZEN SETS:")
print("=" * 50)

# Create frozen set
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")
print(f"Type: {type(frozen)}")

# Cannot modify frozen set
try:
    frozen.add(6)
except AttributeError as e:
    print(f"Error: {e}")

# Can use as dictionary key
dict_with_set_key = {frozen: "value"}
print(f"\nFrozen set as dict key: {dict_with_set_key}")

# Regular set cannot be dict key
try:
    regular_set = {1, 2, 3}
    bad_dict = {regular_set: "value"}
except TypeError as e:
    print(f"Regular set as key error: {e}")

# Frozen sets support all query operations
frozen1 = frozenset([1, 2, 3])
frozen2 = frozenset([3, 4, 5])

print(f"\nfrozen1: {frozen1}")
print(f"frozen2: {frozen2}")
print(f"Union: {frozen1 | frozen2}")
print(f"Intersection: {frozen1 & frozen2}")

# Set Iteration
print("\n" + "=" * 50)
print("SET ITERATION:")
print("=" * 50)

fruits = {"apple", "banana", "orange", "grape"}

print("Iterating over set:")
for fruit in fruits:
    print(f"  - {fruit}")

# Order is not guaranteed!
print("\nNote: Order may vary between runs")

# Convert to sorted list for ordered iteration
print("\nSorted iteration:")
for fruit in sorted(fruits):
    print(f"  - {fruit}")

# Copying Sets
print("\n" + "=" * 50)
print("COPYING SETS:")
print("=" * 50)

original = {1, 2, 3, 4, 5}
print(f"Original: {original}")

# Shallow copy methods
copy1 = original.copy()
copy2 = set(original)

print(f"copy1: {copy1}")
print(f"copy2: {copy2}")

# Modify copy
copy1.add(999)
print(f"\nAfter copy1.add(999):")
print(f"Original: {original}")  # Unchanged
print(f"copy1: {copy1}")

# Real-world Example: Unique Visitors
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: UNIQUE VISITORS")
print("=" * 50)

# Website visits (with duplicates)
visits = [
    "user1", "user2", "user1", "user3", 
    "user2", "user4", "user1", "user5"
]

print(f"All visits: {visits}")
print(f"Total visits: {len(visits)}")

unique_visitors = set(visits)
print(f"\nUnique visitors: {unique_visitors}")
print(f"Total unique visitors: {len(unique_visitors)}")

# Real-world Example: Tags System
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: BLOG TAGS")
print("=" * 50)

post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "data-science", "tutorial"}
post3_tags = {"javascript", "web-dev", "programming"}

print(f"Post 1 tags: {post1_tags}")
print(f"Post 2 tags: {post2_tags}")
print(f"Post 3 tags: {post3_tags}")

# All tags used
all_tags = post1_tags | post2_tags | post3_tags
print(f"\nAll tags: {all_tags}")

# Common tags between post 1 and 2
common = post1_tags & post2_tags
print(f"Common tags (post1 & post2): {common}")

# Tags only in post 1
exclusive = post1_tags - post2_tags
print(f"Exclusive to post 1: {exclusive}")

# Real-world Example: Email Comparison
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: EMAIL LISTS")
print("=" * 50)

newsletter_a = {"alice@email.com", "bob@email.com", "charlie@email.com"}
newsletter_b = {"bob@email.com", "diana@email.com", "eve@email.com"}

print(f"Newsletter A: {len(newsletter_a)} subscribers")
print(f"Newsletter B: {len(newsletter_b)} subscribers")

# Subscribers to both
both = newsletter_a & newsletter_b
print(f"\nSubscribed to both: {both}")

# Only newsletter A
only_a = newsletter_a - newsletter_b
print(f"Only newsletter A: {only_a}")

# Only newsletter B
only_b = newsletter_b - newsletter_a
print(f"Only newsletter B: {only_b}")

# All subscribers
all_subscribers = newsletter_a | newsletter_b
print(f"\nTotal unique subscribers: {len(all_subscribers)}")

# Real-world Example: Remove Duplicates
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: REMOVE DUPLICATES")
print("=" * 50)

# Shopping list with duplicates
shopping = [
    "milk", "bread", "eggs", "milk", 
    "butter", "bread", "cheese", "milk"
]

print("Shopping list (with duplicates):")
for i, item in enumerate(shopping, 1):
    print(f"  {i}. {item}")

print(f"\nTotal items: {len(shopping)}")

# Remove duplicates
unique_items = list(set(shopping))
print(f"\nUnique items: {unique_items}")
print(f"Items to buy: {len(unique_items)}")

# Real-world Example: Permission System
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: USER PERMISSIONS")
print("=" * 50)

admin_permissions = {"read", "write", "delete", "admin"}
editor_permissions = {"read", "write", "edit"}
viewer_permissions = {"read"}

print(f"Admin: {admin_permissions}")
print(f"Editor: {editor_permissions}")
print(f"Viewer: {viewer_permissions}")

# Check if user has permission
def has_permission(user_perms, required_perm):
    return required_perm in user_perms

print(f"\nAdmin can 'delete': {has_permission(admin_permissions, 'delete')}")
print(f"Editor can 'delete': {has_permission(editor_permissions, 'delete')}")

# Extra permissions admin has over editor
extra = admin_permissions - editor_permissions
print(f"\nExtra admin permissions: {extra}")

# Common permissions
common = admin_permissions & editor_permissions
print(f"Common permissions: {common}")

# Common Patterns
print("\n" + "=" * 50)
print("COMMON PATTERNS:")
print("=" * 50)

# Check if any elements in common
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [4, 5, 6, 7]

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

has_common_1_2 = bool(set(list1) & set(list2))
print(f"\nlist1 and list2 have common elements: {has_common_1_2}")

has_common_1_3 = bool(set(list1) & set(list3))
print(f"list1 and list3 have common elements: {has_common_1_3}")

# Find unique elements across all lists
all_unique = set(list1) | set(list2) | set(list3)
print(f"\nAll unique elements: {all_unique}")

# Find elements that appear in all lists
common_all = set(list1) & set(list2) & set(list3)
print(f"Elements in all lists: {common_all}")

# Practice Exercises
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a set from a list and remove duplicates")
print("2. Find common elements between two lists using sets")
print("3. Create a program to track unique words in a text")
print("4. Build a simple tag system for blog posts")
print("5. Compare two shopping lists and find common/different items")
print("6. Create a permission checker using sets")
print("7. Find all unique characters in a string")
print("8. Implement set operations: union, intersection, difference")
print("=" * 50)