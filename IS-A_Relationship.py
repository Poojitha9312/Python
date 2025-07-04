#------------INHERITANCE--------------
#1. IS-A Relationship / Inheritance

# Inheritance is a mechanism for creating a new class from an existing class.
# Here the old class is called Base class and the new class is called Derived class.
# if we will create a new class from an old class then we can easily access the members of a old class...


#Example:
'''
class A -->Old class/ Base Class/ Parent Class
  ..
  ..
  ..
  ..
  ..
class B(A) -->New Class/ Derived Class/ Child Class/ Sub Class/ Extended Class.
'''

#Example:
'''
            Person
            *    *
     IS-A  *      * IS-A
          *        *
         *          *
    Employee        Student
    
In the above 
    Employee IS-A Person.
    Student IS-A Person           
'''

#Example:
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

# #Example:
# class A:
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
b1.m2()# here it doesn't work it will raise attribute error

# #Example 2:
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
b1.m1()#here it will works because we apply inheritance...
# # B is the child class to parent class A.....



# Example 3:
class A:
    def __init__(self):
        self.x=10
        self.y=20
        
class B(A):
    def Details(self):
        print(f'x is {self.x}')
        print(f'y is {self.y}')
b=B()
b.Details()


# x is 10
# y is 20

#Example: Without Inheritance
class A:
    def __init__(self):
        self.x=10
        self.y=20
        
class B:
    def __init__(self):  #Here without Inheritance code usabilty is repeated
        self.x=10
        self.y=20
    def Details(self):
        print(f'x is {self.x}')
        print(f'y is {self.y}')
        
b=B()
b.Details()

'''
x is 10
y is 20
'''

#Adv and Disadv of Inheritance

# Adv:
# 1. Code reusability.
# 2. Reduce the code.
# 3. Code extensibility(By overriding the base class functionality).

# DisAdv:
# 1. Base and derived class both are tightly coupled(If we made any changes on parent class it will directly reflect on child class).

#Example about Disadvantage: If we change the value in parent class it will reflect in child class that's way Inheritance concept is tightly coupled.


#Example 1:
class A:
    def m1(self):
        self.x=10
        print(f"Value or x is {self.x}")

class B(A):
    def m2(self):
        self.x=20
        

b=B()
b.m1()

        
        
   