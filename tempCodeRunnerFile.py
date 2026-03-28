class employee:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def sample(self):
        print(f"My name is {self.__name}  and my age is {self.age}")
        
e1=employee("ram",30)
e1.sample()