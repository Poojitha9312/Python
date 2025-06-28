#---------------INSTANCE METHOD--------------------------
# Inside the instance method we use instance variables.
# The first argument of the instance method is self.
# We can call one instance method inside another instance method.
# Inside the class we can call instance method using self variable and outside the class we can call throught object reference.
# By using instance method we can perform various operations like modify, delete, etc.

# Example:
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        result=self.a+self.b
        print(f"The adding of two numbers result is {result}")
    def sub(self):
        result=self.a-self.b
        print(f"the subtraction of two numbers result is {result}")
s1=calculator(10,20)
s1.add()
s1.sub()


# 2. calling instance method inside another instance method...
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        result=self.a+self.b
        print(f"The addition result is {result}")
        self.sub()
    def sub(self):
        result=self.a-self.b
        print(f"the subtraction result is {result}")
s1=calculator(10,20)
s1.add()

# Example 3
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def access(self):
        print(f"The value of a is {self.a} and the value of b is {self.b}")
    
    def update(self,x,y):
        self.a=x
        self.b=y

    def delete(self):
        del self.a

        
t1=Test(10,20)
print(t1.__dict__)
t1.access()
t1.update(30,40)
t1.access()
t1.delete()
print(t1.__dict__)