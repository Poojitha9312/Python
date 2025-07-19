class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"
    def __repr__(self):
        return f"My name is {self.name} and my age is {self.age}"
    
s1=student("snehi",15)
print(s1)
