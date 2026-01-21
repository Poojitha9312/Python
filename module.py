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

# dir() vs help()

#dir() function will give only the members

#help() function will give all the member name along with description.
# import math
# print(dir(math))
# print(help(math))

#Example:
#sample1.py
a=10
b=20
def add(a,b):
    print(a+b)

#sample2.py
import sample1 
print(help(sample1))

#help output:
'''Help on module sample1:

NAME
    sample1

FUNCTIONS
    add(a, b)

DATA
    a = 10
    b = 20

FILE
    c:\users\jvrkr\git-repo\python\sample1.py


None'''

#sample2.py
import sample1 
print(dir(sample1))

#dir output:
'''['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'add', 'b']'''


#name__main__
'''
1. __name__ is a special variable.
2. If we want to know whether the program executed as a normal individual program or as a module then we use __name__ variable.
3. If you will execute a python individual program then it will give you the output as __main__.
4. If you will execute the program as a module from some other program then the value of __name__ variable is name of the module.
'''
#sample1.py
print("hello")
print(__name__)

#output
'''
hello
__main__  #it prints __main__ because it is directly execution
'''

#sample2.py
import sample1
print("hello")
print(__name__)

#Output:
'''
hello    #from sample1 program
sample1  #from sample1 program __name__ as module name because it imported
hello    #from sample2 program
__main__ #from sample2 program __name__ as __main__ because it is direct
'''

#Example:
#sample1 program code
def add(a,b):
    print(a+b)

if __name__=='__main__':
    add(10,20)
else:
    print("add() is not direct execution.")
    
'''If we run these above problem in sample1 it gives the output as 30'''

#sample 2 program code
import sample1

'''If we run the above code in sample2 it gives the output as 'add() is not direct execution.' '''
    
    
# math-module:
import math
#factorial
print(math.factorial(5))

#square root
print(math.sqrt(100))

#Ceiling and floor
print(math.floor(3.67))
print(math.ceil(3.67))

print(math.pi)

#Find area of triangle
area=math.pi*3.9*3.9
print(area)

#Find Eulers number value
print(math.e)