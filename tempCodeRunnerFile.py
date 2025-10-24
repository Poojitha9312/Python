class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age  
    def deleteDetails(self):
        del self.name
p1=Person("Ram",30)
print(p1.__dict__)

p1.deleteDetails()
print(p1.__dict__)
