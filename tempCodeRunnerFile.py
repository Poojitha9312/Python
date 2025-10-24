class student:
    school_name="hamsavahini"
    def __init__(self):
        del  student.school_name

print(student.__dict__)
s1=student()
print(student.__dict__)
