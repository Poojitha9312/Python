class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_detail(self):
        print(f"My name is {self.name}")
    def my_detail2(self):
        print(f"My age is {self.age}")

s1=student("nihitha",18)
s1.my_detail()
s1.my_detail2()