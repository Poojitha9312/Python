# Relationship is used to access the members of one class inside another class..
# The advantage of relationship is code-reusability....
# HAS-A relationship(also known as composition)
# IS-A relationship(Inheritance)
# Examples:

# 1. Employee HAS-A car
# 2. Employee IS-A Person
# 3. Car HAS-A Engine
# 4. Car IS-A Vehicle

# #1. HAS-A Relationship
# HAS-A Relationship is also known as Composition or Containership or Complex Objects.
# In HAS-A Relationship we will build objects from smaller objects.
# Ex: University is complex object and departments are smaller objects.

# Here without College(Container Object) there are no departments(Contained objects).

# Example:
# Student HAS-A Bag
# Student is not a bag
# Student has a bag
# Bag can exist alone

# This is HAS-A relationship
# HAS-A relationship means one class contains an object of another class.


class car:
    def __init__(self,cname,ccolour,cprice):
        self.cname=cname
        self.ccolour=ccolour
        self.cprice=cprice
    def car_details(self,ename):
        print(f"{ename}carname is {self.cname}")
        print(f"{ename}car colour is {self.ccolour}")
        print(f"{ename}car price is {self.cprice}")
        print("*"*20)



class laptop:
    def __init__(self,lname,lcolour,lprice):
        self.lname=lname
        self.lcolour=lcolour
        self.lprice=lprice

    def laptop_details(self,ename):
        print(f"{ename} laptopname is {self.lname}")
        print(f"{ename}  laptop colour is {self.lcolour}")
        print(f" {ename} laptop price is {self.lprice}")



class employee:
    def __init__(self,ename,eage,eid):
        self.ename=ename
        self.eage=eage
        self.eid=eid
        self.l =laptop("Lenovo", "Grey", "40K")
        self.c=car("BMW","black","1cr")
    def employee_details(self):
        print(f"my name is {self.ename}")
        print(f"my age is {self.eage}")
        print(f"my id is {self.eid}")
        self.l.laptop_details(self.ename)
        self.c.car_details(self.ename)
          # Pass the emp_name to the Laptop's details
s1=employee("ganilakshmi",20,1026)
s1.employee_details()


