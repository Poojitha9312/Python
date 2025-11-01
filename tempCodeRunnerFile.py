class A:
    def m1(self):
        self.x=10
        print(f"Value or x is {self.x}")

class B(A):
    def m2(self):
        self.x=20
        

b=B()
b.m1()