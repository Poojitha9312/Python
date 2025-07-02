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
c1=calculator()
c1.add()
calculator.sub()#calling static method using class name
c1.sub()