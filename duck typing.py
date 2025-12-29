'''
Duck typing is to determine if an object is suitable for a purpose by checking for the presence of certain methods and properties rather than objects actual type.
'''
#  If it looks like a duck, swims like a duck,and quacks like a duck,then it probbably is a duck...
#  which simply means it doesnt matter it is duck or not if the behaviour of the bird match with the duck then it is a duck....

# Another example:
# A teacher says:
# “Anyone who can write may answer the question.”
# Students may have:
# Pen
# Pencil
# Marker

# The teacher does not care what you are holding.
# The teacher only cares:
# Can you write?


#Example
class A:
    def m1(self):
        print('A-m1')
class B:
    def m1(self):
        print('B-m1')
class C:
    def m1(self):
        print('C-m1')
        
def search(x):
    x.m1()

a=A()
search(a)

b=B()
search(b)

#Example
class Duck:
    def swim(self):
        print("Duck is swimming")
    
    def fly(self):
        print("Duck is Flying")
class Whale:
    def swim(self):
        print("Whale is Swimming")

def search(x):
    x.swim()
    x.fly()
    
d=Duck()
w=Whale()
search(d)
search(w)
        
for i in [Duck(),Whale()]:
    i.swim()
    i.fly()

'''   
Duck is swimming
Duck is Flying
Whale is Swimming
AttributeError: 'Whale' object has no attribute 'fly' 
'''