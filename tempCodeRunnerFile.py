class calculator:
    @staticmethod
    def add(a=10,b=20):
        print(f"Addition result is {a+b}")
        
    def sub(a,b):
        print(f"Subtraction result is {a-b}")
        
calculator.add() #calling static method using class name
c1=calculator()
c1.add()