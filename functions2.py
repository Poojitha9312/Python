# #Functions is the collection of statements or a piece of code to perform a specific task.
# # function means sub program or mini program
# # function is nothing but collection of statements that are kept inside a block
# ###Advantages###
# '''
# Code Reusability
# Improve Modularity
# '''

# define user defined function
# # def keyword is used to user defined function

# # syntax for functions:
# # def function_name(parameters):
# # ''' doc string'''
# # statements
# # return value

def add(a,b):
    print(a+b)
add(10,20)

 ##### Use of Functions #####
# '''If we want to execute a piece of code for multiple times then we go for functions.'''

# a=10
# if a%2==0:
#     print('Even')
# else:
#     print('odd')
    
# b=20
# if b%2==0:
#     print('Even')
# else:
#     print('odd')
    
# c=30
# if c%2==0:
#     print('Even')
# else:
#     print('odd')
    
# #Here in the above line of code we are writing the piece of code again and again on the scenarios use functions like below.
# def Even_Odd(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
        
# Even_Odd(10)
# Even_Odd(13)

# # Types of Functions:
# # There are two types of functions:
# # 1. build in function
# # 2. user defined function:

# # 1. build in function:
# # those function which is already created by python people such functions are 
# # known as build in functions...these functions are ready to use...

# # EX: print(),min(),max(),eval(),type(),id(),int(),input()

# # 2.user defined functions:
# # those functions which are  defined by user , here user is nothing but programmer
# # as per user requirement such type of function is called user defined

# # EX: evenodd(),check(),display(),msg()

# # what is doc string
# # docstring is used to know the description of particular function:
# # how to print description about a function?
# # print(fun_name.__doc__)

# def add(a,b):
#     """This add function is used to perform adding of numbers"""
#     print(a+b)

# add(25,35)
# add(60,80)

# print(add.__doc__)

# # parameters and argument:
# # what is a parameter?
# # A parameter is just like a variable that present in function definition
# # parameters means input to function

# # what is a Argument?
# # An argument is a value that is send to function at the time of calling

# # here is the example to know what are parameters and arguments
# def add(a,b,c):# (a,b,c) are parameters
#     print(a+b+c)
# add(10,20,30) # here (10,20,30) are arguments....



# call by value and call by reference:
# If we made any changes on called function it will not reflect on outside the function when we call with value.
def sample(a):
    print("inside the function before modification",a)
    print("inside the function before modification",id(a))
    a=a+10
    print(" after modification inside the function",a)
    print("after modification inside the function",id(a))
a=23
print(" outside the function before calling function",a)
print(" outside the function before function calling",id(a))
sample(a)
print("outside the function after modification",a)
print("outside the function after calling",id(a))

# call by reference:-
'''If we made any changes on called function it will reflect on outside the function when we call with reference.'''
def sample(a):
    print(" inside the function before modification",a)
    print("inside the function before modification",id(a))
    a.append(100)
    print(" after modification inside the function",a)
    print("after modification inside the function",id(a))
a=[10,20,30]
print(" outside the function before calling function",a)
print(" outside the function before function calling",id(a))
sample(a)
print("outside the function after modification",a)
print("outside the function after calling",id(a))

'''Py# these are not in correct position
thon does not support Call by value or Call by reference it support by call by object reference. When we pass immutable objects like int,float, tuple it acts like call by value (i.e., modify that object and create new object.) and when we pass mutable objects like list, dictionary it acts like call by reference (i.e., modify that object and will not create new object.).'''

##### return vs print
'''In functions internally return a value by default as None'''
#Example:
def add(a):
    print(a)

print(add(10))  #Here it will return None because we not returning any thing.  10  None

# Example:
def add(a):
    print(a)
    return a+20
print(add(10))

# Example:
def say():
    print("hello")
    return "how are you"
print(say())

# Example:
def sample():
    print("ram")
    return("krishna") # if we want return value also then we use print function...
sample()

'''return statement only be at end of the function. If we give return statement in the middle after return statement remaining statement will not going to be executed.'''
#Python function can return multiple values.
def sample(a,b,c):
    return a,b,c
print(sample(10,20,30))


##### Types of Arguments #####
'''There may be several types of arguments which can be passed at the time of function calling.
•	Default arguments
•	Keyword arguments
•	Required or positional arguments
•	Variable-length arguments'''

#1. Positional Arguments:
'''Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.'''
# Example:
def sample(a,b,c):
    print(a,b,c)
sample(10,20)# arguments should match with arguments in the definition of function

# Example:
def my_fun(a,b):
    print ("Name is:",a, "My age is :",b)
my_fun(30,"Ram")
# 2.keyword Arguments:
'Python allows us to call the function with the keyword arguments. This kind of function call will enable us to pass the arguments in the random order.'''
# Example:
def snehi(name,age,school_name):
    print("My name is:",name)
    print("My age is:",age)
    print("My school_name is :",school_name)
snehi("snehitha",15,"hamsavahini")

# Example:
def sample(name,age,place):
    print("My name is:",name)
    print("My age is:",age)
    print("My place is:",place)
