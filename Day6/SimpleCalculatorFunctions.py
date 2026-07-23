# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a // b

def square_root(a):
    if a < 0:
        return "Error! Square root of a negative number is not possible."
    return a ** 0.5

def factorial(a):
    if a < 0:
        return "Error! Factorial is not defined for negative numbers."

    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

def percentage(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return (a / b) * 100


# Main Program
while True:
    print('''CALCULATOR
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
    6. Power
    7. Floor Division
    8. Square Root
    9. Factorial
    10. Percentage
    11. Exit''')

    choice = int(input("Enter your choice (1-11): "))

    if choice == 11:
        print("Thank you for using the calculator!")
        break

    elif choice == 8:
        num = float(input("Enter a number: "))
        print("Result =", square_root(num))

    elif choice == 9:
        num = int(input("Enter a number: "))
        print("Result =", factorial(num))

    elif 1 <= choice <= 7 or choice == 10:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(num1, num2))
        elif choice == 2:
            print("Result =", subtract(num1, num2))
        elif choice == 3:
            print("Result =", multiply(num1, num2))
        elif choice == 4:
            print("Result =", divide(num1, num2))
        elif choice == 5:
            print("Result =", modulus(num1, num2))
        elif choice == 6:
            print("Result =", power(num1, num2))
        elif choice == 7:
            print("Result =", floor_division(num1, num2))
        elif choice == 10:
            print(f"{num1} is {percentage(num1, num2):.2f}% of {num2}")

    else:
        print("Invalid choice! Please try again.")
