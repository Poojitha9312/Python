#  Global functions:
# Local variable has more scope than global variable. If we want to access global variable when local and global with same variable name the we use gobal function.
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
