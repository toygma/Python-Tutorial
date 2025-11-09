"""
DEFAULT PARAMETERS
==================

Default parameters allow functions to have optional arguments with predefined
values. This makes functions more flexible and easier to use.

Key Concepts:
- Basic default parameters
- Multiple default parameters
- Combining required and optional parameters
- Default parameter evaluation time
- Mutable default arguments (common pitfall!)
- None as sentinel value
- Best practices for default parameters
- Real-world usage patterns

Benefits:
- Backward compatibility
- Simpler function calls
- Flexible APIs
- Sensible defaults
"""

# Basic Default Parameters
print("BASIC DEFAULT PARAMETERS:")
print("=" * 50)

def greet(name="Guest"):
    """Greet with default name."""
    print(f"Hello, {name}!")

# Without argument - uses default
print("Without argument:")
greet()

# With argument - overrides default
print("\nWith argument:")
greet("Alice")

# Multiple calls showing flexibility
print("\nMultiple calls:")
greet()
greet("Bob")
greet("Charlie")

# Multiple Default Parameters
print("\n" + "=" * 50)
print("MULTIPLE DEFAULT PARAMETERS:")
print("=" * 50)

def create_user(username, email="", age=0, active=True):
    """Create user with multiple optional parameters."""
    print(f"Username: {username}")
    print(f"Email: {email if email else 'Not provided'}")
    print(f"Age: {age}")
    print(f"Active: {active}")

print("Only required parameter:")
create_user("alice123")

print("\nWith some optional parameters:")
create_user("bob456", email="bob@email.com")

print("\nWith all parameters:")
create_user("charlie789", "charlie@email.com", 25, False)

print("\nUsing keyword arguments:")
create_user("diana000", age=30, active=False)

# Combining Required and Optional Parameters
print("\n" + "=" * 50)
print("REQUIRED + OPTIONAL PARAMETERS:")
print("=" * 50)

def book_flight(passenger, destination, date, seat_class="Economy", meal="Standard"):
    """Book flight with required and optional parameters."""
    print(f"Passenger: {passenger}")
    print(f"Destination: {destination}")
    print(f"Date: {date}")
    print(f"Class: {seat_class}")
    print(f"Meal: {meal}")

print("Minimum required parameters:")
book_flight("Alice", "Paris", "2025-12-01")

print("\nWith one optional parameter:")
book_flight("Bob", "London", "2025-12-15", seat_class="Business")

print("\nWith all parameters:")
book_flight("Charlie", "Tokyo", "2026-01-01", "First", "Vegetarian")

# Parameter Order Rule
print("\n" + "=" * 50)
print("PARAMETER ORDER RULE:")
print("=" * 50)

print("""
✅ CORRECT: Required parameters BEFORE default parameters
def function(required1, required2, optional1="a", optional2="b"):
    pass

❌ WRONG: Default parameter before required
def function(optional="a", required):  # SyntaxError!
    pass

Why? Once you have a default parameter, all following parameters
must also have defaults.
""")

# Correct example
def correct(a, b, c="default_c", d="default_d"):
    print(f"a={a}, b={b}, c={c}, d={d}")

print("correct(1, 2):")
correct(1, 2)

print("\ncorrect(1, 2, 'custom_c'):")
correct(1, 2, 'custom_c')

# Default Parameter Evaluation
print("\n" + "=" * 50)
print("DEFAULT PARAMETER EVALUATION:")
print("=" * 50)

import datetime

def log_time(message, timestamp=datetime.datetime.now()):
    """PROBLEM: Default evaluated at DEFINITION time!"""
    print(f"[{timestamp}] {message}")

print("Calling function multiple times:")
log_time("First call")

import time
time.sleep(1)  # Wait 1 second

log_time("Second call")
# Both show same timestamp! Because default is evaluated once at definition

print("\n⚠️  Default values are evaluated ONCE when function is defined!")
print("    Not each time the function is called!")

# Correct Approach
print("\n" + "=" * 50)
print("CORRECT APPROACH FOR DYNAMIC DEFAULTS:")
print("=" * 50)

def log_time_correct(message, timestamp=None):
    """Use None as sentinel, compute actual default in function."""
    if timestamp is None:
        timestamp = datetime.datetime.now()
    print(f"[{timestamp}] {message}")

