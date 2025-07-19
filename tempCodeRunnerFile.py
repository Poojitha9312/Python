class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        print("str method executes")
        return f" My name is {self.name} and my age is {self.age}"
    def __repr__(self):
        print("repr method executes")
        return f"My name is {self.name} and my age is {self.age}"
s1=student("snehi",15)
print(s1)
s2=student("ruchi",15)
print(s2)
s3=[(student("ram",30),student("krishna",29))]
print(s3)