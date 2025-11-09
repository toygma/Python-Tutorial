"""
FUNCTION DEFINITION
===================

Functions are reusable blocks of code that perform a specific task. They help
organize code, avoid repetition, and make programs easier to understand and
maintain.

Key Concepts:
- Defining functions
- Function parameters and arguments
- Return values
- Default parameters
- Keyword arguments
- Variable-length arguments (*args, **kwargs)
- Docstrings
- Function scope
- Lambda functions

Why use functions?
- Code reusability
- Better organization
- Easier testing and debugging
- Abstraction and modularity
"""

# Basic Function Definition
print("BASIC FUNCTION DEFINITION:")
print("=" * 50)

# Simple function with no parameters
def greet():
    """Print a greeting message."""
    print("Hello, World!")

print("Calling greet():")
greet()

# Function with parameters
def greet_person(name):
    """Print a personalized greeting."""
    print(f"Hello, {name}!")

print("\nCalling greet_person('Alice'):")
greet_person("Alice")

# Function with multiple parameters
def greet_full(first_name, last_name):
    """Print greeting with full name."""
    print(f"Hello, {first_name} {last_name}!")

print("\nCalling greet_full('John', 'Doe'):")
greet_full("John", "Doe")

# Function Syntax
print("\n" + "=" * 50)
print("FUNCTION SYNTAX:")
print("=" * 50)

print("""
def function_name(parameter1, parameter2):
    '''Docstring: Describes what the function does'''
    # Function body
    # Do something
    return result  # Optional

# Calling the function
result = function_name(argument1, argument2)
""")

# Return Values
print("\n" + "=" * 50)
print("RETURN VALUES:")
print("=" * 50)

# Function that returns a value
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}")

# Function with multiple operations
def calculate_area(length, width):
    """Calculate area of rectangle."""
    area = length * width
    return area

area = calculate_area(5, 3)
print(f"\ncalculate_area(5, 3) = {area}")

# Function returning multiple values (as tuple)
def get_min_max(numbers):
    """Return both minimum and maximum from list."""
    return min(numbers), max(numbers)

numbers = [3, 7, 2, 9, 1, 5]
minimum, maximum = get_min_max(numbers)
print(f"\nget_min_max({numbers}):")
print(f"  Minimum: {minimum}")
print(f"  Maximum: {maximum}")

# Function with no return (returns None)
def print_message(message):
    """Print a message (no return value)."""
    print(message)

result = print_message("Hello!")
print(f"\nFunction returned: {result}")

# Default Parameters
print("\n" + "=" * 50)
print("DEFAULT PARAMETERS:")
print("=" * 50)

def greet_with_default(name="Guest"):
    """Greet with default name if not provided."""
    print(f"Hello, {name}!")

print("Without argument:")
greet_with_default()

print("\nWith argument:")
greet_with_default("Alice")

# Multiple default parameters
def create_profile(name, age=0, city="Unknown"):
    """Create user profile with defaults."""
    print(f"Name: {name}, Age: {age}, City: {city}")

print("\nAll parameters:")
create_profile("Alice", 25, "Paris")

print("\nOnly required parameter:")
create_profile("Bob")

print("\nSome optional parameters:")
create_profile("Charlie", 30)

# Default parameters must come after non-default
def invalid_function():
    """This would cause an error:"""
    # def bad_func(a=1, b):  # SyntaxError!
    #     pass
    print("  Default parameters must come AFTER required ones")

invalid_function()

# Keyword Arguments
print("\n" + "=" * 50)
print("KEYWORD ARGUMENTS:")
print("=" * 50)

def introduce(name, age, city):
    """Introduce a person."""
    print(f"{name} is {age} years old and lives in {city}")

# Positional arguments
print("Positional arguments:")
introduce("Alice", 25, "Paris")

# Keyword arguments (any order)
print("\nKeyword arguments:")
introduce(age=30, city="London", name="Bob")

# Mix of positional and keyword
print("\nMixed (positional first):")
introduce("Charlie", city="Tokyo", age=28)

# Named arguments for clarity
print("\nNamed for clarity:")
introduce(name="Diana", age=22, city="Berlin")

# Position-only and Keyword-only Parameters
print("\n" + "=" * 50)
print("POSITION-ONLY AND KEYWORD-ONLY:")
print("=" * 50)

# Keyword-only parameters (after *)
def create_user(name, *, age, email):
    """age and email must be passed as keywords."""
    print(f"User: {name}, Age: {age}, Email: {email}")

print("Must use keywords for age and email:")
create_user("Alice", age=25, email="alice@email.com")

