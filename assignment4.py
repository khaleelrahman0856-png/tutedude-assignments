# Combined Program: File Reading with Error Handling + File Writing and Appending

# --- Task 1: Read a File and Handle Errors ---
print("=== Task 1: Read a File and Handle Errors ===")

try:
    # Try opening the file
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        # Read and print each line
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    # Handle if file doesn't exist
    print("Error: The file 'sample.txt' is not found.")


# --- Task 2: Write and Append Data to a File ---
print("\n=== Task 2: Write and Append Data to a File ===")

# Take input from user and write to file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Take additional input to append
text_to_append = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Read and display final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
