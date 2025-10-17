# Combined Program: Factorial Function + Math Module Calculations

# --- Task 1: Calculate Factorial Using a Function ---
print("=== Task 1: Calculate Factorial Using a Function ===")

# Define a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
num = int(input("Enter a number: "))

# Call the function and display the result
print("The factorial of", num, "is:", factorial(num))


# --- Task 2: Using the Math Module for Calculations ---
print("\n=== Task 2: Using the Math Module for Calculations ===")

import math

# Take input from the user
x = float(input("Enter a number: "))

# Perform calculations using math module
sqrt_val = math.sqrt(x)
log_val = math.log(x)
sin_val = math.sin(x)

# Display results
print("Square root:", sqrt_val)
print("Logarithm:", log_val)
print("Sine:", sin_val)
