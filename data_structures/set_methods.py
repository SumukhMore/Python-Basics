collection = set()
collection.add(1)

collection.add(2)

collection.add(2)  # Duplicate, will be ignored

collection.add("Sumukh") # Adding a string

collection.add((3, 4)) # Adding a tuple

collection.remove(1) # Remove element 1

collection.clear() # Clear all elements

print(collection)


collection2 = {"Python", "Java", "HTML", "C++"}
print(collection2.pop()) # Remove and return an arbitrary element


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))  # Union of two sets

print(set1.intersection(set2))  # Intersection of two sets

print(set1.difference(set2))  # Difference of two sets

print(set1.symmetric_difference(set2))  # Symmetric difference of two sets