print("Calling function multiple times:")
log_time_correct("First call")

time.sleep(1)  # Wait 1 second

log_time_correct("Second call")
# Now each call has its own timestamp!

print("\n✅ Use None as default, then compute actual value inside function")

# Mutable Default Arguments - THE TRAP!
print("\n" + "=" * 50)
print("MUTABLE DEFAULT ARGUMENTS - COMMON PITFALL!")
print("=" * 50)

# ❌ WRONG: Using mutable default
def add_item_wrong(item, shopping_list=[]):
    """BUG: List is shared between all calls!"""
    shopping_list.append(item)
    return shopping_list

print("❌ WRONG approach:")
list1 = add_item_wrong("milk")
print(f"First call: {list1}")

list2 = add_item_wrong("bread")
print(f"Second call: {list2}")  # Contains milk too!

list3 = add_item_wrong("eggs")
print(f"Third call: {list3}")  # Contains everything!

print("\n⚠️  The default list is SHARED between all calls!")
print("    It's created once and reused!")

# ✅ CORRECT: Using None as default
def add_item_correct(item, shopping_list=None):
    """Correct: Create new list each time if not provided."""
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    return shopping_list

print("\n✅ CORRECT approach:")
list1 = add_item_correct("milk")
print(f"First call: {list1}")

list2 = add_item_correct("bread")
print(f"Second call: {list2}")  # Only bread!

list3 = add_item_correct("eggs")
print(f"Third call: {list3}")  # Only eggs!

# Can still pass a list to continue building it
my_list = ["butter"]
list4 = add_item_correct("cheese", my_list)
print(f"Fourth call with existing list: {list4}")

# More Mutable Default Examples
print("\n" + "=" * 50)
print("MORE MUTABLE DEFAULT EXAMPLES:")
print("=" * 50)

# ❌ Wrong with dictionary
def add_config_wrong(key, value, config={}):
    """Bug: dict is shared!"""
    config[key] = value
    return config

print("❌ Wrong dictionary default:")
c1 = add_config_wrong("theme", "dark")
print(f"First call: {c1}")

c2 = add_config_wrong("language", "en")
print(f"Second call: {c2}")  # Has both!

# ✅ Correct with dictionary
def add_config_correct(key, value, config=None):
    """Correct: Create new dict if needed."""
    if config is None:
        config = {}
    config[key] = value
    return config

print("\n✅ Correct dictionary default:")
c1 = add_config_correct("theme", "dark")
print(f"First call: {c1}")

c2 = add_config_correct("language", "en")
print(f"Second call: {c2}")  # Only language!

# ❌ Wrong with set
def add_tag_wrong(tag, tags=set()):
    """Bug: set is shared!"""
    tags.add(tag)
    return tags

print("\n❌ Wrong set default:")
t1 = add_tag_wrong("python")
print(f"First call: {t1}")

t2 = add_tag_wrong("javascript")
print(f"Second call: {t2}")  # Has both!

# ✅ Correct with set
def add_tag_correct(tag, tags=None):
    """Correct: Create new set if needed."""
    if tags is None:
        tags = set()
    tags.add(tag)
    return tags

print("\n✅ Correct set default:")
t1 = add_tag_correct("python")
print(f"First call: {t1}")

t2 = add_tag_correct("javascript")
print(f"Second call: {t2}")  # Only javascript!

# Why This Happens
print("\n" + "=" * 50)
print("WHY MUTABLE DEFAULTS BEHAVE THIS WAY:")
print("=" * 50)

print("""
When Python reads:
    def function(param=[]):
        pass

It creates the list [] ONCE when defining the function,
not each time you call it!

The default value becomes part of the function object:
    function.__defaults__  # Contains the actual default objects

If you modify a mutable default, you're modifying that
single shared object used by all calls.

Solution: Use None (immutable) as default, then create
the mutable object inside the function.
""")

# Demonstrating Function Defaults
def show_defaults(lst=[]):
    """Demonstrate how defaults are stored."""
    return lst

print("Function defaults storage:")
print(f"show_defaults.__defaults__ = {show_defaults.__defaults__}")
print(f"ID of default list: {id(show_defaults.__defaults__[0])}")

# Modify the default
result = show_defaults()
result.append(1)

