class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self):
        print(f" my name is {self.name} and my age is {self.age}")
s1=student("prasanna",18)
print(student.__dict__)
