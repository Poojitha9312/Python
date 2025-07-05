class employee:
    def __init__(self,sal):
        self.sal=sal
    def __lt__(self,other):
        return self.sal<other.exp
class person:
    def __init__(self,exp):
        self.exp=exp

e1=employee(40000)
p1=person(45000)
print(e1<p1)
