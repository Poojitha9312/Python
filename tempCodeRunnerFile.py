class student:
    def sample(self,*a):
        print(a)
    def sample(self,*x):
        print(x)
s1=student()
s1.sample(10)
s1.sample(10,20,30)
s1.sample(120,130,140,150,160)