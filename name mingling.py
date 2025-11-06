#---------Name mingling----------------

# In Python, private variables are typically declared by prefixing them with an underscore (e.g., _variable), or more conventionally with two underscores (e.g., __variable). However, Python does not enforce strict access restrictions like some other languages (such as Java or C++). Instead, it relies on name mangling to "protect" variables with double underscores.

# Here are a few methods you can use to access private variables outside the class:

# 1. Using Name Mangling (For Double Underscore Variables)
# Python "mangles" the names of private variables by internally renaming them to include the class name. This makes it harder (but not impossible) to access them from outside.

# if we want to know in simple way what is name manglin
#  if we declare a variable with one or more underscores 
# then the interpreter taken as that variable with _classname___variablename....
# we know that private attribute can access only within the 
#class...
# if user has a requirement to access an private variable
# outside the class.. then we can use name mangling process....
# then we can access the private attribute outside the class..


# But how can we know the namemangling occurs in interpreter..
#  Here see one example for namemangling...
class A:
    _a=10
    __b=20
    _c__=30
    ___d=40
    __e__=50
# if we want to know that we have to check directory...
print(dir(A))

# output:

['_A___d', '_A__b', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__e__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_a', '_c__']

#Ex: Accessing variable outside the class
class A:
    def __init__(self):
        self.__x=100 #private attribute
             
a=A()
#print(a.__x)#we cannot access private attribute outside the class which is not possible. But we can overcome with the help of Name manlging.

print(a._A__x) #This is known as name mingling