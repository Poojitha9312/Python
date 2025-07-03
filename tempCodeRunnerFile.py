class x:
    def __init__(self):
        self.a=10
        self.b=30

class y(x):
    def sample(self):
        print(f"My name is {self.a}")
        print(f"My age is {self.b}")
y1=y()
y1.sample