sample("ram",age=29,"kkd")# positional argument follows keyword argument


# Example:
def sample(name,age,place):
     print("My name is:",name)
     print("My age is:",age)
     print("My place is:",place)
sample(name="ram",age=29,place="kkd")

# 3.Default arguments
'''While defining a function, we can initialize some of the arguments using default values. Passing default value to parameter is optional.
If we pass value to default argument, existing value will be replaced.'''

# Example:
def sample(a,b,c=15):
    print ("The value of a is :",a,"The value of b is :",b,"The value of c is :",c)
sample(10,20)

# Example:
def add(a,b,c=30):
    return a+b+c
print(add(10,20,40))

###Variable-Length Arguments:
'''In the large projects, sometimes we may not know the number of arguments to be passed in advance. In such cases, Python provides us the flexibility to provide the comma separated values which are internally treated as tuples at the function call.
However, at the function definition, we have to define  *variable-name .
•	Non–Keyworded Arguments (*args)
•	Keyworded Arguments (**kwargs)'''

#Example:
def variableargs(a):
	print(a)
variableargs(10)

#Example:
def variableargs(a):
	print(a)
	
variableargs(10,20) # it gives an error because we declared one parameter but we passed two values.

#Example:
def variableargs(*a):
	print(a)
	
variableargs(10,35.2,"pyton") #it will executes because we take it is a pointer like tuple.
variableargs(name="Rama",age=24)#it gives an error beacue it is in dictinary format.

#Example:
def variableargs(**a):
	print(a)
variableargs(name="Rama",age=24)      #** accepts dictinary format.

# Global functions:
# Local variable has more scope than global variable. If we want to access global variable when local and global with same variable name then we use gobal function.
y="awesome"
def sample():
    y="fantastic"
    print("python is" + y)
sample()
print("python is "+ y)

# global keyword:
y="awesome"
def sample():
    global y
    y="fantastic"
    print("python is" + y)
sample()
print("python is "+ y)

# one more example:
a=20
def sample():
    global a
    a=a+15
    print("The value of a is :", a)
sample()

# Nested function:
# A function present inside another function is known as nested function...
def outer_fun():
    print(" inside outerfun")
    def inner_fun():
        print(" inside innerfun")
    inner_fun()
outer_fun()

# Calling inner functions outside of outer function is not possible to call inner function outside of the function'''
def outer_fun():
    print("Inside outer function")
    def inner_fun():
        print('Inside inner function')
    inner_fun()
    
outer_fun()
#inner_fun() #error
def outer_fun():
    print("Inside outer function")
    def inner_fun():
        print('Inside inner function')
    return inner_fun
    
x=outer_fun() #when outer function is equal to some variable then it returns inner function as well
x() 

# output:
# Inside outer function
# Inside inner function

# what is recursion:
# A function call itself is called as recursion
# A function must have base case(termination condition) and recursive steps

# why we use recursion:
# solve complex problems easily
# to write less code
# Example:
def sample():
    print("hai welcome to python")
    sample()
sample()

'''Example: Option to stop recursive function.'''
def sample():
    print("welcome to Janahita\n\n")
    print("press 1 to call function again \n")
    print("press 0 to exit\n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        sample()
    else:
        exit(0)
        
sample()

#WAP to print *'s using recursion
'''
*
**
***
****
*****
'''
def fun(num):
    print('*'*num)
    if num==5:
        return
    fun(num+1)

fun(1)

#WAP to print *'s using recursion
'''
*****
****
***
**
*
'''
def fun(num):
    print('*'*num)
    if num==1:
        return
    fun(num-1)

fun(5)


# lamda function:
# lamda function is a called small anonymous function...
# here anonymous nameless
# if we declare a function without anyname such type of function is called as lamda function..
# in normal functions we are using def keyword but in lamda function
# we are using lamda keyword...
# The main function of lamda is for onetime use...
#Example:
x=lambda a,b,c:a+b
print(x(1,8,3))

print((lambda a,b:a+b)(10,20)) #we can write in one line also

#Example:
y=lambda a,b:a if a>b else b
print(y(10,20))

print((lambda a,b:a if a>b else b)(10,20))

#Example:
z=lambda a,b:a,b
print(z(10,20))#error beacuse lambda can take any no of arguments but have only one expression

#Example:
z=lambda a,b:(a,b) #Here it is one expression
print(z(10,20)) # it works Because it is one expression with in one entity tuple

#Where we exactly use lambda function?
'''Sometime as a programmer we have to pass function as an argument to another function, at that particular time we can go for lambda function. These functions mainly used in filter(), map(), reduce().'''

# import function:
# In python we can import and export the data.
def add(a,b):
    print(a+b)


def sub(a,b):
    print(a-b)

from zsample import add,sub
add(10,20)
sub(50,15) 


#Enumerate Function:
'''
The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.The enumerate() function adds a counter as the key of the enumerate object.
'''
            
#Syntax:
'''
enumerate(iterable, start)

iterable ----------- An iterable object
start---------A Number. Defining the start number of the enumerate object. Default 0
'''

#Example:
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))

