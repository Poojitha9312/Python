class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @classmethod
    def modify_student(cls, x):  # class method
        x.age = 31
        print("Student age modified by class method in Staff")

s1 = Student("Ram", 30)
s1.Details()

Staff.modify_student(s1)  # class method can be called from class
s1.Details()