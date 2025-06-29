#----------CLASS METHOD----------------
# Inside the class method we use static variables/ class-level variables.
# The first argument of the class method is cls.
# @classmethod decarator we have to write before class method.
# we can call one class method inside the another class method.
# Inside the class we can call class method using class name and outside the class we can call throught class name or object reference.
# By using class method we can perform various operations like modify, delete, etc.

# Example:
class student:
    school_name="hamsavahini"
    @classmethod
    def cm(cls):
        cls.school_location="kkd"# create class variable by using cls
        student.school_pincode=533005
        print(f"my school name is {cls.school_name} and my school location is {cls.school_location} and my school pincode is {cls.school_pincode}")
student.cm()
s1=student()
s1.cm()


# Example 2: call class method inside another class method....
class student:
    school_name="Aditya"
    @classmethod
    def cm(cls):
        cls.school_location="rjy"
        print(f"My schoolname is {cls.school_name} and my school location is {cls.school_location}")
        student.sample(cls)#here calling class method in another class method
    def sample(cls):
        cls.school_principalname="haritha"
        print(f" my principal name is {cls.school_principalname}")

student.cm()
# s1=student()
# s1.sample()


#Example: accessing one classmethod variables to another classmethod
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