print(f"\nAfter appending to default:")
print(f"show_defaults.__defaults__ = {show_defaults.__defaults__}")
print(f"ID of default list: {id(show_defaults.__defaults__[0])}")
print("Same ID - same object!")

# None as Sentinel Value
print("\n" + "=" * 50)
print("NONE AS SENTINEL VALUE:")
print("=" * 50)

def process_data(data, default_value=None):
    """Use None to distinguish 'not provided' from actual values."""
    if default_value is None:
        default_value = []
    
    # Process data
    return default_value

# Can now distinguish between these cases:
result1 = process_data([1, 2, 3])  # No default provided
result2 = process_data([1, 2, 3], [])  # Empty list provided
result3 = process_data([1, 2, 3], [99])  # List with value provided

print("Different ways to call:")
print(f"No default: {result1}")
print(f"Empty list: {result2}")
print(f"List with value: {result3}")

# Multiple None Defaults
print("\n" + "=" * 50)
print("MULTIPLE NONE DEFAULTS:")
print("=" * 50)

def create_report(title, sections=None, authors=None, tags=None):
    """Create report with multiple optional collections."""
    if sections is None:
        sections = []
    if authors is None:
        authors = []
    if tags is None:
        tags = set()
    
    print(f"Title: {title}")
    print(f"Sections: {sections}")
    print(f"Authors: {authors}")
    print(f"Tags: {tags}")

print("With no optional parameters:")
create_report("Q4 Report")

print("\nWith some optional parameters:")
create_report("Annual Report", sections=["Intro", "Results"], tags={"important", "2025"})

# Real-World Example: API Function
print("\n" + "=" * 50)
print("REAL-WORLD: API REQUEST FUNCTION")
print("=" * 50)

def api_request(url, method="GET", headers=None, data=None, timeout=30):
    """Make API request with sensible defaults."""
    if headers is None:
        headers = {"Content-Type": "application/json"}
    
    print(f"Making {method} request to: {url}")
    print(f"Headers: {headers}")
    print(f"Data: {data}")
    print(f"Timeout: {timeout}s")

print("Simple GET request:")
api_request("https://api.example.com/users")

print("\nPOST with custom headers:")
custom_headers = {"Authorization": "Bearer token123"}
api_request(
    "https://api.example.com/users",
    method="POST",
    headers=custom_headers,
    data={"name": "Alice"}
)

# Real-World Example: Database Connection
print("\n" + "=" * 50)
print("REAL-WORLD: DATABASE CONNECTION")
print("=" * 50)

def connect_db(host="localhost", port=5432, username="admin", 
               password="", database="mydb", options=None):
    """Connect to database with defaults."""
    if options is None:
        options = {"timeout": 30, "pool_size": 10}
    
    print("Connection parameters:")
    print(f"  Host: {host}")
    print(f"  Port: {port}")
    print(f"  Username: {username}")
    print(f"  Database: {database}")
    print(f"  Options: {options}")

print("Local development (all defaults):")
connect_db(password="dev123")

print("\nProduction (custom settings):")
connect_db(
    host="prod.db.example.com",
    port=3306,
    username="prod_user",
    password="prod_pass",
    database="production",
    options={"timeout": 60, "pool_size": 50, "ssl": True}
)

# Real-World Example: Email Function
print("\n" + "=" * 50)
print("REAL-WORLD: EMAIL SENDER")
print("=" * 50)

def send_email(to, subject, body, cc=None, bcc=None, 
               attachments=None, priority="normal", html=False):
    """Send email with optional parameters."""
    if cc is None:
        cc = []
    if bcc is None:
        bcc = []
    if attachments is None:
        attachments = []
    
    print("Email details:")
    print(f"  To: {to}")
    print(f"  Subject: {subject}")
    print(f"  Body: {body[:50]}...")
    print(f"  CC: {cc if cc else 'None'}")
    print(f"  BCC: {bcc if bcc else 'None'}")
    print(f"  Attachments: {len(attachments)} file(s)")
    print(f"  Priority: {priority}")
    print(f"  HTML: {html}")

print("Simple email:")
send_email("user@example.com", "Hello", "This is a test message")

print("\nComplex email:")
send_email(
    "team@example.com",
    "Weekly Report",
    "Please find the weekly report attached.",
    cc=["manager@example.com"],
    bcc=["archive@example.com"],
    attachments=["report.pdf", "data.xlsx"],
    priority="high",
    html=True
)

