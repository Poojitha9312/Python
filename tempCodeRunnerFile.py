class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        result=self.a+self.b
        print(f"The addition result is {result}")
        self.sub()
    def sub(self):
        result=self.a-self.b
        print(f"the subtraction result is {result}")
s1=calculator(10,20)
s1.add()