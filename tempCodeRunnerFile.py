class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @classmethod
    def modify_age(cls, x):  # class method (uses cls)
        print(f'Modified Age: {x}')

s1 = Student("Ram", 30)
Staff.modify_age(s1.age)