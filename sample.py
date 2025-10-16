class student:
    marks=100
    def sample(self,name,age):
        print(f"My name is {name} and my age is {age}")
s1=student()
print(s1.marks)
s1.sample("ramya",20)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self,address):
        print(f"My name is {self.name} and my age is {self.age} and my address is {address}")
s1=student("ram",30)
s1.sample("kkd")


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_funct1(self):
        print(f"My name is {self.name}")
    def my_funct2(self):
        print(f"My age is {self.age} ")
s1=student("nikhi",20)
s1.my_funct1()
s1.my_funct2()
