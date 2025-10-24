class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("pavani",21)
print(s1.__dict__)


class student:
    def __init__(self,name):
        self.name=name
s1=student("pavani")
print(s1.__dict__)
s1.age=18
s1.address="kkd"
s1.rollno=24
print(s1.__dict__)