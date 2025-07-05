#------------operator overloading------------
'''
-->If we will use same operator in different purposes then it is called operator overloading.
-->we are using +, * and etc in operator for different purposes.
-->Python supports operator overloading other languages like java does not support it.
-->we will use corresponding magic method to overload operator.
'''
#Ex:
print(10+20)
print('Ram'+'Krishna')
'''In the above example operator work in different formats like adding, concatination'''

# overloading the '+' opeartor.........
class person:
    def __init__(self,sal):
        self.sal=sal
class employee:
    def __init__(self,bonus):
        self.bonus=bonus

p1=person(20000)
e1=employee(5000)
v=p1+e1
# adding two objects is not possible

#By using the magic method.........
class person:
    def __init__(self,sal):
        self.sal=sal
    def __add__(self,other):
        return self.sal+other.bonus
class employee:
    def __init__(self,bonus):
        self.bonus=bonus

p1=person(20000)
e1=employee(5000)
print(p1+e1)
print(p1.sal)
print(e1.bonus)

# Example 2:
# overloading the '<' operator
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

