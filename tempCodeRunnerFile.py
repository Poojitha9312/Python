lass student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"My name is {self.name} and my age is {self.age}"
s1=student("prasanna",18)
print(s1)