'''
output: It returns Index(i.e., Iterable) and value
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
'''

# filter function:
# filter function is used to filter value in a sequence...
# filter function is a higher order function that means 
# if a function takes function as a argument...

# syntax of filter function:
# filter(function,sequence)
# argument function should return either true or false...
#function: 
'''function that tests if each element of a sequence true or not.'''
#sequence:
'''sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.'''
# NOTE:filter gives true output only

# write a program to print even in a list by using filter function
def even(y):
    if y%2==0:
        return True
    else:
        return False
l=[10,15,30,27,92,46]
r=list(filter(even,l))
print(r)
print(type(r))
for i in r:
    print(i)

# here it is an iterable object so we can use for loop

# second program using lambda function:
# write a program to print even in a list using lambda function
l=[10,20,30,77,51,97]
r=list(filter(lambda y:y%2==0,l))
print(r)
print(type(r))
for i in r:
    print(i)

# if we want to print in set format:
l=[10,20,30,77,51,97]
r=set(filter(lambda y:y%2==0,l))
print(r)
print(type(r))
for i in r:
    print(i)

# By using lambda function we can write in single line also:
l=[10,20,30,47,56,21]
print(list(filter(lambda y:y%2==0,l)))


#WAP to print the vowels is present in the specific elements with filter.
l=['h','e','r','a','r','s','p','k']
def sample(y):
    vowels=['a','e','i','o','u']
    if (y in vowels):
        return True
    else:
        False
r=list(filter(sample,l))
print(r)
print(type(r))


# WAP to print the vowels is present in the specific elements with filter by using lambda
l=['h','e','r','a','r','s','p','k']
vowels=['a','e','i','o','u']
r=tuple(filter(lambda y: y in vowels,l ))
print(r)
print(type(r))
for i in r:
    print(i)

# By using lambda function can write in single line:
l=['h','e','r','a','r','s','p','k']
print(list(filter( lambda y:y in ['a','e','i','o','u'],l)))

# Another way using lambda function:
print(list(filter(lambda i:i in ['a', 'e', 'i', 'o', 'u'],['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'])))

# write a program to print even items from dictionary:
d={1:"ram",2:"krishna",3:"ruchi",4:"ramya"}
def sample(i):
        if i[0]%2==0:
            return True
        else:
            return False  
r=list(filter(sample,d.items()))
print(r)
print(type(r))

# By using lambda function we can write in single line:
d={1:"ram",2:"krishna",3:"ruchi",4:"ramya"}
print(list(filter(lambda i:i[0]%2==0 ,d.items())))


# map function():
# if you have one or more sequence of data, if you want to perform operation on each and every element then we can use map function...
# syntax of map function:
# map(function,sequences)
# here function performs operation on each and every element...

# write a program to print square of each number in the list...
l=[10,20,30,40]
def square(z):
    return z*z
r=list(map(square,l))
print(r)
print(type(r))

# write a program to print square of each number in the list by using lambda function
l=[10,20,30,40]
print(list(map( lambda  z:z*z,l)))


# write a program to print merging two lists:
l=[1,2,3,4,5,]
r=[10,20,30,40,50]
print(list(map(lambda l,r:l*r,l,r)))

#Reduce function:
'''The reduce() function receives two arguments, a function and an iterable. However, it doesn't return another iterable, instead it returns a single value.
Reduce function present inside the functools, so we have to import it before using reduce function.'''

# adding sum of all elements in the list....
from functools import reduce
l=[1,2,3,4,5]
def sample(a,b):
    return a+b
r=reduce(sample,l)
print(r)
print(type(r))

# By  using lambda function:
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda a,b:a+b,l))


# finding out square of all elements in the list by using lambda function......
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda a,b:a*b,l))

#Difference between reduce and accumulate
'''
reduce gives final output but accumulate gives iterable output
accumulate syntax:(iterable,function)
'''
#reduce example
from functools import reduce
result=reduce(lambda a,b:a+b,[2,3,4,5])
print(result)

#accumulate example
from itertools import accumulate
result=list(accumulate([1,2,3,4,5],lambda a,b:a+b))
print(result)


# generator function:
#generators are like functions which contain yield keyword...
'''A generator-function is defined like a normal function, but whenever it needs to generate a value, it does go with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.'''
'''The difference between the yield and the return statement in Python is:
Return: A function that returns a value at once. The return statement returns a value and exits the function altogether.
Yield: A function that yields values repeatedly. The yield statement pauses the execution of a function and returns a value.
When called again, the function continues execution from the previous yield. A function that yields values is known as a generator.'''

def add(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
    yield a%b
    yield a+20
    yield b+40
    yield a-2
    yield a+1
x=add(10,20)
print(type(x))
# here x is an generator object
print(x.__next__())
print(next(x))
print(next(x))
print(next(x))
for i in x:
    print(i)

# example:
def sample():
    yield 1
    yield 2
    yield 3
x=sample()
print(x.__next__())
print(next(x))
print(next(x))


# example:
def sample():
    yield 1
    yield 2
    yield 3
x=sample()
print(type(x))
for i in x:
    print(i)



































    





















  

