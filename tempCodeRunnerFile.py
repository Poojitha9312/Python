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
