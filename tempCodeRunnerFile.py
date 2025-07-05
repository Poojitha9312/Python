class employee:
    def __init__(self,exp):
        self.exp=exp
    def __lt__(self,other):
        return self.exp<other.sal
class person:
    def __init__(self,sal):
        self.sal=sal

e1=employee(40000)
p1=person(30000)
print(p1<e1)
