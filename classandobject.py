# What is Class
'''
class is a blue print of object. It is logical entity and it is virtual not real.
If we want to create an object, then we required a blueprint and that blueprint is known as class. Collection of object is known as class.
Inside class we will represent properties(variables) and behaviours(methods).
'''

#Example
'''
Suppose we have the class like Student.
For Student have some properties like SName, Sage, SAddress, SID.
For Student have some methods like Eating, Sleeping, Reading, Playing.
'''

#Syntax for class:
'''
class classname:
    #properties
    #methods
'''
    
#what is Object
'''
object is real entity and it is a physical entity.
Object is the instance of class.
Objects are created inside the Heap Memory.
we can create any number of objects by using class.
'''

#Syntax for Object:
'''
reference_variable=classname(arguments)
'''

#What is reference variable
'''
Reference varaible is used to refer to an object
Reference variable is acting as an accessor.
Reference variable is used to access properties and methods of an object.
Multiple objects can point to the same class.
'''

# creating class:
class Student:
    marks=10
    
    def sample(self):
        print("hello world")
# here we created only plan nothing but class, when we are creating
# method we have to pass atleast one argument "self" keyword


##Creating object by using class with the help of reference variable s1 and calling the propertys and methods.
s1=Student()
print(s1.marks)
(s1.sample())

# example 2:
class student:
    marks=10
    def sample(self,name,age):
        print(f"My name is {name} and my age is {age} ")
s1=student()
print(s1.marks)
s1.sample("ram",30)


#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
#Here no need to call with object (app.__init__(10)). It will execute directly when object created.
#Here init is a constructor as well as method used to assign values to instance variable

# example 3:
class student:
    def __init__(self,name,age):

        self.name=name
        self.age=age
    def sample(self,address):
        print(f"My name is {self.name} and my age is{self.age} and my address is {address}")
s1=student("ram",30)
s1.sample("kkd")

#Example 4: print the details with different methods:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_detail(self):
        print(f"My name is {self.name}")
    def my_detail2(self):
        print(f"My age is {self.age}")

s1=student("nihitha",18)
s1.my_detail()
s1.my_detail2()










        
