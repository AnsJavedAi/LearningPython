# Check if a string is a palindrome.
string3 = input("Enter a string: ")
lowercase_string3 = string3.lower()
reversed_string3 = lowercase_string3[::-1]
if lowercase_string3 == reversed_string3:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Reverse every word in a sentence.
string4 = input("Enter a sentence: ")
sentence_list = string4.split()
print("Reversed every word")
for word in sentence_list:
    reversed_word = word[::-1]
    print(reversed_word, end=" ")

# Count uppercase and lowercase letters separately.
string_5=input("Enter a sentence: ")
no_spaces_str_5=str(string_5.strip())
count_lowercase=0
count_uppercase=0
for letter in no_spaces_str_5:
    if letter==letter.lower():
        count_lowercase+=1
    elif letter==letter.upper():
        count_uppercase+=1
print("Number of Lower case letters: ", count_lowercase)
print("Number of Upper case letters: ", count_uppercase)

# Remove duplicate characters.
string_6=input("Enter a string: ")
string_no_dup=set(string_6)
string_no_duplicate=list(string_no_dup)
str_string=" ".join(string_no_duplicate)
print("Uniques letters",str_string)

# Find the most frequent character.
string_7=input("Enter a string: ")
string_no_dup2=set(string_7)
string_no_duplicate2=list(string_no_dup2)
str_string2=" ".join(string_no_duplicate2)
print("Uniques Char: ", str_string2)
max_count=0
max_char=""
for ch in str_string2:
    count=0
    for char in string_7:
        if ch==char:
            count+=1
        if count>max_count:
            max_count=count
            max_char=ch
print("Frequent char: ", max_char)
print("Frequency: ", max_count)
            

            
            
            