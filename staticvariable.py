#--------------------------STATIC VARIABLE---------------------------
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
print(s1.school_name) # We can call by object as well
print(student.__dict__)  # verify the static variable is class level object
print(s1.__dict__)   #Static variable is not object level 


#Example 2: Creation of static variable outside the Class
class student:
    pass
s1=student()
student.school_name="Sri Chaitanya" #static variable
print(student.__dict__)
#here we can create with object also
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
        
#Here in this case no need to create object we directly call static methods with class name reference.
student.static_method()
print(student.__dict__)


#-----------------ACCESSING THE STATIC VARIABLE--------------------------
# 1. Accessing the static variable outside the class...
class student:
    college_name="pragati college" # here it is a static variable
print(student.college_name)

# 2.Accessing the static variable inside the constuctor.....
class student:
    college_name="sri chaitanya" # static variable
    def __init__(self):
        print(student.college_name)
s1=student()

# 3. Accessing the static variable inside the instance method...
class student:
    college_name="sri chaitanya"
    def sample(self):
        print(student.college_name)

s1=student()
print(student.college_name)

# 4.Accessing the static variable inside the class method....
class student:
    school_name="hamsavahini"
    @ classmethod
    def sample(cls):
        print(student.school_name)

student.sample()

# 5. Accessing the static variable inside the static method....
class student:
    college_name="sri chaitanya"
    @staticmethod
    def sample():
        print(student.college_name)
student.sample()


#------------------MODIFYING STATIC VARIABLES------------------------
# 1.modify the static variable outside the class...
class student:
    college_name="pragati college"
print(student.college_name)
student.college_name="geetham college"
print(student.college_name)

# 2.Modifying the static variable inside the class and constuctor...
class student:
    school_name="little woods"
    def __init__(self):
        student.school_name="sri chaitanya"
print(student.school_name)
s1=student()
print(student.school_name)


# 3. Modifying the static variable inside the class and inside the instance method.......
class student:
    college_name="sri chaitanya"
    def sample(self):
        student.college_name="Aditya college"
print(student.college_name)
s1=student()
s1.sample()
print(student.college_name)


#---------------------DELETION OF STATIC VARIABLE-----------------------
# 1.Deletion of static variable outside the class
class student:
    school_name="pargati"
print(student.school_name)
print(student.__dict__)
del student.school_name
print(student.__dict__)

# 2.Deletion of static variable inside the class......
class student:
    college_name="aditya"
    del college_name
print(student.__dict__)

# 3.Deletion of static variable inside the class and inside the constuctor...
class student:
    school_name="hamsavahini"
    def __init__(self):
        del  student.school_name

print(student.__dict__)
s1=student()
print(student.__dict__)


# 4.Deletion of static variable inside the class and inside the instance method...
class student:
    college_name="pragati"
    def sample(self):
        del student.college_name
print(student.__dict__)
s1=student()
s1.sample()
print(student.__dict__)

# 5.Deletion of static variable inside the class and inside  the class method..
class student:
    school_name="Aditya"
    @classmethod
    def sample(cls):
        del student.school_name
print(student.__dict__)
student.sample()
print(student.__dict__)

# 6.Deletion of static variable inside the class and inside static method..
class student:
    college_name="Narayana"
    @staticmethod
    def sample():
        del student.college_name
print(student.__dict__)
student.sample()
print(student.__dict__)

