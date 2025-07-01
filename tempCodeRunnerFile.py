class student:
    @classmethod
    def class_method(cls):  #here for class method 1st variable is "cls" like "self"
        student.school_name="Sri Chaitanya" #static variable
        
#Here in this case no need to create object we directly call class methods with class name reference.
student.class_method()
print(student.__dict__)