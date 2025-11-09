"""
DICTIONARIES
============

Dictionaries are unordered collections of key-value pairs. They are also known
as associative arrays, hash maps, or objects in other languages. Dictionaries
are optimized for retrieving data by key.

Key Concepts:
- Creating dictionaries
- Accessing values by key
- Adding, updating, removing items
- Dictionary methods
- Dictionary operations
- Nested dictionaries
- Dictionary comprehensions

Why use dictionaries?
- Fast lookups by key
- Store related data together
- Flexible structure
- Real-world data representation
"""

# Creating Dictionaries
print("CREATING DICTIONARIES:")
print("=" * 50)

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")
print(f"Type: {type(empty_dict)}")

# Also using dict()
empty_dict2 = dict()
print(f"Using dict(): {empty_dict2}")

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"\nPerson: {person}")

# Dictionary with different value types
mixed = {
    "name": "Bob",
    "age": 30,
    "scores": [85, 90, 88],
    "is_student": False,
    "address": None
}
print(f"\nMixed types: {mixed}")

# Using dict() constructor
person2 = dict(name="Charlie", age=28, city="London")
print(f"\nUsing dict(): {person2}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_pairs = dict(pairs)
print(f"\nFrom tuples: {from_pairs}")

# From two lists using zip
keys = ["name", "age", "city"]
values = ["Diana", 22, "Paris"]
from_zip = dict(zip(keys, values))
print(f"\nUsing zip: {from_zip}")

# Keys must be immutable (strings, numbers, tuples)
valid_keys = {
    "string_key": 1,
    42: "number key",
    (1, 2): "tuple key",
    3.14: "float key"
}
print(f"\nValid keys: {valid_keys}")

# Lists and sets cannot be keys
try:
    bad_dict = {[1, 2]: "list key"}
except TypeError as e:
    print(f"\nError with list as key: {e}")

# Accessing Dictionary Values
print("\n" + "=" * 50)
print("ACCESSING VALUES:")
print("=" * 50)

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

print(f"Dictionary: {student}")

# Using square brackets
print(f"\nstudent['name']: {student['name']}")
print(f"student['age']: {student['age']}")
print(f"student['courses']: {student['courses']}")

# KeyError if key doesn't exist
try:
    print(student['address'])
except KeyError as e:
    print(f"\nKeyError: {e}")

# Using get() method (safer)
print("\n--- Using get() ---")
name = student.get('name')
print(f"get('name'): {name}")

address = student.get('address')
print(f"get('address'): {address}")  # Returns None

# get() with default value
address = student.get('address', 'Not provided')
print(f"get('address', 'Not provided'): {address}")

phone = student.get('phone', 'No phone')
print(f"get('phone', 'No phone'): {phone}")

# Checking if Key Exists
print("\n" + "=" * 50)
print("CHECKING IF KEY EXISTS:")
print("=" * 50)

person = {"name": "Bob", "age": 30, "city": "Tokyo"}

print(f"Dictionary: {person}")

print(f"\n'name' in person: {'name' in person}")
print(f"'address' in person: {'address' in person}")
print(f"'age' not in person: {'age' not in person}")

# Safe access pattern
if 'address' in person:
    print(person['address'])
else:
    print("Address not found")

# Adding and Updating Items
print("\n" + "=" * 50)
print("ADDING AND UPDATING:")
print("=" * 50)

person = {"name": "Alice", "age": 25}
print(f"Original: {person}")

# Add new key
person["city"] = "Paris"
print(f"After adding city: {person}")

person["country"] = "France"
print(f"After adding country: {person}")

# Update existing key
person["age"] = 26
print(f"\nAfter updating age: {person}")

# Update multiple items
person["age"] = 27
person["job"] = "Engineer"
print(f"After multiple updates: {person}")

# Using update() method
print("\n--- Using update() ---")
person = {"name": "Bob", "age": 30}
print(f"Original: {person}")

person.update({"city": "London", "job": "Teacher"})
print(f"After update(): {person}")

# update() can also update existing keys
person.update({"age": 31, "country": "UK"})
print(f"After another update(): {person}")

# Removing Items
print("\n" + "=" * 50)
print("REMOVING ITEMS:")
print("=" * 50)

# pop() - Remove and return value
person = {"name": "Charlie", "age": 28, "city": "Berlin"}
print(f"Original: {person}")

age = person.pop("age")
print(f"\nPopped 'age': {age}")
print(f"After pop: {person}")

# pop() with default value (no error if key missing)
country = person.pop("country", "Not found")
print(f"\nPopped 'country': {country}")
print(f"Dictionary unchanged: {person}")

# del statement
person = {"name": "Diana", "age": 22, "city": "Madrid"}
print(f"\nOriginal: {person}")

del person["age"]
print(f"After del person['age']: {person}")

# popitem() - Remove and return last inserted item
person = {"name": "Eve", "age": 35, "city": "Rome"}
print(f"\nOriginal: {person}")

item = person.popitem()
print(f"Popped item: {item}")
print(f"After popitem(): {person}")

# clear() - Remove all items
person = {"name": "Frank", "age": 40}
print(f"\nOriginal: {person}")

person.clear()
print(f"After clear(): {person}")

# Dictionary Length
print("\n" + "=" * 50)
print("DICTIONARY LENGTH:")
print("=" * 50)

person = {"name": "Alice", "age": 25, "city": "Paris"}
print(f"Dictionary: {person}")
print(f"Length: {len(person)}")

empty = {}
print(f"\nEmpty dict: {empty}")
print(f"Length: {len(empty)}")

# Dictionary Methods - keys(), values(), items()
print("\n" + "=" * 50)
print("KEYS, VALUES, ITEMS:")
print("=" * 50)

person = {"name": "Bob", "age": 30, "city": "Tokyo"}
print(f"Dictionary: {person}")

# keys() - Get all keys
keys = person.keys()
print(f"\nkeys(): {keys}")
print(f"Type: {type(keys)}")

# Convert to list
keys_list = list(keys)
print(f"As list: {keys_list}")

# values() - Get all values
values = person.values()
print(f"\nvalues(): {values}")
print(f"As list: {list(values)}")

# items() - Get all key-value pairs
items = person.items()
print(f"\nitems(): {items}")
print(f"As list: {list(items)}")

# Iterating over items
print("\n--- Iterating ---")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary Iteration
print("\n" + "=" * 50)
print("DICTIONARY ITERATION:")
print("=" * 50)

scores = {"Math": 85, "Physics": 92, "Chemistry": 88}

# Method 1: Iterate over keys (default)
print("Method 1: Keys")
for subject in scores:
    print(f"  {subject}: {scores[subject]}")

# Method 2: Explicitly iterate over keys
print("\nMethod 2: keys()")
for subject in scores.keys():
    print(f"  {subject}: {scores[subject]}")

# Method 3: Iterate over values
print("\nMethod 3: values()")
for score in scores.values():
    print(f"  Score: {score}")

# Method 4: Iterate over key-value pairs (best)
print("\nMethod 4: items()")
for subject, score in scores.items():
    print(f"  {subject}: {score}")

# Dictionary Comprehension
print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION:")
print("=" * 50)

# Basic comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"\nEvens squared: {evens}")

# From two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
people = {name: age for name, age in zip(names, ages)}
print(f"\nPeople: {people}")

# Transform existing dictionary
prices = {"apple": 2.5, "banana": 1.5, "orange": 3.0}
print(f"\nOriginal prices: {prices}")

discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Discounted (10% off): {discounted}")

# Filter dictionary
scores = {"Math": 85, "Physics": 92, "Chemistry": 78, "Biology": 95}
print(f"\nAll scores: {scores}")

high_scores = {subject: score for subject, score in scores.items() if score >= 90}
print(f"High scores (>=90): {high_scores}")

# Nested Dictionaries
print("\n" + "=" * 50)
print("NESTED DICTIONARIES:")
print("=" * 50)

# Dictionary of dictionaries
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": {"Math": 85, "Physics": 90}
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "grades": {"Math": 92, "Physics": 88}
    }
}