# This would cause an error:
# create_user("Alice", 25, "alice@email.com")

# Position-only parameters (before /)
def calculate(a, b, /):
    """a and b must be positional (Python 3.8+)."""
    return a + b

print(f"\ncalculate(5, 3) = {calculate(5, 3)}")

# Variable-Length Arguments (*args)
print("\n" + "=" * 50)
print("VARIABLE-LENGTH ARGUMENTS (*args):")
print("=" * 50)

def sum_all(*numbers):
    """Sum any number of arguments."""
    total = sum(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    return total

print("sum_all(1, 2, 3):")
sum_all(1, 2, 3)

print("\nsum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10):")
sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# *args collects into tuple
def print_args(*args):
    """Show what *args collects."""
    print(f"Type: {type(args)}")
    print(f"Content: {args}")
    print("Individual items:")
    for i, arg in enumerate(args, 1):
        print(f"  arg {i}: {arg}")

print("\nprint_args('a', 'b', 'c'):")
print_args('a', 'b', 'c')

# Combining regular and *args
def greet_all(greeting, *names):
    """Greet multiple people."""
    for name in names:
        print(f"{greeting}, {name}!")

print("\ngreet_all('Hello', 'Alice', 'Bob', 'Charlie'):")
greet_all('Hello', 'Alice', 'Bob', 'Charlie')

# Variable-Length Keyword Arguments (**kwargs)
print("\n" + "=" * 50)
print("VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs):")
print("=" * 50)

def create_profile(**info):
    """Create profile from keyword arguments."""
    print("Profile:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print("create_profile(name='Alice', age=25, city='Paris'):")
create_profile(name='Alice', age=25, city='Paris')

print("\ncreate_profile(name='Bob', job='Engineer', country='USA', hobbies='Reading'):")
create_profile(name='Bob', job='Engineer', country='USA', hobbies='Reading')

# **kwargs collects into dictionary
def print_kwargs(**kwargs):
    """Show what **kwargs collects."""
    print(f"Type: {type(kwargs)}")
    print(f"Content: {kwargs}")

print("\nprint_kwargs(a=1, b=2, c=3):")
print_kwargs(a=1, b=2, c=3)

# Combining *args and **kwargs
print("\n" + "=" * 50)
print("COMBINING *args AND **kwargs:")
print("=" * 50)

def flexible_function(*args, **kwargs):
    """Accept any positional and keyword arguments."""
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

print("flexible_function(1, 2, 3, name='Alice', age=25):")
flexible_function(1, 2, 3, name='Alice', age=25)

# Common pattern: all argument types
def complete_function(required, *args, default="value", **kwargs):
    """Function with all parameter types."""
    print(f"Required: {required}")
    print(f"*args: {args}")
    print(f"Default: {default}")
    print(f"**kwargs: {kwargs}")

print("\ncomplete_function(1, 2, 3, default='custom', key1='value1'):")
complete_function(1, 2, 3, default='custom', key1='value1')

# Docstrings
print("\n" + "=" * 50)
print("DOCSTRINGS:")
print("=" * 50)

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Parameters:
        numbers (list): A list of numeric values
        
    Returns:
        float: The average of the numbers
        
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    return sum(numbers) / len(numbers)

# Access docstring
print("Function docstring:")
print(calculate_average.__doc__)

# Using help()
print("\nUsing help():")
help(calculate_average)

# Function Scope
print("\n" + "=" * 50)
print("FUNCTION SCOPE:")
print("=" * 50)

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")

scope_demo()

print(f"\nOutside function - global_var: {global_var}")
try:
    print(f"Outside function - local_var: {local_var}")
except NameError as e:
    print(f"Error: {e}")

# Modifying global variables
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print(f"\nCounter before: {counter}")
increment()
increment()
print(f"Counter after: {counter}")

# Nested Functions
print("\n" + "=" * 50)
print("NESTED FUNCTIONS:")
print("=" * 50)

def outer_function(text):
    """Outer function containing inner function."""
    
    def inner_function():
        """Inner function can access outer variables."""
        print(f"Inner: {text}")
    
    print(f"Outer: {text}")
    inner_function()

outer_function("Hello")

# Lambda Functions
print("\n" + "=" * 50)
print("LAMBDA FUNCTIONS:")
print("=" * 50)

# Regular function
def square(x):
    return x ** 2

print(f"square(5) = {square(5)}")

# Lambda function (anonymous function)
square_lambda = lambda x: x ** 2
print(f"square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"\nadd(3, 4) = {add(3, 4)}")

# Lambda in sorted()
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 95)
]

print("\nOriginal list:")
for student in students:
    print(f"  {student}")

# Sort by score (second element)
sorted_students = sorted(students, key=lambda x: x[1])
print("\nSorted by score:")
for student in sorted_students:
    print(f"  {student}")

# Lambda in filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nEven numbers: {evens}")

# Lambda in map()
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Function as Argument
print("\n" + "=" * 50)
print("FUNCTIONS AS ARGUMENTS:")
print("=" * 50)

def apply_operation(x, y, operation):
    """Apply given operation to x and y."""
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 3, add)
print(f"apply_operation(5, 3, add) = {result1}")

