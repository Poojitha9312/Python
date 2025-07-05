#--------------CONSTRUCTOR OVERLOADING----------------------------
# Constructor overloading is a mechanism in which a class can have any number of constructors with different no of parameters of different type of parameters. Generally It doesnot support but we overcome with multi dispatch module

# example 1:
# constructor overloading is not possible

class student:
    def __init__(self,a):
        print(a)
    def __init__(self,a,b):
        print(a)
        print(b)
    def __init__(self,a,b,c):
        print(a)
        print(b)
        print(c)
s1=student(10)
# here it will raise TypeError student.init missing two positional arguments..because we alreay know that python will takes the latest one....
