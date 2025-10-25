class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def access(self):
        print(f"The value of a is {self.a} and the value of b is {self.b}")
    def update(self,x,y):
        self.a=x
        self.b=y
    def delete(self):
        del self.a
t1=test(10,20)
print(t1.__dict__)
t1.access()
t1.update(30,40)
t1.delete()
print(t1.__dict__)