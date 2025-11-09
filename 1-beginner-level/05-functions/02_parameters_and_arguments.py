"""
PARAMETERS AND ARGUMENTS
=========================

Understanding the difference between parameters and arguments, and mastering
different types of parameters is crucial for writing flexible and maintainable
Python functions.

Key Concepts:
- Parameters vs Arguments
- Positional parameters
- Keyword parameters
- Default parameters
- Variable-length positional (*args)
- Variable-length keyword (**kwargs)
- Position-only parameters (/)
- Keyword-only parameters (*)
- Parameter order rules
- Argument unpacking

Terminology:
- Parameters: Variables in function DEFINITION
- Arguments: Actual values passed when CALLING function
"""

# Parameters vs Arguments
print("PARAMETERS VS ARGUMENTS:")
print("=" * 50)

def greet(name, greeting):  # name and greeting are PARAMETERS
    """Print a personalized greeting."""
    print(f"{greeting}, {name}!")

# "Alice" and "Hello" are ARGUMENTS
greet("Alice", "Hello")

print("""
Parameters: Variables in the function definition
  def greet(name, greeting):  ← name, greeting are parameters
                └─ DEFINITION

Arguments: Values passed to the function
  greet("Alice", "Hello")     ← "Alice", "Hello" are arguments
        └─ CALL
""")

# Positional Parameters and Arguments
print("\n" + "=" * 50)
print("POSITIONAL PARAMETERS:")
print("=" * 50)

def introduce(name, age, city):
    """Order matters with positional arguments."""
    print(f"{name} is {age} years old and lives in {city}")

print("Correct order:")
introduce("Alice", 25, "Paris")

print("\nWrong order gives wrong results:")
introduce("Paris", "Alice", 25)  # Wrong but no error!

print("\nPositional arguments must match parameter order")

# Keyword Arguments
print("\n" + "=" * 50)
print("KEYWORD ARGUMENTS:")
print("=" * 50)

def create_user(username, email, age):
    """Create user with named arguments."""
    print(f"User: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")

print("Order doesn't matter with keyword arguments:")
create_user(email="alice@email.com", age=25, username="alice123")

print("\nMixing positional and keyword (positional first!):")
create_user("bob456", age=30, email="bob@email.com")

# This would cause an error:
# create_user(username="charlie", "charlie@email.com", 28)
print("\nNote: Positional arguments must come BEFORE keyword arguments")

# Default Parameters
print("\n" + "=" * 50)
print("DEFAULT PARAMETERS:")
print("=" * 50)

def send_email(to, subject, body="", cc=None, bcc=None):
    """Send email with optional parameters."""
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"CC: {cc}")
    print(f"BCC: {bcc}")

print("Only required parameters:")
send_email("alice@email.com", "Hello")

print("\nWith some optional parameters:")
send_email("bob@email.com", "Meeting", body="See you at 3pm")

print("\nWith all parameters:")
send_email("charlie@email.com", "Report", "Attached", "boss@email.com", "hr@email.com")

# Default parameter rules
print("\n" + "=" * 50)
print("DEFAULT PARAMETER RULES:")
print("=" * 50)

# ✓ Correct: defaults after required
def correct(required, optional="default"):
    print(f"Required: {required}, Optional: {optional}")

correct("value1")
correct("value1", "value2")

# ✗ Wrong: default before required
print("\nThis would cause SyntaxError:")
print("  def wrong(optional='default', required):")
print("  ❌ Non-default parameter follows default parameter")

# Mutable Default Arguments (DANGER!)
print("\n" + "=" * 50)
print("MUTABLE DEFAULT ARGUMENTS - COMMON PITFALL:")
print("=" * 50)

# ❌ BAD: Mutable default argument
def bad_append(item, lst=[]):
    """DON'T DO THIS! List is shared between calls!"""
    lst.append(item)
    return lst

print("Calling bad_append multiple times:")
result1 = bad_append(1)
print(f"  First call: {result1}")

result2 = bad_append(2)
print(f"  Second call: {result2}")  # Unexpected!

result3 = bad_append(3)
print(f"  Third call: {result3}")  # List keeps growing!

print("\n⚠️  The list is shared between all calls!")

