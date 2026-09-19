# A class attribute is an attribute defined directly inside a class. 
# It belongs to the class and can be accessed through the class or, if not shadowed, through its instaces.  
from unicodedata import name

from django.db.models import When


class Student:
    school = "ABC School"
print(Student.school)  # Output: ABC School
# Here, school is a class attribute. It is shared by all instances of the Student class.


#How to acces the class attribute inside the class method
class Student:
    school="ABC School"
    def show_school(self):
        print(f"School: {self.school}")
s1=Student()
s1.show_school()  # Output: School: ABC School

# Better Way: cls with @classmethod

# Agar method specifically class ke data ke saath kaam kar raha hai, then @classmethod use karna better hai.
class Student:
    school="ABC SCHOOL"
    @classmethod
    def show_school(cls):
        print(f"school:{cls.school}")
Student.show_school()  # Output: school: ABC SCHOOL`

# cls is the conventional name for the class reference automatically passed to a class method.
# @classmethod
# def show_school(cls):

# When you call:

# Student.show_school()

# Python conceptually provides:

# cls → Student

# So:

# cls.school

# is effectively:

# Student.school
# Student.show_school()
#         ↓
#      cls = Student
#         ↓
#     cls.school
#         ↓
#  Student.school
