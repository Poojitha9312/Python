#----------------------------METHOD OVERRIDING---------------------------

# --> A parent containg some method that method by default available to the child class.
# --> If child class want, then child class can provide own implementation for those method, this mechanism is called as method overriding.

# Example 1:
class parent:
    def sample(self):
        print(" I like fruits")
class child(parent):
    pass
c1=child()
c1.sample()


# example for method overriding

class parent:
    def sample(self):
        print("I like fruits")
    
class child(parent):
    def sample(self):
        print("I like Ice cream and pizza")# Method overriding
c1=child()
c1.sample()

# Another example of overriding:
#Ex: 
class Circle:
    def area(self,r):
        print(3.14*r*r)

class Triangle(Circle):
    def area(self,b,h):
        print(0.5*b*h)
        
class Square(Circle):
    def area(self,s):
        print(s*s)
        
t=Triangle()
t.area(2.3,5.6)