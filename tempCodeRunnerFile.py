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