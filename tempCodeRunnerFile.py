class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        
class Student(Human):
    def __init__(self,name,age,course,college):
        super().__init__(name,age)
        self.course=course
        self.college=college
    
    def details(self):
        super().details()
        print(f"My COurse is {self.course}")
        print(f"My college is {self.college}")
        
class Employee(Human):
    def __init__(self,name,age,dep,company):
        super().__init__(name,age)
        self.dep=dep
        self.company=company
    
    def details(self):
        super().details()
        print(f"My COurse is {self.dep}")
        print(f"My college is {self.company}")
        
e=Employee("Ram",30,"IT","Wipro")
e.details()
s1=Student("divya",22,"BSC","PRAGATI")
s1.details()