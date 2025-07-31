class A:
    def m1(self):
        print("python")
    def m2(self):
        print("java")
class B(A):
    def sample(self):
        self.a=10
        print(f"The value of a is {self.a}")
b=B()
b.m1()
b.m2()

    