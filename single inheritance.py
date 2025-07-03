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