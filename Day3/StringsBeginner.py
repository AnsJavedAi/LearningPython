# Print the first and last character of your name.
name = input("Enter your name: ")
first_character = name[0]
last_character = name[-1]
print("First character:", first_character)
print("Last character:", last_character)

# Print the length of your name.
name_length = len(name)
print("Length of your name:", name_length)

# Convert your name to uppercase.
uppercase_name = name.upper()
print("Uppercase name:", uppercase_name)

# Convert it to lowercase.
lowercase_name = name.lower()
print("Lowercase name:", lowercase_name)

# Reverse your name.
reversed_name = name[::-1]
print("Reversed name:", reversed_name)
