# __str_method is dunder method or magic method used to represent the object as a string...used to print the output as string to users....

# without using __str__ method:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("snehi",15)
print(s1)

#Output:
'''<__main__.Student object at 0x0000021478455DF0>''' #Here it is not human readable language

# By using __str__method:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
# #Here in the this below __str__ method it converts the output to string.
    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"
s1=student("snehi",15)
print(s1)

# output:
# my name is snehi and my age is 15


# By using __repr__method:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#Here in the this below __repr__ method it converts the output to string. 
    def __repr__(self):
        return f"My name is {self.name} and my age is {self.age}"
s1=student("Ram",30)
print(s1)
#output:
#My name is Ram and my age is 30


# By using both __Str__method and __repr__method:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        print("here __str__method will executes")
        return f"My name is{self.name} and My age is {self.age}"
    def __repr__(self):
        print("here __repr_-method will executes")
        return f"My name is {self.name} and My age is {self.age}"
s1=student("ram",30)
print(s1)

#  If both methods are defined and if we call print() on this case python will use only __str__ method. If __str__ not present then only it fall back to __repr__ method.


# Another example using both methods:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        print("here __str__method will executes") 
        return f"My name is {self.name} and My age is {self.age}"
    def __repr__(self):
        print("here __repr__method will executes")
        return f" My name is {self.name} and my age is {self.age}"
s1=student("snehi",15)
s2=student("vasu",30)
print(s1)
print(s2)

s3=[(student("kavya",25),student("gopal",30))]
print(s3)

# Here executes __repr__ method because it is group object. Without __repr__ we cannot print the group objects.


