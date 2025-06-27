# In Python, the __dict__ method is a special attribute that is present in most objects. It returns the __dict__ attribute of an object, which is a dictionary that stores the object's attributes (variables and methods) and their corresponding values.


# 1. Instance __dict__:
# For an instance of a class, __dict__ is a dictionary containing all instance attributes (variables) and their corresponding values.

# example:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("priya",20)
# Accessing the __dict__ attribute
print(s1.__dict__)

#Output:
{'name': 'priya', 'age': 20}


# 2. Class __dict__:
# For a class, the __dict__ attribute contains the class’s attributes (including methods and variables) and their values. It holds information like class variables and method references.

class student:
    class_var = "I am a class variable"
    
    def method(self):
        print("This is a method.")

# Accessing the __dict__ attribute of the class
print(student.__dict__)

#Output:
'''
{'__module__': '__main__', 'class_var': 'I am a class variable', 'method': <function student.method at 0x7ff82efc0
'''