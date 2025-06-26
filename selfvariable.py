#self_variable:
'''
We can access attributes and methods inside the class.
These variables are used to access instance variables and instance methods.
self is used to refer to a current class object or current memory.
'''

#reference_variable:
'''We can access object attributes and methods outside of the class'''

# Example:
class student:
    def __init__(self,name,age):# constructor with self
        self.name=name
        self.age=age
    def sample(self):
        print(f"My name is {self.name} and my age is {self.age}")
s1=student("mahi",25)# here s1 is reference variable
s1.sample()

# Example:Taking values at run time
class student:
    def __init__(self):
        self.name=input("enter your name:")
        self.age=int(input("enter your age:"))
    def sample(self,address):
        print(f" My name is {self.name} and my age is {self.age} and my address is {address} ")
s1=student()
s1.sample("vizag")

#Both self and reference variable pointing to same location it returns same address
class student():
    def __init__(self):
        print(id(self))
        
s1=student()
print(id(s1))


#Example: we can use x or anything instead of self variable
class student:
    def __init__(x):# constructor with self
        x.name=input("enter your name:")
        x.age=int(input("enter your age:"))
    def sample(x):
        print(f"My name is {x.name} and my age is {x.age}")
s1=student()# here s1 is reference variable
s1.sample()
    
