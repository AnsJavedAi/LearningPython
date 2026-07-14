# Calculate the sum of numbers from 1 to 100.
sum=0
for i in range(1,101):
    sum=sum+i
print("The sum of numbers from 1 to 100 is:", sum)

# Find the factorial of a number.
num=int(input("Enter a number: "))
factorial=1
i=1
while i<=num:
    factorial=factorial*i
    i=i+1
print("The factorial of", num, "is:", factorial)

# Count vowels in a string.
str=input("Enter a string: ")
vowels="aeiouAEIOU"
count=0
for v in vowels:
    for i in str:
        if i==v:
            count=count+1
print("The number of vowels in the string is:", count)

# Reverse a string using a loop.
str = input("Enter a string: ")
reversed_str = ""
for i in str:
    reversed_str = i + reversed_str
print("The reversed string is:", reversed_str)

# Find the largest number in a list.
numbers=list(map(int, input("Enter numbers separated by spaces: ").split()))
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print("The largest number in the list is:", largest)
print(numbers)
