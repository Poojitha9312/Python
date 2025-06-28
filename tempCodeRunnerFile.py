class student:
    college_name="Narayana"
    @staticmethod
    def sample():
        del student.college_name
print(student.__dict__)
student.sample()
print(student.__dict__)