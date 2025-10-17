class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self,address):
        print(f"My name is {self.name} and my age is {self.age} and my address is {address}")
s1=student("ram",30)
s1.sample("kkd")