# Reading from a file
file = open('data.txt', 'r')  # Open 'data.txt' file in read mode
line = file.readline()  # Read a single line
print(line)  
line = file.readline()  # Read the next line
print(line)  
file.close()  # Close the file

# Reading the entire content of a file
with open('data.txt', 'r') as file:  # Open 'data.txt' file
  text = file.read()  # Read the entire content of the file
  print(text)  # Print the content

# Writing to a file
file = open('newdata.txt', 'w')  # Open 'newdata.txt' file in write mode
file.write('123\n')  # Write '123' followed by a newline to the file
file.close()  # Close the file

with open('newdata.txt', 'w') as file:  # Open 'newdata.txt' file in write mode
  file.write('12345\n')  # Write '12345' followed by a newline to the file

# Appending to a file
file = open('newdata.txt', 'a')  # Open 'newdata.txt' file in append mode
file.write('xyz\n')  # Append 'xyz' followed by a newline to the file
file.close()  # Close the file

with open('newdata.txt', 'a') as file:  # Open 'newdata.txt' file in append mode
  file.write('xyz\n')  # Append 'xyz' followed by a newline to the file
