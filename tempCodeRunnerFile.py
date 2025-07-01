class student:
    pass
s1=student()
student.school_name="Sri Chaitanya" #static variable
print(student.__dict__)
#here we can create with object also
s1.school_name="Sri Chaintanya"
print(student.__dict__)