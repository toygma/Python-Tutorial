# ============================================================================
# FILE: 02_string_operations.py
"""
STRING OPERATIONS
=================

Strings are sequences of characters. Python provides many methods and operations
to manipulate strings.

Key Concepts:
- String indexing and slicing
- String methods
- String concatenation
- String formatting
"""

# String creation
text = "Python Programming"
single_quote = 'Hello'
double_quote = "World"

# String indexing (starts at 0)
print("String Indexing:")
print(f"First character: {text[0]}")  # P
print(f"Last character: {text[-1]}")  # g
print(f"Third character: {text[2]}")  # t

# String slicing [start:end:step]
print("\nString Slicing:")
print(f"First 6 characters: {text[0:6]}")  # Python
print(f"From index 7 to end: {text[7:]}")  # Programming
print(f"Last 4 characters: {text[-4:]}")  # ming
print(f"Every 2nd character: {text[::2]}")  # Pto rgamn

# String methods
print("\nString Methods:")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Replace: {text.replace('Python', 'Java')}")

sample = "  hello world  "
print(f"Strip whitespace: '{sample.strip()}'")
print(f"Split: {text.split()}")

# String checking methods
print("\nString Checking:")
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'ing': {text.endswith('ing')}")
print(f"Contains 'gram': {'gram' in text}")
print(f"Is alphanumeric: {text.isalnum()}")
print(f"Is alphabetic: {text.isalpha()}")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\nConcatenation: {full_name}")

# String formatting
age = 25
# f-strings (modern way)
message1 = f"My name is {full_name} and I am {age} years old"
# format() method
message2 = "My name is {} and I am {} years old".format(full_name, age)
# % formatting (old way)
message3 = "My name is %s and I am %d years old" % (full_name, age)

print("\nString Formatting:")
print(message1)
print(message2)
print(message3)

# String length
print(f"\nLength of text: {len(text)}")

# Character counting
print(f"Count of 'a': {text.count('a')}")
print(f"Index of 'Programming': {text.find('Programming')}")

# Practice Exercises:
print("\n--- EXERCISES ---")
print("1. Create a string with your full name")
print("2. Print the first letter, last letter, and middle letters")
print("3. Convert your name to uppercase and lowercase")
print("4. Count how many vowels are in your name")