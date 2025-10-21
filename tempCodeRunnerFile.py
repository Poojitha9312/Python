class student:
    def __init__(self,name):
        self.name=name
s1=student("kaveri")
print(s1.__dict__)
s1.age=25
s1.address="vizag"
s1.rollno=124
print(s1.__dict__)