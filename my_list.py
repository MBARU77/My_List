list = [10, 20, 30, 40]
print(list)
list.insert(1, 15)  # Insert 15 at the second position (index 1)
print(list)
list.extend([50, 60, 70])  # Extend the list with [50, 60, 70]
print(list)
list.pop()  # Remove the last element
print(list)
list.sort()  # Sort the list in ascending order
print(list)
index_of_30 = list.index(30)  # Find the index of the value 30
print(f"The index of 30 is: {index_of_30}")