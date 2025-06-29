class Test:
    a=10
    b=20
    
    @classmethod
    def access(cls):
        print(f"The value of a is {cls.a} and the value of b is {cls.b}")
    
    @classmethod
    def update(cls,x,y):
        cls.a=x
        cls.b=y

    @classmethod
    def delete(cls):
        del cls.a

Test.access()
Test.update(30,40)
Test.access()
Test.delete()
print(Test.__dict__)