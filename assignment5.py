# Combined Program: Student Marks Dictionary + List Slicing Demonstration

# --- Task 1: Create a Dictionary of Student Marks ---
print("=== Task 1: Create a Dictionary of Student Marks ===")

# Create dictionary of students and marks
student_marks = {
    "John": 85,
    "Alice": 90,
    "Bob": 78,
    "Sara": 92,
    "Tom": 88
}

# Ask user for student name
name = input("Enter the student's name: ")

# Check and display marks
if name in student_marks:
    print(name, "marks:", student_marks[name])
else:
    print("Student was not found.")

# --- Task 2: Demonstrate List Slicing ---
print("\n=== Task 2: Demonstrate List Slicing ===")

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extract first five elements
first_five = numbers[:5]

# Reverse the extracted list
reversed_list = first_five[::-1]

# Display results
print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)
