# Create a set with duplicate values.
set={1,2,2,3,4,4,5}
print("Set is :",set)

# Add a new element.
set.add(9)
print("Add a new element.",set)

# Remove an element safely.
set.discard(3)
print("Remove an element safely.",set)

# Find the union of two sets.
set_2={6,7,8,9,2}
add_sets= set|set_2
print("Union of two sets:",add_sets)

# Find the intersection of two sets.
intersection_sets= set&set_2
print("Intersection of two sets.",intersection_sets)
