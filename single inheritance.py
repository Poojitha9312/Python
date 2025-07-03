# single heritance a child class can derive from a parent class...
#class A ------> class B(A)

# . Child class can access parent class members as well as own members.

# . But the parent class only can access its own members it can't access the members of the child class.
# '''


# Example:
class A:
    def m1(self):
        self.x=10
        self.y=20
        print(self.x)
        print(self.y)
    def m2(self):
        self.z=30
        print(self.z)
class B(A):
    pass

b1=B()
b1.m2()
b1.m1()

# Example 2:
# parent class can only access of there own properties but child class can access both parent and its own properties.
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

# Example 3:
# child class can access constructor, instance method, staticmethod, classmethod.

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
