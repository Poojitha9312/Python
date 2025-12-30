#Passing one class members to another class using Instance method............


# In Python, you can pass **one class’s object or its data** to another class using:

# 1. **Instance Methods**
# 2. **Class Methods**
# 3. **Static Methods**

# Real-life example 🏫
# A Student has a name
# A School shows student details
# The School should not store student data.
# It should just use it.


# What’s happening?
# Student keeps student data
# School uses that data
# Data is passed, not copied

# Here are the advantages in very simple lines 👇
# Keeps code simple and organized
# Makes code easy to reuse
# Easy to change or update later
# Each class does only one job
# Makes programs easy to understand and maintain


# passing one class object reference to another class  by using 
# Instance method
class student:
    def __init__(self,name,age,address,rollno):
        self.name=name
        self.age=age
        self.address=address
        self.rollno=rollno

    def sample(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My address is {self.address}")
        print(f"My rollno is {self.rollno}")

class student2:
    def modify(self,x):
        x.name="pranavi"
s1=student("punarvi",24,"kkd",124)
s1.sample()
s2=student2()
s2.modify(s1)
s1.sample()

###Here we are passing only one object from one class to another class using instance method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    def modify(self, x):  # instance method (requires self)
        print(f'Modified Age: {x}')

s1 = Student("Ram", 30)
staff1 = Staff()  # creating an instance of Staff
staff1.modify(s1.age)  # calling instance method with self

###Passing one class members to another class using Class method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @classmethod
    def modify_student(cls, x):
        x.age = 31
        print("Student age modified by class method in Staff")

s1 = Student("Ram", 30)
s1.Details()

Staff.modify_student(s1)   # ✅ pass object, not s1.age
s1.Details()


###Here we are passing only one object from one class to another class using class method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @classmethod
    def modify_age(cls, x):  # class method (uses cls)
        print(f'Age is: {x}')

s1 = Student("Ram", 30)
Staff.modify_age(s1.age)  # works like static method, but passes class as first arg

###Passing one class members to another class  using static method
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @staticmethod
    def modify(x): #### x is object reference where s1 and x are same.
        x.age=31 
              
s1=Student("Ram",30)
s1.Details()

Staff.modify(s1)  #Here we are passing complete object (s1 ---- x)
s1.Details()

###Here we are passing only one object from one class to another class using static method
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @staticmethod
    def modify_age(x): 
        print(x)

s1=Student("Ram",30)
Staff.modify_age(s1.age)  #Here s1 has two objects but we are taking only age in to x.

