class employee:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def sample(self):
        print(f"My name is {self.__name}  and my age is {self.age}")
    def get_name(self):
        return self.__name
    def set_name(self,mname):
        self.__name=mname
e1=employee("ram",30)
print(e1.get_name())
e1.sample()
e1.set_name("ramakrishna")
e1.sample()


        
