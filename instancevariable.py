# Instance variable:
# Instance variables are variables that belong to a specific instance (object) of a class.

# what is the requirement of instance variable?
# if the value of the variable varies from one object to another object then we can go for instance variables..

# how many ways to create instance variables?
# There are three ways to create instance variables
# Those are:
# 1.inside the constructor
# 2.inside the instance method
# outside the class..

# creating instance variables inside the constructor...
class student:
    def __init__(self,name,age): # constructor
        self.name=name# instance variable
        self.age=age# instance variable
s1=student("ram",30)
s2=student("snehi",15)
print(s1.__dict__)
print(s2.__dict__)


# creating instance variables inside the instance method...
class student:
    def sample(self,name,age):
        self.name=name
        self.age=age
h1=student()
print(h1.sample("lakshmi",30))
print(h1.__dict__)
h2=student()
print(h2.sample("punarvi",15))
print(h2.__dict__)


# creating instance variable outside the class...
class student:
    def __init__(self,name):
        self.name=name
s1=student("kaveri")
print(s1.__dict__)
s1.age=25
s1.address="vizag"
s1.rollno=124
print(s1.__dict__)


# Another example of instance variables....
class student:
    def __init__(self,name,age,rollno):# constructor
        self.name=name
        self.age=age
        self.rollno=rollno
s1=student("ruchi",15)
s2=student("snehi",15)
s3=student("rishitha",20)