# Real-World Example: Logger
print("\n" + "=" * 50)
print("REAL-WORLD: LOGGER FUNCTION")
print("=" * 50)

def log(message, level="INFO", timestamp=None, metadata=None):
    """Log message with optional parameters."""
    if timestamp is None:
        timestamp = datetime.datetime.now()
    if metadata is None:
        metadata = {}
    
    print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] [{level}] {message}")
    if metadata:
        print(f"  Metadata: {metadata}")

print("Simple log:")
log("Application started")

print("\nDetailed log:")
log(
    "User login failed",
    level="WARNING",
    metadata={"user": "alice123", "attempts": 3, "ip": "192.168.1.1"}
)

# Real-World Example: Configuration
print("\n" + "=" * 50)
print("REAL-WORLD: CONFIGURATION BUILDER")
print("=" * 50)

def create_config(env="development", debug=True, port=8000, 
                 allowed_hosts=None, middleware=None):
    """Create application configuration."""
    if allowed_hosts is None:
        allowed_hosts = ["localhost", "127.0.0.1"]
    if middleware is None:
        middleware = ["auth", "logging"]
    
    config = {
        "environment": env,
        "debug": debug,
        "port": port,
        "allowed_hosts": allowed_hosts,
        "middleware": middleware
    }
    
    print("Configuration:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    return config

print("Development config (defaults):")
create_config()

print("\nProduction config (custom):")
create_config(
    env="production",
    debug=False,
    port=80,
    allowed_hosts=["example.com", "www.example.com"],
    middleware=["auth", "logging", "compression", "security"]
)

# Best Practices Summary
print("\n" + "=" * 50)
print("BEST PRACTICES:")
print("=" * 50)

print("""
✅ DO:
1. Use immutable defaults (None, numbers, strings, tuples)
2. Use None for mutable defaults, create inside function
3. Place required parameters before optional ones
4. Use descriptive names showing what default means
5. Document defaults in docstrings
6. Use sensible defaults that work for most cases
7. Group related optional parameters

❌ DON'T:
1. Use mutable defaults (lists, dicts, sets) directly
2. Use function calls as defaults (evaluated once!)
3. Have too many default parameters (consider **kwargs)
4. Use defaults that aren't truly optional
5. Change default values in existing APIs carelessly

💡 REMEMBER:
- Defaults evaluated once at function definition time
- Mutable defaults are SHARED between all calls
- None is your friend for mutable defaults
- Defaults should make functions easier to use
""")

# Common Patterns
print("\n" + "=" * 50)
print("COMMON PATTERNS:")
print("=" * 50)

# Pattern 1: Optional collection
def add_items(items, collection=None):
    """Optional collection that's created if not provided."""
    if collection is None:
        collection = []
    collection.extend(items)
    return collection

result = add_items([1, 2, 3])
print(f"Pattern 1 - Optional collection: {result}")

# Pattern 2: Optional configuration
def process(data, config=None):
    """Optional config dict with defaults."""
    if config is None:
        config = {}
    
    # Merge with defaults
    default_config = {"timeout": 30, "retries": 3}
    final_config = {**default_config, **config}
    
    print(f"Processing with config: {final_config}")

process([1, 2, 3])
process([1, 2, 3], {"timeout": 60})

# Pattern 3: Flag with default
def format_text(text, uppercase=False, trim=True):
    """Boolean flags with sensible defaults."""
    if trim:
        text = text.strip()
    if uppercase:
        text = text.upper()
    return text

print(f"\nPattern 3 - Format '  hello  ': {format_text('  hello  ')}")
print(f"With uppercase: {format_text('  hello  ', uppercase=True)}")

# Practice Exercises
print("\n" + "=" * 50)
print("--- EXERCISES ---")
print("1. Create a function with 3 default parameters")
print("2. Fix this bug: def add(x, lst=[]): lst.append(x); return lst")
print("3. Write a function that uses None for a default timestamp")
print("4. Create an API wrapper with sensible defaults")
print("5. Build a configuration function with multiple defaults")
print("6. Write a logger with optional metadata dictionary")
print("7. Create a function demonstrating default evaluation time")
print("8. Design a user creation function with optional fields")
print("=" * 50)