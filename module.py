# Module is a file that contains calsses,variables and functions and running code...

# what is the requirement of module?
# if we want to reuse code then we go for functions but if we want to 
# reuse group of variables,classes and functions then we use module concept....each and every .py file is called as  module...

# types of Modules:
# There are three type of Modules
# 1. standard Modules
# 2.User defined Modules
# 3.3rd party Modules

# Example for understanding module concept..
a=10

x="ram"

z=9.2

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

# now you can import this file to another file now...
# import filename(means module name)
# print(modulename.variable or function)


# 1.standard Modules:
# These modules are already available in python software
# ex: os,sys,math etc...
# Example:
import math
print(math.factorial(5))
print(math.sqrt(9))

# 2.userdefined modules:
# The module which is created by user as per our requirement
# such type of module is called userdefined modules..
# ex: sample,pythonpractice(this means .py file names)
# Example:
def add(a,b):
    print(a+b)
    
def sub(a,b):
    print(a-b)

from module import add,sub
add(10,20)
sub(50,10)

# 3.3rd party modules:
# These modules provided by 3rd party vendor,it is vailable on internet
# by using pip
# Ex:
# numpy,pandas,matplotlib etc...

#Module Aliasing:
'''•	Giving another name to module is called module aliasing
        Ex: import sample as sam'''

#Module Member Aliasing:
'''•	Giving another name to module member is called module member aliasing.
        Ex: from sample import add as a, sub as s'''




