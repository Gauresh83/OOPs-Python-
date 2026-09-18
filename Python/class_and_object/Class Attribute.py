# A class attribute is an attribute defined directly inside a class. 
# It belongs to the class and can be accessed through the class or, if not shadowed, through its instaces.  
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