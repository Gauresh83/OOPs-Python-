# # What is a Class?

# # A class is a blueprint/template for creating objects.
# ->pass
# # pass is used as a placeholder when we want to leave a block of code empty without causing a syntax error.

from turtle import write


class Student:
    pass

print(type(Student))
# output:
# <class 'type'>

# Important interview point:

# A class itself is also an object in Python.

# More precisely, a class is an instance of a metaclass, normally type.

# What is an Object?

# An object is an instance of a class.

class Student:
    pass

student1 = Student() #Here, student1 is an object of the class Student. It is an instance of the class and can have its own attributes and methods.

print(student1)

# output:
# <__main__.Student object at 0x0000018B66A786E0>

print(isinstance(student1, Student)) # We can use the isinstance() function to check if an object is an instance of a specific class.
# output:
# True

# What actually happens when we do Student()?

# This is VERY important for interviews.

# When you write:

# s1 = Student()

# Python doesn't simply "run the class."

# Conceptually, object creation involves:

# Student()
#    ↓
# Python creates a new object
#    ↓
# __new__()
#    ↓
# __init__()
#    ↓
# object returned
#    ↓
# student1 points/references to it

# So:

# __new__

# Responsible for creating/allocating the object.

# __init__

# Responsible for initializing the already-created object.

class Student:

    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")

s1 = Student()

# Output:

# Creating object
# Initializing object

# Interview question:

# What is the difference between __new__ and __init__?

# Answer:

# __new__ creates the object, while __init__ initializes the object after it has been created.

# Usually, we only need to write __init__.
# What is __init__?

# Example:

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating object:

s1 = Student("Rahul", 21)

# Internally:

# Student("Rahul", 21)
#        ↓
# __new__ creates object
#        ↓
# __init__(s1, "Rahul", 21)
#        ↓
# self.name = "Rahul"
# self.age = 21

# So s1 now contains:

# s1
#  ↓
# ┌─────────────────┐
# │ name = "Rahul"  │
# │ age = 21        │
# └─────────────────┘
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
s1=Student("Rahul", 21)
s2=Student("Rohit", 22)
s1.introduce()
s2.introduce()