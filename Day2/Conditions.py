# Check whether a number is positive, negative, or zero.
num=int(input("Enter a number: "))
if num>0:
    print("The number is positive.")
elif num<0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Check if a student passed (marks ≥ 50).
student_marks=int(input("Enter your marks: "))
if student_marks>=50:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")

# Determine whether a number is even or odd.
num_=int(input("Enter a number: "))
if num_%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

# Check whether a person is eligible to vote.
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Find the largest of three numbers.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num2<=num1>=num3:
    print("The largest number is:", num1)
elif num1<=num2>=num3:
    print("The largest number is:", num2)
elif num1<=num3>=num2:
    print("The largest number is:", num3)
else:
    print("No largest number found.")

# Determine the grade based on marks.
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade: A+")
elif marks>=80:
    print("Grade: A")
elif marks>=70:
    print("Grade: B")
elif marks>=60:
    print("Grade: C")
elif marks>=50:
    print("Grade: D")
else:
    print("Grade: F")

# Check whether a character is a vowel or consonant.
char=input("Enter a character: ")
if char in 'aeiouAEIOU':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

# Use nested if to check age and ID for entry.
user_age=int(input("Enter your age: "))
user_id=input("Do you have an ID? (yes/no): ")
if user_age>=18:
    if user_id.lower()=="yes":
        print("You are allowed entry.")
    else:
        print("You need an ID for entry.")
else:
    print("You are not allowed entry due to age restrictions.")

# Rewrite an if-else block using a ternary expression.
number=int(input("Enter a number: "))
result="Even" if number%2==0 else "Odd"
print("The number is:", result)

# Build a simple login system that checks a username and password.
username=input("Enter your username: ")
password=input("Enter your password: ")
if username=="AnsJavedAi" and password=="password123":
    print("Login successful.")
else:
    print("Login failed. Invalid username or password.")
