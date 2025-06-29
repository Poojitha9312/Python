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