result2 = apply_operation(5, 3, multiply)
print(f"apply_operation(5, 3, multiply) = {result2}")

# With lambda
result3 = apply_operation(5, 3, lambda a, b: a - b)
print(f"apply_operation(5, 3, lambda a, b: a - b) = {result3}")

# Real-world Example: Temperature Converter
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TEMPERATURE CONVERTER")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")

# Real-world Example: Grade Calculator
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: GRADE CALCULATOR")
print("=" * 50)

def calculate_grade(score):
    """
    Calculate letter grade based on score.
    
    Args:
        score (int): Score between 0 and 100
        
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def calculate_average_grade(scores):
    """Calculate average and letter grade."""
    avg = sum(scores) / len(scores)
    grade = calculate_grade(avg)
    return avg, grade

student_scores = [85, 92, 78, 88, 95]
average, letter_grade = calculate_average_grade(student_scores)

print(f"Scores: {student_scores}")
print(f"Average: {average:.2f}")
print(f"Grade: {letter_grade}")

# Real-world Example: Validator Functions
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: VALIDATOR FUNCTIONS")
print("=" * 50)

def is_valid_email(email):
    """Check if email format is valid (simple check)."""
    return '@' in email and '.' in email

def is_valid_password(password):
    """Check if password meets requirements."""
    has_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    return has_length and has_digit and has_upper

def validate_user(email, password):
    """Validate user credentials."""
    email_valid = is_valid_email(email)
    password_valid = is_valid_password(password)
    
    if not email_valid:
        return False, "Invalid email format"
    if not password_valid:
        return False, "Password must be 8+ chars with digit and uppercase"
    
    return True, "Valid credentials"

# Test validation
email = "user@example.com"
password = "Pass1234"
is_valid, message = validate_user(email, password)
print(f"Email: {email}")
print(f"Password: {password}")
print(f"Valid: {is_valid}, Message: {message}")

# Real-world Example: Data Processing
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: DATA PROCESSING")
print("=" * 50)

def clean_data(data):
    """Remove None and empty values."""
    return [item for item in data if item]

def transform_data(data, transformation):
    """Apply transformation to each item."""
    return [transformation(item) for item in data]

def filter_data(data, condition):
    """Filter data based on condition."""
    return [item for item in data if condition(item)]

# Example pipeline
raw_data = [1, 2, None, 4, 5, "", 7, 8, 9, 10]
print(f"Raw data: {raw_data}")

cleaned = clean_data(raw_data)
print(f"Cleaned: {cleaned}")

doubled = transform_data(cleaned, lambda x: x * 2)
print(f"Doubled: {doubled}")

large = filter_data(doubled, lambda x: x > 10)
print(f"Greater than 10: {large}")

# Common Patterns
print("\n" + "=" * 50)
print("COMMON PATTERNS:")
print("=" * 50)

# 1. Helper function
def format_currency(amount):
    """Format number as currency."""
    return f"${amount:,.2f}"

print(f"format_currency(1234.5): {format_currency(1234.5)}")

# 2. Early return
def divide(a, b):
    """Divide a by b with error handling."""
    if b == 0:
        return None  # Early return on error
    return a / b

print(f"\ndivide(10, 2): {divide(10, 2)}")
print(f"divide(10, 0): {divide(10, 0)}")

# 3. Function with default mutable argument (AVOID!)
def bad_append(item, lst=[]):  # BUG: mutable default!
    """This has a bug with mutable default."""
    lst.append(item)
    return lst

# Better approach
def good_append(item, lst=None):
    """Correct way with mutable default."""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"\ngood_append('a'): {good_append('a')}")
print(f"good_append('b'): {good_append('b')}")

# Practice Exercises
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Write a function that checks if a number is prime")
print("2. Create a function that reverses a string")
print("3. Write a function that finds the largest number in a list")
print("4. Create a calculator function with operations as parameters")
print("5. Write a function that counts vowels in a string")
print("6. Create a function that generates Fibonacci sequence")
print("7. Write a function decorator (advanced)")
print("8. Create a function that validates credit card numbers")
print("=" * 50)