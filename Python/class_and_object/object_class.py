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
# Python internally behaves approximately like:
# Student.introduce(s1)
# Student.introduce(s2)

# s1.introduce()
#       ↓
# self = s1

# s2.introduce()
#       ↓
# self = s2

# That's why self.name means:

# "Get the name belonging to this particular object."

# self is NOT a keyword

# This is a common interviewer question.

# You can technically write:

class Student:

    def introduce(this):
        print(this)

# and:

s = Student()
s.introduce()

# It works.

# But convention says use:

# self

# So:

# self is a conventional parameter name representing the current instance. It is not a Python keyword.


#Instance Variables
# self.name
# self.age
#            Student class
#                   │
#         ┌─────────┴─────────┐
#         ↓                   ↓

#        s1                  s2
#  ┌─────────────┐      ┌─────────────┐
#  │ name Rahul  │      │ name Amit   │
#  │ age 20      │      │ age 22      │
#  └─────────────┘      └─────────────┘

# Each object has its own instance data.
# Class Variables

# Now:

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

# Here:

# school

# is a class variable.

# It belongs to the class rather than being independently created for every instance.

#              Student
#                 │
#           school = ABC
#                 │
#         ┌───────┴───────┐
#         ↓               ↓
#        s1              s2
#  name=Rahul        name=Amit

# You can access:

# Student.school
# s1.school
# s2.school
# 10. How Python actually finds s1.school

# This is where interview-level understanding starts.

# Suppose:

class Student:
    school = "ABC"

s1 = Student()

# Then:

# s1.school

# Python approximately searches:

# Does s1 have "school"?
#        ↓
#       NO
#        ↓
# Does Student have "school"?
#        ↓
#       YES
#        ↓
# Return "ABC"

# This is related to Python's:

# Attribute Lookup → MRO → inheritance

# We'll go deeply into this.

# 11. The __dict__ — VERY IMPORTANT

# Python objects often have a dictionary containing their instance attributes.

# Example:

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 21)

print(s1.__dict__)

# Output:

# {
#     'name': 'Rahul',
#     'age': 21
# }

# So:

# self.name = "Rahul"

# roughly means that the object's attribute storage gets an entry for name.

# This is one of the most useful things to understand internally.

# 12. Class also has __dict__

# Try:

print(Student.__dict__)

# You'll see a mapping containing things like:

# school
# __init__
# __module__
# __dict__
# __weakref__
# __doc__

# So Python classes themselves store their attributes/methods.

# 13. A method is basically a function stored in a class

# Example:

class Student:

    def study(self):
        print("Studying")

# The function study is stored inside the class.

# Student
#    │
#    ├── study
#    ├── __init__
#    └── ...

# When you do:

# s1.study()

# Python finds study on the class and binds the object s1 to it.

# That's why:

# s1.study()

# is conceptually related to:

# Student.study(s1)

# This mechanism is called method binding and is implemented using Python's descriptor protocol.

# Don't worry—we'll unpack descriptors later.

# 🔥 The first 5-minute mental model

# Remember this:

#                     CLASS
#               ┌────────────────┐
#               │ Student        │
#               │                │
#               │ class variables│
#               │ methods        │
#               └───────┬────────┘
#                       │
#               creates objects
#                 ┌─────┴─────┐
#                 ↓           ↓
#               OBJECT       OBJECT
#                 s1           s2
#              ┌───────┐    ┌───────┐
#              │name   │    │name   │
#              │age    │    │age    │
#              └───────┘    └───────┘

# And:

# s1 = Student()

# roughly:

# Student()
#    ↓
# __new__()
#    ↓
# object created
#    ↓
# __init__()
#    ↓
# object initialized
#    ↓
# s1 references object

# And:

# s1.method()

# roughly:

# s1.method()
#     ↓
# attribute lookup
#     ↓
# find method in class
#     ↓
# bind s1 as self
#     ↓
# method executes