class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        print("here __str__method will executes") 
        return f"My name is {self.name} and My age is {self.age}"
    def __repr__(self):
        print("here __repr__method will executes")
        return f" My name is {self.name} and my age is {self.age}"
s1=student("snehi",15)
s2=student("vasu",30)
print(s1)
print(s2)

s3=[(student("kavya",25),student("gopal",30))]
print(s3)