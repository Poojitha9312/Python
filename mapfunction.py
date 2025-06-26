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
print(list(map(lambda l,r:l+r,l)))