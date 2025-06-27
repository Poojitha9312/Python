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

# --------------CREATION OF INSTANCE VARIABLE-----------------

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

s1=student("ruchi",15,13)
s2=student("snehi",15,12)
s3=student("rishitha",20,36)
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)


# self.name and self.age hold data that is unique for each Person object created.
# -Instance variables are unique to each object


# Note:
# 
# -If the values of the variable is differ then we can proceed with Instance variable like(Name and age)because they differ on every object. So,Instance variable is a object level variable.
# -If the values of the variable is not differ then we can't use instance variable we can use only static variables like(school_name)


# ---------------MODIFYING INSTANCE VARIABLE-----------------
#Example 1:Modify the instance variable inside the constructor
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        if self.age<18:
            self.status="minor"
        else:
            self.status="major"
s1=student("'snehi",20)
print(s1.__dict__)


# Example 2: Modify the instance variable inside the Instance method......
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self,new_name):
        self.name=new_name
s1=student("lakshmi",30)
print(s1.__dict__)
s1.sample("ramya")
print(s1.__dict__)
 

# Example 3: Moifying the instance variable outside the class....
class student:
    def __init__(self,name):
        self.name=name
s1=student("ram")
print(s1.__dict__)
s1.name="vasu"
print(s1.__dict__)


# Accessing the instance variable inside the constructor...
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"my name is {self.name} and my age is {self.age}")
s1=student("ram",30)
print(s1.__dict__)

#Example 2:Accessing the instance variable inside the Instance Method
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age   
    
    def detials(self):
        print(f"My name is {self.name} and my age is {self.age}")
p1=Person("Ram",30)
p1.detials()


#Example 3:Accessing the instance variable outside the class 
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age   
p1=Person("Ram",30)
print(f"my name is {p1.name} and my age is {p1.age}")
print(p1.__dict__)

# 3. Deletion of instance variable....
#Example 1: Delete the instance variable inside the Constructor
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age  
        del self.age
p1=Person("Ram",30)
print(p1.__dict__)

#Example 2: Delete the instance variable inside the Instance method
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age  
    def deleteDetails(self):
        del self.name
p1=Person("Ram",30)
print(p1.__dict__)

p1.deleteDetails()
print(p1.__dict__)


#Example 3: Deletion the instance variable outside the class
class Person:
    def __init__(self,name,age,rollno):
        self.name=name 
        self.age=age 
        self.rollno=rollno 
p1=Person("Ram",30,32)
print(p1.__dict__)

del p1.rollno
print(p1.__dict__)
   
    
    








