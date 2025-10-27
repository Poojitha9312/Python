#---------------STATIC METHOD------------------
# Inside the static method we will use the local variables.
# self or cls variable not required as argument.
# @staticmethod decarator we have to write before static method.
# we can call one static method inside the static method.
# Inside the class we can call the static method using the class name and outside of class we can call through the class name or object reference.


#Example 1:
class calculator:
    @staticmethod
    def add():
        a=10
        b=20
        result=a+b
        print(f"Addition result is {a+b}")
    @staticmethod
    def sub():
        a=10
        b=20
        result=a-b
        print(f"Subtraction result is {a-b}")
        
calculator.add() #calling static method using class name
# c1=calculator()
# c1.add()
calculator.sub()#calling static method using class name
# c1.sub()



#Example 2: calling static method inside the class
class calculator:
    @staticmethod
    def add():
        a=10
        b=20
        result=a+b
        print(f"Addition result is {a+b}")
        calculator.sub(30,40)
    def sub(a,b):
        result=a-b
        print(f"Subtraction result is {a-b}")
        
calculator.add()