#----------------------------METHOD OVERRIDING---------------------------

# --> A parent containg same method that method by default available to the child class.
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

#Ex: 
class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
        
class Cat(Animal):
    def sound(self):
        print("Cat Meows")
        