# ✓ GOOD: Use None as default
def good_append(item, lst=None):
    """Correct way to handle mutable defaults."""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("\nCalling good_append multiple times:")
result1 = good_append(1)
print(f"  First call: {result1}")

result2 = good_append(2)
print(f"  Second call: {result2}")  # Works correctly!

result3 = good_append(3)
print(f"  Third call: {result3}")  # Each call gets new list!

# Variable-Length Positional Arguments (*args)
print("\n" + "=" * 50)
print("VARIABLE-LENGTH POSITIONAL (*args):")
print("=" * 50)

def sum_numbers(*numbers):
    """Accept any number of positional arguments."""
    print(f"Received: {numbers}")
    print(f"Type: {type(numbers)}")  # tuple
    total = sum(numbers)
    return total

print("sum_numbers(1, 2, 3):")
result = sum_numbers(1, 2, 3)
print(f"Result: {result}")

print("\nsum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10):")
result = sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Result: {result}")

print("\nsum_numbers() with no arguments:")
result = sum_numbers()
print(f"Result: {result}")

# *args with regular parameters
def greet_all(greeting, *names):
    """First arg is greeting, rest are names."""
    print(f"Greeting: {greeting}")
    print(f"Names: {names}")
    for name in names:
        print(f"  {greeting}, {name}!")

print("\ngreet_all('Hello', 'Alice', 'Bob', 'Charlie'):")
greet_all('Hello', 'Alice', 'Bob', 'Charlie')

# Variable-Length Keyword Arguments (**kwargs)
print("\n" + "=" * 50)
print("VARIABLE-LENGTH KEYWORD (**kwargs):")
print("=" * 50)

def print_info(**kwargs):
    """Accept any number of keyword arguments."""
    print(f"Received: {kwargs}")
    print(f"Type: {type(kwargs)}")  # dict
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("print_info(name='Alice', age=25, city='Paris'):")
print_info(name='Alice', age=25, city='Paris')

print("\nprint_info(job='Engineer', company='TechCorp', years=5):")
print_info(job='Engineer', company='TechCorp', years=5)

