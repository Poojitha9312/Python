class A:
    def __init__(self):
        self.x=100 #public attribute
    
    def test(self):
        print(self.x) #We are accessing public attribute with in the class.
        
class B(A):
    def test1(self):
        print(self.x) #We are accessing public attribute with in the child class
        
# a=A()
# a.test()

# b=B()
# b.test1()

a=A()
print(a.x)