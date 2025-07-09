a=int(input("Enter a value:"))
b=input("Enter b value:")
try:
    result=a+b
except TypeError:
    print(TypeError)