# Create a nested dictionary.
students = {
    "student1":{"name": "Alice",
    "marks": 92,
    "city": "New York"}
    ,
    "student2":{"name": "Ali",
    "marks": 42,
    "city": "Lahore"}
    ,
    "student3":{"name": "Alina",
    "marks": 82,
    "city": "London"}
}
print(students)

# Build a phone book.
phone_book = {
    "Alice": "1234567890",
    "Ali": "9876543210",
    "Alina": "1122334455"
}
name=input("Enter name for Phone")
phone=phone_book.get(name,"Not Found")
print(phone)

# Count word frequencies in a sentence
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# Merge two dictionaries.
merged_dict=students["student1"].update(phone_book)
print("Merged book:", merged_dict)

# Create a dictionary using comprehension.
cubes={x:x**3 for x in range(1,6)}
print(cubes)

