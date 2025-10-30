class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    def modify(self, x):  # instance method (requires self)
        print(f'Modified Age: {x}')

s1 = Student("Ram", 30)
staff1 = Staff()  # creating an instance of Staff
staff1.modify(s1.age) 