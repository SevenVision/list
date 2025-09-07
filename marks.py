# Step 1: Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

# Step 2: Ask the user for a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve marks if found, else show message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Sorry, no record found for {name}.")
