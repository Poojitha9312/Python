# # Example 1:
class student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def sample(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My rollno is {self.rollno}")
#Creation of Mutiple Objects this method is some have difficult
s1=student("priya",21,102)
s1.sample()

s2=student("kavya",22,124)
s1.sample()

s3=student("ramya",23,152)
s1.sample()

# creation of multiple objects by using list and for method
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(30*'=')

names=["kavya","priya","divya","ramya"]
age=[20,21,22,23]
for i in range(len(names)):
    s1=student(names[i],age[i])
    s1.sample()
    
# Example 3:
#Creation of multiple objects by using lists and for and the output is stored in list.
class  student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")

names=["kavya","priya","divya","ramya","punarvi","praneetha"]
age=[15,16,17,18,19,20]

obj_list=[]
for i in range(len(names)):
    s1=student(names[i],age[i])
    obj_list.append(s1)

print(obj_list)
print(30*'=')
# print(obj_list[0].name)
# print(obj_list[0].age)

# print(obj_list[1].name)
# print(obj_list[1].age)

# upto 5 we have to given like this instead of that method we can use this below method.....

for i in range(len(names)):
    print(obj_list[i].name)
    print(obj_list[i].age)
    print(30*'=')

# Example 4
#Creation of Mutiple Objects By using Multi Elements single list and for Method 
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(30*'=')
s1=[student("aparna",15),student("kavya",20)]
for student in s1:
    student.sample()
