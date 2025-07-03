class A:
    def method1(self):
        print("A class Method1")
    def method2(self):
        print("A class method2")
class B:
    def method3(self):
        print("B class method3")

b=B()
b.method3()
b.method1() #Here B object has no attribute 'method1'

#Example:
class A:
    def m1(self):
        x="ram"
        print(x)
    def m2(self):
        y="ruchi"
        print(y)
    def m3(self):
        z="kaveri"
class B:
    def sample(self):
        a=20
        b=10
        print(a+b)
b1=B()
b1.sample()
b1.m2()