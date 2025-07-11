class A:
    def __init__(self):
        self._x=100 #protected attribute
    
    def test(self):
        print(self._x) #we are accessing protected attributes with in the class

class B(A):
    def test1(self):
        print(self._x) #we are accessing protected attributes with in the child class

a=A()
a.test()

b=B()
b.test1()

a=A() 
print(a._x)