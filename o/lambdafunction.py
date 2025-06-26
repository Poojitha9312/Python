# lamda function:
# lamda function is also called as anonymous function...
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
