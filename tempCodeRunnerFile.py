class A:
    def m1(self):
        self.x=10
        self.y=20
        print(self.x)
        print(self.y)
    def m2(self):
        self.z=30
        print(self.z)
class B:
    def m3(self):
        self.k=50
        print(self.k)
    
a1=A()
a1.m3()

b1=B()
b1.m1()
b1.m3()