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
# Ex: College is complex object and departments are smaller objects.

# Here without College(Container Object) there are no departments(Contained objects).
class car:
    def __init__(self,cname,ccolour,cprice):
        self.cname=cname
        self.ccolour=ccolour
        self.cprice=cprice
    def 
