# Pressence check
name = input('Enter name: ')
# Checking if the input stored in 'name' is empty.
if name == '':
    # If the input is empty, this block of code is executed, printing a message indicating an empty input.
    print('Empty input')


# Length check
classroom = input('Enter class: ')
# Checking if the length of the input stored in 'classroom' is not equal to 5.
if len(classroom) != 5:
    # If the length of the input is not equal to 5, this block of code is executed, printing a message indicating no such classroom.
    print('No such classroom')


# Format check (digit)
number = input("Enter a number: ")
# Checking if the input consists of only digits.
if number.isdigit(): 
    # If the input consists of only digits, this block of code is executed, printing a message indicating it's a valid number.
    print("valid number")
else:
    # If the input contains non-digit characters, this block of code is executed, printing a message indicating it's not a number.
    print('not a number')


# Format check (alphabat and number)
user = input('Enter username: ')
# Checking if the input consists of only alphanumeric characters.
if user.isalnum():
    # If the input consists of only alphanumeric characters, this block of code is executed, printing a message indicating it's a valid username.
    print('valid username')
else:
    # If the input contains characters other than alphanumeric characters, this block of code is executed, printing a message indicating the username is not valid.
    print('username not found')


# Format check (alphabat)
name = input('Enter name: ')
# Checking if the input consists of only alphabetic characters.
if name.isalpha():
    # If the input consists of only alphabetic characters, this block of code is executed, printing a message indicating the input is a valid name.
    print('Name found')
else:
    # If the input contains characters other than alphabetic characters, this block of code is executed, printing a message indicating it's not a valid name.
    print('Not a name')


# Range check
age = int(input("Enter age: "))
# Checking if the entered age falls within the range of 16 to 19 (inclusive).
if 16 <= age <= 19:
    # If the age falls within the specified range, this block of code is executed, printing a message indicating it's a valid age.
    print("valid age")
else:
    # If the age does not fall within the specified range, this block of code is executed, printing a message indicating it's not in the specified age category.
    print('not in age category')


# Existence check
# A list of student names.
students = ['John', 'Tom', 'Jane']
# Prompting the user to enter a name and storing the input in the variable 'name'.
name = input('Enter name: ')
# Checking if the entered name exists in the list of students.
if name in students:
    # If the name is found in the list of students, this block of code is executed, printing a message indicating that the name is a student.
    print('is a student')
else:
    # If the name is not found in the list of students, this block of code is executed, printing a message indicating that the name is not a student.
    print('is not a student')
