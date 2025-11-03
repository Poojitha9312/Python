class A:
    def method1(self):
        print('A class method')
class B:
    def method1(self):
        print('B class Method')
class C(B,A): #Here is the priority first A will execute.
    pass
    
c=C()
c.method1()
