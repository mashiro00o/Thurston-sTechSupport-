# Create an empty array
my_array = []

# Create - Adding elements to the array
my_array.append(1)
my_array.append(2)
my_array.append(3)
print(my_array) # Array after adding elements: [1, 2, 3]

# Read - Accessing elements of the array
print(my_array[1]) # Element at index 1: 2

# Update - Modifying elements of the array
my_array[1] = 10
print(my_array) # Array after updating element at index 1: [1, 10, 3]

# Delete - Removing elements from the array
my_array.pop()  # Remove the last element
print(my_array) # Array after deleting the last element: [1, 10]

# Remove the element at index 0
del my_array[0]
print(my_array) # Array after deleting the first element: [10]

# output
# [1, 2, 3]
# 2
# [1, 10, 3]
# [1, 10]
# [10]
