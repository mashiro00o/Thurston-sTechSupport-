# Creating a dictionary
my_dict = {'apple': 5, 'banana': 10, 'orange': 7}

# Accessing values using keys
print(my_dict['banana'])  # Output: 10

# Adding a new key-value pair
my_dict['grape'] = 3

# Modifying a value
my_dict['apple'] = 8

# Removing a key-value pair
del my_dict['orange']

# Iterating through a dictionary
for key, value in my_dict.items():
    print(key, ':', value)
