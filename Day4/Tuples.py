# Create a tuple of five numbers.
num_tuple=(1,2,3,4,5)
print("Create a tuple of five numbers.",num_tuple)

# Print the last element.
print("Print the last element.",num_tuple[-1])

# Unpack the tuple into variables.
num1,num2,num3,num4,num5=num_tuple
print("Unpack the tuple into variables.")
print("Variable 1: ",num1)
print("Variable 2: ",num2)
print("Variable 3: ",num3)
print("Variable 4: ",num4)
print("Variable 5: ",num5)

# Count how many times 5 appears.
count_of_5=num_tuple.count(5)
print("# Count how many times 5 appears:",count_of_5)

# Slice the tuple.
sliced_tuple=num_tuple[1:3]
print("Slice the tuple:",sliced_tuple)
