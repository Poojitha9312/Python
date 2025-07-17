class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"My name is {name} and my age is {age}")
    def sample(self,address):
        print(f" my address is {address}")
s1=student("ram",30)
s1.sample("KKD")