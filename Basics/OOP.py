class Person:  # Defines a parent/super class called Person
    def __init__(self, pname, page):  # Constructor method to initialize attributes
        self.name = pname  # Assigns the name attribute
        self.age = page  # Assigns the age attribute

    def get_name(self):  # Method to retrieve the name attribute
        return self.name

    def get_age(self):  # Method to retrieve the age attribute
        return self.age

    def set_age(self, new_age):  # Method to update the age attribute
        self.age = new_age

    def display(self):  # Method to display the name and age attributes
        print(self.name)
        print(self.age)


class Student(Person):  # Defines a child/sub class called Student, inheriting from Person
    def __init__(self, pname, page, scca):  # Constructor method for Student class
        super().__init__(pname, page)  # Inherits and initializes attributes from Person
        self.cca = scca  # Additional attribute specific to Student

    def get_cca(self):  # Method to retrieve the co-curricular activity (CCA) attribute
        return self.cca

    def display(self):  # Method to display name, age, and CCA
        super().display()  # Calls the display method of the parent class
        print(self.cca)


class Staff(Person):  # Defines a child/sub class called Staff, inheriting from Person
    def __init__(self, pname, page, sdept):  # Constructor method for Staff class
        super().__init__(pname, page)  # Inherits and initializes attributes from Person
        self.dept = sdept  # Additional attribute specific to Staff

    def get_dept(self):  # Method to retrieve the department attribute
        return self.dept

    def display(self):  # Method to display name, age, and department
        super().display()  # Calls the display method of the parent class
        print(self.dept)

# main
MrTan = Person("Husband", 18)  # Creates an instance of Person
MsLim = Person("Wife", 15)  # Creates another instance of Person
John = Student("Son", 14, "Visual arts")  # Creates an instance of Student
MrNg = Staff("Teacher", 120, "Math")  # Creates an instance of Staff
people = [MrTan, MsLim, John, MrNg]  # Stores instances in a list

# Polymorphism
for person in people:  # Iterates through each person in the list
    person.display()  # Calls the display method, which varies based on the object type

# output
# Husband
# 18
# Wife
# 15
# Son
# 14
# Visual arts
# Teacher
# 120
# Math