# **kwargs with regular parameters
def create_profile(username, **details):
    """Username is required, rest are optional details."""
    print(f"Username: {username}")
    print("Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

print("\ncreate_profile('alice123', email='alice@email.com', age=25, city='Paris'):")
create_profile('alice123', email='alice@email.com', age=25, city='Paris')

# Combining All Parameter Types
print("\n" + "=" * 50)
print("COMBINING ALL PARAMETER TYPES:")
print("=" * 50)

def complex_function(required, *args, default="value", **kwargs):
    """Demonstration of all parameter types together."""
    print(f"Required parameter: {required}")
    print(f"*args (tuple): {args}")
    print(f"Default parameter: {default}")
    print(f"**kwargs (dict): {kwargs}")

print("complex_function(1, 2, 3, default='custom', key1='val1', key2='val2'):")
complex_function(1, 2, 3, default='custom', key1='val1', key2='val2')

print("\ncomplex_function('only_required'):")
complex_function('only_required')

# Parameter Order Rules
print("\n" + "=" * 50)
print("PARAMETER ORDER RULES:")
print("=" * 50)

print("""
Correct parameter order in function definition:
1. Regular positional parameters
2. *args (variable positional)
3. Default parameters
4. **kwargs (variable keyword)

Example:
def function(pos1, pos2, *args, default1="a", default2="b", **kwargs):
    pass

Special markers:
- / : Everything before is position-only (Python 3.8+)
- * : Everything after is keyword-only

def function(pos_only, /, both, *, kwd_only):
    pass
""")

# Position-Only Parameters (/)
print("\n" + "=" * 50)
print("POSITION-ONLY PARAMETERS (/):")
print("=" * 50)

def divide(a, b, /):
    """a and b MUST be positional (Python 3.8+)."""
    return a / b

print("Can only use positional arguments:")
result = divide(10, 2)
print(f"divide(10, 2) = {result}")

# This would cause an error:
# result = divide(a=10, b=2)
print("\ndivide(a=10, b=2) would cause TypeError!")

# Why use position-only?
def calculate(x, y, /):
    """Prevents confusion if parameter names change."""
    return x + y

print("\nPosition-only allows parameter name changes without breaking code")

# Keyword-Only Parameters (*)
print("\n" + "=" * 50)
print("KEYWORD-ONLY PARAMETERS (*):")
print("=" * 50)

def create_user(username, *, email, age):
    """email and age MUST be keyword arguments."""
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")

print("Must use keywords for email and age:")
create_user("alice123", email="alice@email.com", age=25)

# This would cause an error:
# create_user("alice123", "alice@email.com", 25)
print("\ncreate_user('alice123', 'alice@email.com', 25) would cause TypeError!")

# Why use keyword-only?
print("\n💡 Forces clarity and prevents mistakes with many parameters")

# Combining Position-Only and Keyword-Only
print("\n" + "=" * 50)
print("COMBINING / AND *:")
print("=" * 50)

def api_call(endpoint, /, *, method, timeout=30):
    """
    endpoint: position-only
    method: keyword-only (required)
    timeout: keyword-only (optional)
    """
    print(f"Endpoint: {endpoint}")
    print(f"Method: {method}")
    print(f"Timeout: {timeout}")

print("api_call('/users', method='GET'):")
api_call('/users', method='GET')

print("\napi_call('/data', method='POST', timeout=60):")
api_call('/data', method='POST', timeout=60)

# Full example with all markers
def full_example(pos_only, /, standard, *args, kwd_only, **kwargs):
    """Demonstrates all parameter types."""
    print(f"Position-only: {pos_only}")
    print(f"Standard: {standard}")
    print(f"*args: {args}")
    print(f"Keyword-only: {kwd_only}")
    print(f"**kwargs: {kwargs}")

print("\nfull_example(1, 2, 3, 4, kwd_only=5, extra1=6, extra2=7):")
full_example(1, 2, 3, 4, kwd_only=5, extra1=6, extra2=7)

# Argument Unpacking
print("\n" + "=" * 50)
print("ARGUMENT UNPACKING:")
print("=" * 50)

# Unpacking list/tuple with *
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(f"numbers = {numbers}")
result = add_three(*numbers)  # Unpacks list
print(f"add_three(*numbers) = {result}")

# Unpacking dictionary with **
def greet(name, greeting):
    return f"{greeting}, {name}!"

person = {"name": "Alice", "greeting": "Hello"}
print(f"\nperson = {person}")
result = greet(**person)  # Unpacks dict
print(f"greet(**person) = {result}")

# Combining unpacking
def create_profile(name, age, city, country):
    return f"{name}, {age}, from {city}, {country}"

basic_info = ["Alice", 25]
location = {"city": "Paris", "country": "France"}

result = create_profile(*basic_info, **location)
print(f"\ncreate_profile(*basic_info, **location):")
print(f"Result: {result}")

# Argument Unpacking in Function Calls
print("\n" + "=" * 50)
print("PRACTICAL UNPACKING EXAMPLES:")
print("=" * 50)

# Unpacking range
def sum_range(start, stop, step):
    return sum(range(start, stop, step))

range_params = (0, 10, 2)
result = sum_range(*range_params)
print(f"sum_range(*{range_params}) = {result}")

# Unpacking config dictionary
def connect_db(host, port, username, password):
    return f"Connecting to {host}:{port} as {username}"

config = {
    "host": "localhost",
    "port": 5432,
    "username": "admin",
    "password": "secret123"
}

result = connect_db(**config)
print(f"\nconnect_db(**config) = {result}")

# Real-World Example: Function Builder
print("\n" + "=" * 50)
print("REAL-WORLD: FLEXIBLE FUNCTION DESIGN")
print("=" * 50)

def send_notification(user_id, /, message, *, channel="email", priority=1, **metadata):
    """
    Flexible notification system.
    
    Args:
        user_id: Position-only (implementation detail)
        message: Standard parameter
        channel: Keyword-only with default
        priority: Keyword-only with default
        **metadata: Any additional data
    """
    print(f"Sending to user: {user_id}")
    print(f"Message: {message}")
    print(f"Channel: {channel}")
    print(f"Priority: {priority}")
    if metadata:
        print(f"Metadata: {metadata}")

print("Basic notification:")
send_notification(12345, "Hello!")

print("\nAdvanced notification:")
send_notification(
    67890, 
    "Important message", 
    channel="sms", 
    priority=5,
    category="alert",
    timestamp="2025-11-09"
)

# Real-World Example: API Wrapper
print("\n" + "=" * 50)
print("REAL-WORLD: API WRAPPER")
print("=" * 50)

def api_request(endpoint, /, method="GET", **params):
    """
    Generic API request wrapper.
    
    Args:
        endpoint: API endpoint (position-only)
        method: HTTP method (default GET)
        **params: Query parameters
    """
    print(f"Making {method} request to: {endpoint}")
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        print(f"Query parameters: {query}")

print("Simple GET request:")
api_request("/users")

print("\nGET with parameters:")
api_request("/users", method="GET", page=1, limit=10, sort="name")

print("\nPOST request:")
api_request("/users", method="POST", name="Alice", email="alice@email.com")

# Real-World Example: Logger Function
print("\n" + "=" * 50)
print("REAL-WORLD: LOGGER FUNCTION")
print("=" * 50)

def log(level, message, *args, **kwargs):
    """
    Flexible logging function.
    
    Args:
        level: Log level (INFO, WARNING, ERROR)
        message: Log message (can include format placeholders)
        *args: Positional arguments for formatting
        **kwargs: Additional metadata
    """
    formatted_message = message.format(*args) if args else message
    print(f"[{level}] {formatted_message}")
    if kwargs:
        print(f"  Metadata: {kwargs}")

print("Simple log:")
log("INFO", "Application started")

print("\nLog with formatting:")
log("WARNING", "User {} attempted {} logins", "alice123", 5)

print("\nLog with metadata:")
log("ERROR", "Database connection failed", 
    error_code=500, 
    retry_count=3,
    timestamp="2025-11-09 10:30:00")

# Real-World Example: Data Processor
print("\n" + "=" * 50)
print("REAL-WORLD: DATA PROCESSOR")
print("=" * 50)

def process_data(data, /, transform=None, *, filter_fn=None, sort_key=None, reverse=False):
    """
    Process data with various operations.
    
    Args:
        data: Input data (position-only to allow 'data' in kwargs)
        transform: Function to transform each item
        filter_fn: Function to filter items (keyword-only)
        sort_key: Function for sorting (keyword-only)
        reverse: Reverse sort order (keyword-only)
    """
    result = data[:]  # Copy
    
    if filter_fn:
        result = [x for x in result if filter_fn(x)]
        print(f"After filter: {result}")
    
    if transform:
        result = [transform(x) for x in result]
        print(f"After transform: {result}")
    
    if sort_key:
        result = sorted(result, key=sort_key, reverse=reverse)
        print(f"After sort: {result}")
    
    return result

numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(f"Original: {numbers}")

result = process_data(
    numbers,
    transform=lambda x: x * 2,
    filter_fn=lambda x: x > 5,
    sort_key=lambda x: x,
    reverse=True
)
print(f"Final result: {result}")

# Common Patterns and Best Practices
print("\n" + "=" * 50)
print("BEST PRACTICES:")
print("=" * 50)

print("""
✅ DO:
1. Use descriptive parameter names
2. Use None for mutable default arguments
3. Use keyword-only (*) for clarity with many parameters
4. Use position-only (/) to hide implementation details
5. Document parameters in docstrings
6. Keep parameter lists short (< 5 parameters ideal)

❌ DON'T:
1. Use mutable objects (list, dict) as default arguments
2. Mix positional and keyword arguments confusingly
3. Have too many parameters (consider using a dict/class)
4. Use unclear single-letter names (except in math functions)
5. Change parameter order in existing APIs
""")

# Practice Exercises
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a function that accepts any number of numbers and returns their average")
print("2. Write a function with 3 required and 2 optional parameters")
print("3. Create a function that accepts **kwargs and prints all key-value pairs")
print("4. Fix this function: def bad(lst=[]): lst.append(1); return lst")
print("5. Write a function with position-only and keyword-only parameters")
print("6. Create a flexible search function using *args and **kwargs")
print("7. Build a configuration manager using default and keyword arguments")
print("8. Design an API wrapper function with proper parameter types")
print("=" * 50)