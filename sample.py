class student:
    school_name="pargati"
print(student.school_name)
s1=student()
del s1.school_name
print(student.__dict__)
