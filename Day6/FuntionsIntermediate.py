# Return the largest of three numbers.
def largest(a, b, c):
    return max(a, b, c)
print("Largest:", largest(10, 25, 15))

# Calculate factorial using a function.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial:", factorial(5))

# Return a reversed string.
def reverse_string(text):
    return text[::-1]
print("Reversed String:", reverse_string("Python"))

# Count vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print("Vowel Count:", count_vowels("Programming"))

# Find the average of a list.
def average(numbers):
    return sum(numbers) / len(numbers)
print("Average:", average([10, 20, 30, 40, 50]))