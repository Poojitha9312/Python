class student:
    school_name="Pragati"
    @classmethod
    def cm(cls):
        cls.school_location="kkd"
        cls.school_pincode=533005
        print(f" My schhol name is {cls.school_name} and my school location is {cls.school_location} and my school pincode is {cls.school_pincode}")
    def sample(cls):
        print(f" My schhol name is {cls.school_name} and my school location is {cls.school_location} and my school pincode is {cls.school_pincode}")

student.cm()# we can call by class name
s1=student()
s1.cm()
s1.sample()