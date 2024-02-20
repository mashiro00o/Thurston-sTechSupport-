# Create an empty array
my_array = []

# Create - Adding elements to the array
my_array.append(1)
my_array.append(2)
my_array.append(3)
print(my_array) # Output array after adding elements

# Read - Accessing elements of the array
print(my_array[1]) # Output element at index 1

# Update - Modifying elements of the array
my_array[1] = 10
print(my_array) # Output array after updating element at index 1

# Delete - Removing elements from the array
my_array.pop()  # Remove the last element
print(my_array) # Output array after deleting the last element

# Remove the element at index 0
del my_array[0]
print(my_array) # Output array after deleting the first element

# output
# [1, 2, 3]
# 2
# [1, 10, 3]
# [1, 10]
# [10]