print("Students data:")
for student_id, info in students.items():
    print(f"\n{student_id}:")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    print(f"  Grades: {info['grades']}")

# Accessing nested values
print(f"\nAlice's Math grade: {students['student1']['grades']['Math']}")
print(f"Bob's Physics grade: {students['student2']['grades']['Physics']}")

# Complex nested structure
company = {
    "name": "Tech Corp",
    "departments": {
        "engineering": {
            "employees": ["Alice", "Bob"],
            "budget": 1000000
        },
        "marketing": {
            "employees": ["Charlie", "Diana"],
            "budget": 500000
        }
    }
}

print(f"\nCompany: {company['name']}")
print(f"Engineering employees: {company['departments']['engineering']['employees']}")

# Copying Dictionaries
print("\n" + "=" * 50)
print("COPYING DICTIONARIES:")
print("=" * 50)

original = {"name": "Alice", "age": 25, "city": "Paris"}
print(f"Original: {original}")

# Shallow copy methods
copy1 = original.copy()
copy2 = dict(original)

print(f"copy1: {copy1}")
print(f"copy2: {copy2}")

# Modify copy
copy1["age"] = 999
print(f"\nAfter copy1['age'] = 999:")
print(f"Original: {original}")  # Unchanged
print(f"copy1: {copy1}")

