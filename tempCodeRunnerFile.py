class student:
    school_name="Aditya"
    @classmethod
    def cm(cls):
        cls.school_location="rjy"
        print(f"My schoolname is {cls.school_name} and my location is {cls.school_location}")
        student.sample(cls)#here calling class method in another class method
    def sample(cls):
        cls.school_principalname="haritha"
        print(f" my principal name is {cls.school_principalname}")

student.cm()