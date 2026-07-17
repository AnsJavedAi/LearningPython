# Create a list of five fruits.
fruits_list=["Apple","Banana","Mango","Orange","Pinaapple"]
print("Create a list of five fruits.",fruits_list)

# Replace the third fruit.
fruits_list[2]="Dragon Fruit"
print("Replace the third fruit.",fruits_list)

# Append two new fruits.
fruits_list.append("Peach")
fruits_list.append("Cherry")
print("Append two new fruits.",fruits_list)

# Remove one fruit.
fruits_list.remove("Apple")
print("Remove one fruit.",fruits_list)

# Reverse the list.
fruits_list=fruits_list[::-1]
print("Reverse the list.",fruits_list)