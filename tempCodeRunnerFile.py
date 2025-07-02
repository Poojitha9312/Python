class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(30*'=')
s1=[student("aparna",15),student("kavya",20)]
for student in s1:
    student.sample()