# Combined Program: Basic Operations + Personalized Greeting

# --- Task 1: Basic Mathematical Operations ---
print("=== Task 1: Basic Mathematical Operations ===")

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

print("\n=== Task 2: Personalized Greeting ===")

# --- Task 2: Personalized Greeting ---
# Take name inputs from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate full name
full_name = first_name + " " + last_name

# Display personalized greeting
print("Hello,", full_name + "! Welcome to the Python program.")
