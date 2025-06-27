#------------STATIC VARIABLE---------------
# It is also called as class level variable
# static variable belongs to class not object

#--------when should we go for static variables---------
#  if the value of the variable is fixed for all obects
# then we can go for static variable.....

#----CREATION OF STATIC VARIABLE IN SIX METHODS-----
# 1.Inside class directly
# 2.outside of the class
# 3.inside the constructor
# 4.inside instance method
# 5.Inside class method
# 6.inside static method....


#Example 1: Creation of static variable inside the Class
class student:
    school_name="hamsavahini" #static variable

print(student.school_name)    #We can call directly by class
s1=student()
print(s1.school_name) #We can call by object as well
print(student.__dict__)  # verify the static variable is class level object
print(s1.__dict__)   #Static variable is not object level 


#Example 2: Creation of static variable outside the Class
class student:
    pass
s1=student()
student.school_name="Sri Chaitanya" #static variable
print(student.__dict__)

s1.school_name="Sri Chaintanya"
print(student.__dict__)

#Example 3: Creation of static variable inside the constructor
class student:
    def __init__(self):
        student.school_name="Sri Chaitanya" #static variable

s1=student()
print(student.__dict__)


#Example 4: Creation of static variable inside the Instance method
class student:
    def Details(self):
        student.school_name="Sri Chaitanya" #static variable

s1=student()
s1.Details()
print(student.__dict__)


#Example 5: Creation of static variable inside the class method by using class name
class student:
    @classmethod
    def class_method(cls):  #here for class method 1st variable is "cls" like "self"
        student.school_name="Sri Chaitanya" #static variable
        
#Here in this case no need to create object we directly call class methods with class name reference.
student.class_method()
print(student.__dict__)



#Example 5.1: Creation of static variable inside the class method by using cls variable
class student:
    @classmethod
    def class_method(cls):
        cls.school_name="Sri Chaitanya"
        
student.class_method()
print(student.__dict__)



#Example 6: Creation of static variable inside the static method by using class name
class student:
    @staticmethod
    def static_method():  #here for static method 1st variable is nothing
        student.school_name="Sri Chaitanya" #static variable
        
#Here in this case no need to create object we directly call class methods with class name reference.
student.static_method()
print(student.__dict__)


#-----------------ACCESSING THE STATIC VARIABLE--------------------------