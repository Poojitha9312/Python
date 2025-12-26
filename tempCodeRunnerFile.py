class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @staticmethod
    def modify_age(x): 
        print(x)

s1=Student("Ram",30)
Staff.modify_age(s1.age)