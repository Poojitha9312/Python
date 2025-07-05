class student:
    def method1(self,a):
        print(a)
    def method1(self,a,b):
        print(a)
        print(b)
    def method1(self,a,b,c):
        print(a)
        print(b)
        print(c)

s1=student()
# s1.method1(10)#TypeError student.method1 missing 2 positional arguments
# s1.method1(10,20)#TypeError student.method1 required one positional argument
s1.method1(10,20,30)