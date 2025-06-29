class student:
    def __init__(self,name,age,address,rollno):
        self.name=name
        self.age=age
        self.address=address
        self.rollno=rollno

    def sample(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My address is {self.address}")
        print(f"My rollno is {self.rollno}")

class student2:
    def modify(self,x):
        x.name="pranavi"
s1=student("punarvi",24,"kkd",124)
s1.sample()
s2=student2()
s2.modify(s1)
s1.sample()
