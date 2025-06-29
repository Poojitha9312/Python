class student:
    school_name="hamsavahini"
    @classmethod
    def cm(cls):
        cls.school_location="kkd"# create class variable by using cls
        student.school_pincode=533005
        print(f"my school name is {cls.school_name} and my school location is {cls.school_location} and my school pincode is {cls.school_pincode}")
student.cm()
s1=student()
s1.cm()