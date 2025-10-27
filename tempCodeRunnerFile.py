class student:
    school_name="Pragati"
    @classmethod
    def cm(cls):
        cls.school_location="kkd"
        cls.school_pincode=533005
        print(f" My schhol name is {cls.school_name} and my school location is {cls.school_location} and my school pincode is {cls.school_pincode}")
    
    def sample(cls):
        print(f" My schhol name is {cls.school_name} and my school location is {cls.school_location} and my school pincode is {cls.school_pincode}")
student.cm()# we can call by class name
s1=student()
s1.cm()
s1.sample()

#Example 4: By using class method we can perform several operation to static variables.
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