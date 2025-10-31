# FILE: 04_nested_conditions.py
"""
NESTED CONDITIONS
=================

Nested conditions are if statements inside other if statements. They allow
you to check multiple conditions in a hierarchical manner.

Key Concepts:
- If inside if
- Multiple levels of nesting
- When to use nested conditions
- Avoiding deep nesting
- Alternatives to nesting
"""

# Basic Nested Conditions
print("BASIC NESTED CONDITIONS:")
print("=" * 50)

age = 25
has_license = True

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive")
    else:
        print("You need to get a license")
else:
    print("You are too young to drive")

# Multiple Level Nesting
print("\n" + "=" * 50)
print("MULTIPLE LEVEL NESTING:")

score = 85
attendance = 90
assignment_done = True

if score >= 60:
    print("You passed the course")
    if attendance >= 75:
        print("Good attendance record")
        if assignment_done:
            print("All assignments completed")
            print("Final Grade: A")
        else:
            print("Missing assignments")
            print("Final Grade: B")
    else:
        print("Poor attendance")
        print("Final Grade: C")
else:
    print("You failed the course")

# Real-world Example: Login System
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: LOGIN SYSTEM")

def login_system(username, password, is_active, is_verified):
    """Multi-level authentication check"""
    if username:
        print(f"Username '{username}' found")
        if password == "correct_password":
            print("Password correct")
            if is_active:
                print("Account is active")
                if is_verified:
                    print("✓ Login successful!")
                    return "Success"
                else:
                    print("✗ Email not verified")
                    return "Verify email"
            else:
                print("✗ Account is suspended")
                return "Account suspended"
        else:
            print("✗ Incorrect password")
            return "Wrong password"
    else:
        print("✗ Username is required")
        return "No username"

# Test cases
print("\nTest 1: Valid login")
result = login_system("john_doe", "correct_password", True, True)
print(f"Result: {result}\n")

print("Test 2: Not verified")
result = login_system("jane_doe", "correct_password", True, False)
print(f"Result: {result}\n")

print("Test 3: Wrong password")
result = login_system("user123", "wrong_pass", True, True)
print(f"Result: {result}")

# Real-world Example: Ticket Pricing
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: TICKET PRICING")

def calculate_ticket_price(age, is_student, is_weekend):
    """Calculate ticket price with multiple conditions"""
    base_price = 20
    
    if age < 18:
        # Child pricing
        if is_weekend:
            price = base_price * 0.7  # 30% off
            discount = "Child weekend discount"
        else:
            price = base_price * 0.5  # 50% off
            discount = "Child discount"
    elif age >= 65:
        # Senior pricing
        if is_weekend:
            price = base_price * 0.8  # 20% off
            discount = "Senior weekend discount"
        else:
            price = base_price * 0.6  # 40% off
            discount = "Senior discount"
    else:
        # Adult pricing
        if is_student:
            if is_weekend:
                price = base_price * 0.85  # 15% off
                discount = "Student weekend discount"
            else:
                price = base_price * 0.75  # 25% off
                discount = "Student discount"
        else:
            if is_weekend:
                price = base_price * 1.2  # 20% markup
                discount = "Weekend price (no discount)"
            else:
                price = base_price
                discount = "Regular price"
    
    return price, discount

# Test different scenarios
scenarios = [
    (10, False, False, "Child weekday"),
    (10, False, True, "Child weekend"),
    (25, True, False, "Adult student weekday"),
    (25, False, True, "Adult weekend"),
    (70, False, False, "Senior weekday"),
]

for age, is_student, is_weekend, description in scenarios:
    price, discount = calculate_ticket_price(age, is_student, is_weekend)
    print(f"{description}:")
    print(f"  Age: {age}, Student: {is_student}, Weekend: {is_weekend}")
    print(f"  Price: ${price:.2f} ({discount})\n")

# Real-world Example: Grade Calculator
print("=" * 50)
print("REAL-WORLD EXAMPLE: GRADE CALCULATOR")

