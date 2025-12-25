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