# Create a dictionary for a student
student = {
    "name": "Alice",
    "age": 16,
    "marks": 85
}

# Print the student's name
print("Student Name:", student["name"])

# Add a city
student["city"] = "New York"

# Update marks
student["marks"] = 92

# Remove age
del student["age"]

# Print the final dictionary
print("Updated Student Dictionary:", student)