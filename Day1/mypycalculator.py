print("Hello to a simple calculator!")
print("Enter two numbers and an operator (+, -, *, /, %, **,//):")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %, **,//): ")

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} {operator} {num2} is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} {operator} {num2} is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} {operator} {num2} is: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"The result of {num1} {operator} {num2} is: {result}")
elif operator == "%":
    result = num1 % num2
    print(f"The result of {num1} {operator} {num2} is: {result}")
elif operator == "**":
    result = num1 ** num2
    print(f"The result of {num1} {operator} {num2} is: {result}")
elif operator == "//":
    result = num1 // num2
    print(f"The result of {num1} {operator} {num2} is: {result}")
else:
    print("Invalid operator!")

