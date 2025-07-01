class student:
    def Details(self):
        student.school_name="Sri Chaitanya" #static variable

s1=student()
s1.Details()
print(student.__dict__)
print(s1.__dict)