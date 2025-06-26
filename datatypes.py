# Datatype is used to specify what type of data has to be stored in to the variable
# There are different datatypes in python:

#1.Number
#2.string
#3.list
#4.tuple
#5.set
#6.dict....

# now we are discussing about number datatype:
# int,float,complex,boolean

a=10 # here we do not need  declare datatype because python is dynamically typed language
print(a)
print(type(a))  # if we want to verify the type of object by using type() function
print(id(a))   # here we can know the address of the variable

b=8.2
print(b)
print(type(b))
print(id(b))

c=7+8j
print(c)
print(c.real)
print(c.imag)
print(type(c))
print(type(c.real))
print(type(c.imag))

# boolean- true or false:
f=True
g=False
print(type(g))
print(type(f))
print(bool(1))
print(bool(0))    # except zero if we given any number the output bocomes true
print(bool(8.2))
print(bool(8+7j))


# Type conversion:
x=20
y=8.2
z=7+8j

# convert from int to float:
a=float(x)
print(a)
print(type(a))

# convert from float to int:
b=int(y)
print(b)
print(type(b))

#convert int to complex:
c=complex(x)
print(c)
print(type(c))

# input Function:
a=input("enter the value :")
print(a)
print(type(a))

# but the input() takes default as string
# if we give specific datatype it will takes that type data as input
a=int(input(" enter the value :"))
print(a)
print(type(a))


