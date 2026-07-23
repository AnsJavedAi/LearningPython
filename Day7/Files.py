# Create a text file and write your name Append age
file = open("studentfile.txt", "w")
file.write("Name: Ali\n")    
file.close()

file = open("studentfile.txt", "a")
file.write("Age: 20\n")       
file.close()


# Read the file line by line
file = open("studentfile.txt", "r")

print("File Contents:")
for line in file:
    print(line.strip())

file.close()

# Count the number of lines
file = open("studentfile.txt", "r")
lines = file.readlines()
print("\nTotal number of lines:", len(lines))
file.close()
