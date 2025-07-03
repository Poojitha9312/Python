class A:
    def m1(self):
        x="ram"
        print(x)
    def m2(self):
        y="ruchi"
        print(y)
    def m3(self):
        z="kaveri"
class B(A):
    def sample(self):
        a=20
        b=10
        print(a+b)
b1=B()
b1.sample()
b1.m2()
b1.m1()