def calculate_final_grade(exam_score, project_score, attendance_rate):
    """Calculate final grade with multiple criteria"""
    if exam_score >= 90:
        if project_score >= 90:
            if attendance_rate >= 90:
                grade = "A+"
                comment = "Excellent work!"
            else:
                grade = "A"
                comment = "Great work, improve attendance"
        else:
            if attendance_rate >= 90:
                grade = "A-"
                comment = "Good, improve project work"
            else:
                grade = "B+"
                comment = "Good exam, but improve project and attendance"
    elif exam_score >= 80:
        if project_score >= 80:
            if attendance_rate >= 80:
                grade = "B+"
                comment = "Good overall performance"
            else:
                grade = "B"
                comment = "Good work, better attendance needed"
        else:
            grade = "B-"
            comment = "Improve project scores"
    elif exam_score >= 70:
        if project_score >= 70 and attendance_rate >= 70:
            grade = "C+"
            comment = "Satisfactory, room for improvement"
        else:
            grade = "C"
            comment = "Need significant improvement"
    else:
        grade = "F"
        comment = "Failed - retake required"
    
    return grade, comment

# Test students
students = [
    ("Alice", 95, 95, 95),
    ("Bob", 92, 88, 85),
    ("Charlie", 85, 85, 85),
    ("David", 75, 70, 75),
    ("Eve", 65, 60, 55),
]

for name, exam, project, attendance in students:
    grade, comment = calculate_final_grade(exam, project, attendance)
    print(f"{name}:")
    print(f"  Exam: {exam}, Project: {project}, Attendance: {attendance}%")
    print(f"  Final Grade: {grade}")
    print(f"  Comment: {comment}\n")

# Avoiding Deep Nesting - Better Approach
print("=" * 50)
print("AVOIDING DEEP NESTING:")
print("Instead of deep nesting, use early returns or simplify logic\n")

# Bad: Deep nesting
def check_eligibility_bad(age, income, credit_score, employment):
    """Bad example with deep nesting"""
    if age >= 18:
        if income >= 30000:
            if credit_score >= 600:
                if employment == "full-time":
                    return "Approved"
                else:
                    return "Denied: Employment"
            else:
                return "Denied: Credit score"
        else:
            return "Denied: Income"
    else:
        return "Denied: Age"

# Good: Early returns
def check_eligibility_good(age, income, credit_score, employment):
    """Better example with early returns"""
    if age < 18:
        return "Denied: Age"
    
    if income < 30000:
        return "Denied: Income"
    
    if credit_score < 600:
        return "Denied: Credit score"
    
    if employment != "full-time":
        return "Denied: Employment"
    
    return "Approved"

print("Testing loan eligibility:")
result1 = check_eligibility_good(25, 40000, 650, "full-time")
print(f"Applicant 1: {result1}")

result2 = check_eligibility_good(25, 25000, 650, "full-time")
print(f"Applicant 2: {result2}")

result3 = check_eligibility_good(16, 40000, 650, "full-time")
print(f"Applicant 3: {result3}")

# Real-world Example: Shopping Cart Discount
print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: SHOPPING CART DISCOUNT")

def calculate_discount(total_amount, is_member, has_coupon, is_first_purchase):
    """Calculate discount with multiple nested conditions"""
    discount = 0
    
    if is_member:
        discount = 10  # 10% member discount
        
        if total_amount > 100:
            discount = 15  # 15% for members spending over $100
            
            if has_coupon:
                discount = 20  # 20% for members with coupon over $100
        
        if is_first_purchase:
            discount += 5  # Additional 5% for first purchase
    else:
        # Non-member
        if has_coupon:
            discount = 5  # 5% coupon discount
            
            if total_amount > 150:
                discount = 10  # 10% for large purchases
    
    max_discount = min(discount, 30)  # Cap at 30%
    final_amount = total_amount * (1 - max_discount / 100)
    
    return final_amount, max_discount

# Test shopping scenarios
carts = [
    (120, True, True, True, "Member, first purchase, coupon, $120"),
    (80, True, False, False, "Member, $80, no extras"),
    (200, False, True, False, "Non-member, coupon, $200"),
    (50, False, False, False, "Non-member, $50, no extras"),
]

for amount, member, coupon, first, description in carts:
    final, discount = calculate_discount(amount, member, coupon, first)
    print(f"{description}:")
    print(f"  Original: ${amount:.2f}")
    print(f"  Discount: {discount}%")
    print(f"  Final: ${final:.2f}\n")

# Practice Exercises:
print("=" * 50)
print("--- EXERCISES ---")
print("1. Create a nested condition for a restaurant booking system")
print("   (check date, time, party size, special requirements)")
print("2. Build a job application filter with multiple criteria")
print("   (education, experience, skills, location)")
print("3. Make a shipping cost calculator based on:")
print("   (weight, distance, express shipping, insurance)")
print("4. Design a movie rating system considering:")
print("   (age, parental consent, movie rating, time of day)")