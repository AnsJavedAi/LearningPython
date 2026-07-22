# Create a function that prints your name.
def print_name(name):
    print("Your Name", name)
print_name("Ans")

# Create a function that adds two numbers.
def add_numbers(a, b):
    return a + b
print("Sum:", add_numbers(10, 5))

# Create a function that returns the square of a number.
def square(num):
    return num * num
print("Square:", square(6))

#Create a function that checks even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("12 is", check_even_odd(12))
print("7 is", check_even_odd(7))

# Create a function with a default parameter.
def greet(name="Guest"):
    print("Hello,", name)
greet()          
greet("Alice")