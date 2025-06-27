class Person:
    def __init__(self,name,age,rollno):
        self.name=name 
        self.age=age 
        self.rollno=rollno 
p1=Person("Ram",30,32)
print(p1.__dict__)

del p1.rollno
print(p1.__dict__)
   