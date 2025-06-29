class calculator:
    a=10
    b=20
    @staticmethod
    def add(a,b):
        print(f"Addition result is {a+b}")
        
    def sub(a,b):
        print(f"Subtraction result is {a-b}")
        
calculator.add(10,20) #calling static method using class name
c1=calculator()
c1.add() 