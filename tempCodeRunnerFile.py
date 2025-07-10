class person:
    def __init__(self,sal):
        self.sal=sal
    def __add__(self,x):
        return self.sal+x.bonus
class employee:
    def __init__(self,bonus):
        self.bonus=bonus

p1=person(20000)
e1=employee(5000)
print(p1+e1)