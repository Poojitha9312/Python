class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("priya",20)
print(s1.__dict__)

class student:
    marks=100
    def sample(self):
        print("Hello world")
s1=student()
print(student.__dict__)