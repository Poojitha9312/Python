class A:
    a=10
    print(f"{a}")
    def __init__(self):
        self.b=30
        print(f"The value of b is {self.b}")

    def sample(self):
        x=30
        print(f"the value of x is {x}")

    @classmethod
    def cm(cls):
        cls.j="ram"
        A.age=30
        print(f"My name is {cls.j} and my age is {A.age}")
    @staticmethod
    def sm():
        r="krishna"
        print(f"My name is {r}")
class B(A):
    pass

b1=B()
b1.sample()
b1.cm()
b1.sm()