# Shallow copy issue with nested structures
original = {"name": "Bob", "scores": [85, 90, 88]}
copy = original.copy()

copy["scores"][0] = 999
print(f"\nAfter modifying nested list:")
print(f"Original: {original}")  # Also changed!
print(f"Copy: {copy}")

# Deep copy for nested structures
import copy as copy_module

original = {"name": "Charlie", "scores": [85, 90, 88]}
deep_copy = copy_module.deepcopy(original)

deep_copy["scores"][0] = 999
print(f"\nWith deep copy:")
print(f"Original: {original}")  # Unchanged
print(f"Deep copy: {deep_copy}")

# Merging Dictionaries
print("\n" + "=" * 50)
print("MERGING DICTIONARIES:")
print("=" * 50)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print(f"dict1: {dict1}")
print(f"dict2: {dict2}")

# Method 1: Using update()
merged = dict1.copy()
merged.update(dict2)
print(f"\nMerged (update): {merged}")

# Method 2: Using ** unpacking (Python 3.5+)
merged = {**dict1, **dict2}
print(f"Merged (unpacking): {merged}")

# Method 3: Using | operator (Python 3.9+)
merged = dict1 | dict2
print(f"Merged (| operator): {merged}")

# Handling duplicate keys
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 4}

print(f"\ndict1: {dict1}")
print(f"dict2: {dict2}")

merged = dict1 | dict2
print(f"Merged (dict2 values win): {merged}")

# Default Dictionary Values
print("\n" + "=" * 50)
print("DEFAULT VALUES - setdefault():")
print("=" * 50)

person = {"name": "Alice", "age": 25}
print(f"Original: {person}")

# Get value or set default if key doesn't exist
city = person.setdefault("city", "Unknown")
print(f"\nsetdefault('city', 'Unknown'): {city}")
print(f"Dictionary now: {person}")

# Key already exists - returns existing value
age = person.setdefault("age", 30)
print(f"\nsetdefault('age', 30): {age}")
print(f"Dictionary unchanged: {person}")

# Real-world Example: Word Counter
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: WORD COUNTER")
print("=" * 50)

text = "hello world hello python python python world"
words = text.split()

print(f"Text: {text}")
print(f"Words: {words}")

# Count words
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"\nWord count: {word_count}")

# Better way using get()
word_count2 = {}
for word in words:
    word_count2[word] = word_count2.get(word, 0) + 1

print(f"Using get(): {word_count2}")

# Real-world Example: Student Records
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: STUDENT RECORDS")
print("=" * 50)

students = {
    "S001": {
        "name": "Alice Johnson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
        "courses": ["Python", "Data Structures", "Algorithms"]
    },
    "S002": {
        "name": "Bob Smith",
        "age": 21,
        "major": "Mathematics",
        "gpa": 3.6,
        "courses": ["Calculus", "Linear Algebra", "Statistics"]
    },
    "S003": {
        "name": "Charlie Brown",
        "age": 19,
        "major": "Computer Science",
        "gpa": 3.9,
        "courses": ["Python", "Web Development", "Databases"]
    }
}

print("STUDENT DATABASE")
print("=" * 50)
for student_id, info in students.items():
    print(f"\nID: {student_id}")
    print(f"Name: {info['name']}")
    print(f"Major: {info['major']}")
    print(f"GPA: {info['gpa']}")
    print(f"Courses: {', '.join(info['courses'])}")

# Find students by major
cs_students = {sid: info for sid, info in students.items() 
               if info['major'] == 'Computer Science'}
print(f"\nComputer Science students: {len(cs_students)}")

