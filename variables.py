# basic program:
print("hello world")

# comments:
# means single line comment
#''' are used for multiline comments...

# variables:
x=5  # here it is int
print(x)

y="john" # here it is string
print(y)

# here we can assign multiple values to multiple variables in single line:
x,y,z="ram","seetha","divya"
print(x)
print(y)
print(z)

# here we can assign single value to multiple variables:
x=y=z="ram"
print(x)
print(y)
print(z)

# here we can assign multiple values to single variable:
x="ram","apple","goa"
print(x)


# output variables:
# here we can add text and variable by using + symbol
x="is awesome"
print("python"+ x)
# but we cant add text and integer
x=2
print("python"+x)
# here it will give Type error:can only concatenate str to str but not int


# To know the address of the variable we use id :
x=10
print(x)
print(id(x))

