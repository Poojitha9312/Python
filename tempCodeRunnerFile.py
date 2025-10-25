class calculator:
    def add(self):
        a=10
        b=20
        result=a+b
        print(result)
        
    def sub(self):
        print(a)  #Here var a and b not works because they are local to add method
        print(b)
c1=calculator()
c1.add()
c1.sub()