# Find highest GPA
highest_gpa = max(students.values(), key=lambda x: x['gpa'])
print(f"\nHighest GPA: {highest_gpa['name']} - {highest_gpa['gpa']}")

# Real-world Example: Shopping Cart
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SHOPPING CART")
print("=" * 50)

cart = {}

# Add items
cart["Apple"] = {"price": 2.5, "quantity": 3}
cart["Banana"] = {"price": 1.5, "quantity": 5}
cart["Orange"] = {"price": 3.0, "quantity": 2}

print("SHOPPING CART")
print("-" * 50)
total = 0
for item, details in cart.items():
    subtotal = details["price"] * details["quantity"]
    total += subtotal
    print(f"{item:10} ${details['price']:.2f} x {details['quantity']} = ${subtotal:.2f}")

print("-" * 50)
print(f"{'TOTAL':>30} ${total:.2f}")

# Real-world Example: Configuration Settings
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: APP CONFIGURATION")
print("=" * 50)

config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "features": {
        "authentication": True,
        "notifications": False,
        "dark_mode": True
    }
}

print("Application Configuration:")
print(f"  App: {config['app_name']} v{config['version']}")
print(f"  Debug mode: {config['debug']}")
print(f"\nDatabase:")
print(f"  Host: {config['database']['host']}")
print(f"  Port: {config['database']['port']}")
print(f"  Name: {config['database']['name']}")
print(f"\nFeatures:")
for feature, enabled in config['features'].items():
    status = "✓" if enabled else "✗"
    print(f"  {status} {feature}")

# Real-world Example: Contact Book
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: CONTACT BOOK")
print("=" * 50)

contacts = {
    "Alice": {
        "phone": "555-1234",
        "email": "alice@email.com",
        "address": "123 Main St"
    },
    "Bob": {
        "phone": "555-5678",
        "email": "bob@email.com",
        "address": "456 Oak Ave"
    }
}

def add_contact(name, phone, email, address):
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"✓ Added {name} to contacts")

def search_contact(name):
    if name in contacts:
        print(f"\n{name}:")
        for key, value in contacts[name].items():
            print(f"  {key.capitalize()}: {value}")
    else:
        print(f"✗ {name} not found")

# Add new contact
add_contact("Charlie", "555-9012", "charlie@email.com", "789 Pine Rd")

# Search contacts
search_contact("Alice")
search_contact("Diana")

print(f"\nTotal contacts: {len(contacts)}")

# Real-world Example: Inventory System
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: INVENTORY SYSTEM")
print("=" * 50)

inventory = {
    "P001": {"name": "Laptop", "price": 999.99, "stock": 15},
    "P002": {"name": "Mouse", "price": 29.99, "stock": 50},
    "P003": {"name": "Keyboard", "price": 79.99, "stock": 30},
    "P004": {"name": "Monitor", "price": 299.99, "stock": 8}
}

print("INVENTORY")
print(f"{'Code':<8} {'Product':<12} {'Price':>10} {'Stock':>8}")
print("-" * 42)

for code, product in inventory.items():
    print(f"{code:<8} {product['name']:<12} ${product['price']:>9.2f} {product['stock']:>8}")

# Low stock items (< 10)
print("\n⚠ Low Stock Items:")
low_stock = {code: prod for code, prod in inventory.items() if prod['stock'] < 10}
for code, product in low_stock.items():
    print(f"  {product['name']}: {product['stock']} units")

# Total inventory value
total_value = sum(prod['price'] * prod['stock'] for prod in inventory.values())
print(f"\nTotal Inventory Value: ${total_value:,.2f}")

# Common Patterns
print("\n" + "=" * 50)
print("COMMON PATTERNS:")
print("=" * 50)

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(f"Original: {original}")
print(f"Swapped: {swapped}")

# Count occurrences
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
print(f"\nItem counts: {counts}")

# Group by property
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "B"}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

print(f"\nStudents by grade:")
for grade, names in by_grade.items():
    print(f"  Grade {grade}: {names}")

# Practice Exercises
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a dictionary for a person with name, age, city")
print("2. Add and update items in a dictionary")
print("3. Build a word counter for a text")
print("4. Create nested dictionaries for company structure")
print("5. Implement a simple contact book (add, search, delete)")
print("6. Build an inventory system with stock tracking")
print("7. Create a student grade tracker")
print("8. Merge multiple dictionaries with conflict handling")
print("=" * 50)