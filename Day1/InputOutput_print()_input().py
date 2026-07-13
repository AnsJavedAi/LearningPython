name="AnsTheAiEngineer"
age=16
city="Lahore"
print("My name is", name)
print("My age is", age)
print("My city is", city)
print(name, age, city, sep="|")
print(name, end=" ")
print(city)
print("My name is\tAns \nMy age is\t16 \nMy city is \tLahore")
user_name=input("Enter your name: ")
print("Hello", user_name)
a,b=input("Enter two numbers separated by space: ").split()
print("Sum of two numbers:", int(a)+int(b))
c=input("Enter a float number: ")
print("The square of the float number is:", float(c)**2)
num1,num2,num3=map(int,input("Enter three numbers separated by space: ").split())
print("The average of thrsee numbers is:", (num1+num2+num3)/3)
marks=474
per=88
print(f"My marks are {marks} and percentage is {per}%")