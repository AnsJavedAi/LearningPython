# Count vowels in a string.
string = input("Enter a string: ")
lowercase_string = string.lower()
a_count = lowercase_string.count('a')
e_count = lowercase_string.count('e')
i_count = lowercase_string.count('i')
o_count = lowercase_string.count('o')
u_count = lowercase_string.count('u')
total_vowels = a_count + e_count + i_count + o_count + u_count
print("Number of vowels in the string:", total_vowels)

# Count words in a sentence.
sentence = input("Enter a sentence: ")
words= sentence.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)

# Replace every space with _.
sentence_with_underscores = sentence.replace(" ", "_")
print("Sentence with spaces replaced by underscores:", sentence_with_underscores)

# Check whether a string starts with "Py".
string1 = input("Enter a string: ")
if string1.startswith("Py"):
    print("The string starts with 'Py'.")
else:
    print("The string does not start with 'Py'.")
    
# Check whether a string contains "AI".
string2 = input("Enter a string: ")
if "AI" in string2:
    print("The string contains 'AI'.")
else:
    print("The string does not contain 'AI'.")
    