# Combined Program: Even/Odd Check + Sum from 1 to 50

# --- Task 1: Check if a Number is Even or Odd ---
print("=== Task 1: Check if a Number is Even or Odd ===")

# Take integer input from the user
num = int(input("Enter a number: "))

# Check even or odd using if-else
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

print("\n=== Task 2: Sum of Integers from 1 to 50 ===")

# --- Task 2: Sum of Integers from 1 to 50 Using a Loop ---
total = 0

# Use for loop to iterate and calculate sum
for i in range(1, 51):
    total += i

# Display the final sum
print("The sum of numbers from 1 to 50 is:", total)
