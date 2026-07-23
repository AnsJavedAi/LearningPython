# Custom Exception Class
class UnderAgeError(Exception):
    """Raised when the user's age is less than 18."""
    pass


# Handle division by zero
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Handle invalid integer input
try:
    number = int(input("\nEnter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Error: Invalid integer input.")

# Handle a missing file
try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")


# Raise a custom ValueError if age is less than 18
try:
    age = int(input("\nEnter your age: "))
    if age < 18:
        raise ValueError("Age must be at least 18.")
    print("Access granted.")
except ValueError as e:
    print("Error:", e)


# Create and use your own custom exception class
try:
    age = int(input("\nEnter your age again: "))
    if age < 18:
        raise UnderAgeError("You must be 18 or older.")
    print("Welcome!")
except UnderAgeError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter a valid integer.")
