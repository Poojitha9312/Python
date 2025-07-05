#-----------METHOD OVERLOADING------------
'''
-->If 2 or more methods have same name with different no of parameters of different type of parameters is called method overloading.
-->Python does not support method overloading. Other languages like java support it.
-->Because if we will define multiple methods then python will consider the last one only.
-->But indirectly we can archieve method overloading by using multiple dispatch decorator.
'''

#The advantages of method overloading
'''
->Code reusability.
->Provide flexibility and easy to programmer.
->It reduce complexity.
'''

# Example 1:
# 2 or more methods having same name but different number of arguments...
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
# here in this case python will takes the latest one 
# python does not support method overloading directly...


# Example 2:
#How to archieve method overloading in python by using variable length arguments.

class student:
    def sample(self,*a):
        print(a)
s1=student()
s1.sample(10)
s1.sample(10,20,30)
s1.sample(120,130,140,150,160)

