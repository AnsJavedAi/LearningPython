# Create a dictionary for a student
student = {
    "name": "Alice",
    "marks": 92,
    "city": "New York"
}

# Print all keys
print("Keys:", student.keys())

# Print all values
print("Values:", student.values())

# Print keys and values together
print("Keys and Values:")
for key, value in student.items():
    print(key, ":", value)

# Count total items
print("Total items:", len(student))

# Check if "marks" exists
if "marks" in student:
    print("'marks' exists in the dictionary.")
else:
    print("'marks' does not exist in the dictionary.")