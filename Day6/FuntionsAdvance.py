# Create a recursive factorial function.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial:", factorial(5))

# Create a recursive Fibonacci function.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci:", fibonacci(6))

# Create a function using *args.
def add_all(*args):
    return sum(args)
print("Sum:", add_all(10, 20, 30, 40))

# Create a function using **kwargs.
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)
student_info(name="Ali", age=20, city="Lahore")

# Create a lambda function for cube.
cube = lambda x: x ** 3
print("Cube:", cube(4))