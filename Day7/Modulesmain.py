import math
import random
import myaddmodule

# Print the value of pi
print("Value of π:", math.pi)

# Generate a random number from 1 to 100
random_number = random.randint(1, 100)
print("Random number:", random_number)

# Use the add() function from the custom module
result = myaddmodule.add(10, 20)
print("Sum:", result)
