# set datastructure is just like list but it cant hold duplicate items...
# set is an unorder collection which means it doesn't maintain order..
# In set we cant apply indexing and slicing concept
# set is mutable in nature and we can do modifications on set...
# but the set elements is immutable in nature..
# if we want to store unique elements (not duplicate) then we use the set...
# {} is used to create a set.....

# creation of empty set:
s={}
print(s)

print(type(s))
# Note: if we create a empty set it will taken as dictionary...

# In another way we can create a empty set by using set function:
s=set()
print(s)
print(type(s))

# creation of set with multiple items:
s={10,20,(1,2),50}
print(s)
print(type(s))
# here we cant store list,set,dict elements it will hold only tuple elements

# creation of set with different data items:
s={10,1,"pooji",True,7.8,(1,7)}
print(s)
print(type(s))

# creation of set from list:
l=[10,20,"pooji",True,9.0,50]
s=set(l)
print(s)
print(type(s))

# creation of set from range:
s=set(range(12))
print(s)
print(type(s))

# creation of set using eval()function:
s=eval(input("Enter your set:"))
print(s)
print(type(s))

# creation of set using tuple:
t=(10,20,"snehi",8.2,50)
s=set(t)
print(s)
print(type(s))

# creation of set from string:
a="rama  krishna"
s=set(a)
print(s)
print(type(s))

# Accessing elements in set:
# Accessing elements in set through indexing and slicing is not possible 
# because set doen't follow order
# By using membership operator we know that element is present or not(in,not in)
s={10,20,"snehi",5.2}
print(s)
print("snehi" in s)
print(70 in s)

# set Methods:
# add,update,remove,clear,copy,pop,enumerate,sort,max,min,length,discard

# 1.Add method:
# It used to add element on set
# If the added element is already present in a set it wont'be reflect and not raising any error
s={10,20,30,"snehi",False,8.0}
print(s)
s.add(35)
print(s)
s.add(10)
print(s)

# 2.update Method:
# It is used to add multiple elements in the set
# here we will add iterable objects like list,tuple,range,dict 
# but not individually...
s={10,20,30,"pooji"}
print(s)
# s.update(100,200)# type error: 'int' object is not iterable
# print(s)
s.update((100,200))
print(s)

s={10,20,"snehi",4.7}
print(s)
l=[1,2,3]
t=(50,60)
s.update(l,t,range(10))
print(s)

# 3.Remove Method:
# It is used to remove specified element from the set..
# If the element is not present in the set it will raise an keyerror....
s={5,10,15,60,False}
print(s)
s.remove(10)
print(s)
s.remove(20)# if the element is not present it will raise an keyerror.
print(s)

# 4.discard Method:
# discard is also similar to remove method only but if the element is not
# present in the set it wont raise any key error..
s={1,2,56,47,25}
print(s)
s.discard(47)
print(s)
s.discard(100)
print(s)

# 5.clear Method:
# It is used to clear all elements in the set but not set.....
s={10,20,30}
print(s)
s.clear()
print(s)

# 6.copy Method:
# It is used to copy set from another set
s={10,20,30,89,70}
v=s.copy()
print(v)
print(id(s))
print(id(v))

# 7.pop Method:
# It is used to remove randomly any element from set...
s={10,45,"ruchi",False}
print(s)
s.pop()
print(s)
s.pop()
print(s)

# 8.Enumerate method:
# It is used to return the index value and the value
s={1,2,3,True,"senhi"}
for i in enumerate(s):
    print(i)

# 9.sum Method:
s={10,20,5}
print(sum(s))

# 10.Length Method:
s={10,20,30}
print(len(s))

# Min Method:
s={1,3,5,7,75}
print(min(s))

# Max method:
s={15,25,48,79,97}
print(max(s))

# sort Method:
# It is used to print either in ascending order or descending order
s={21,35,65,82,1,4,7}
v=sorted(s)
print(v)
print(type(v))
s={1,2,7,21,35,78,97}
l=sorted(s,reverse=True)
print(l)
print(type(l))

# union method:
# it is used to return all the elements present in the set
s1={23,33,43,53,63,71,91}
s2={15,20,25,43,53,65}
print(s1.union(s2))
print(s1|s2)

# Intersection Method:
# it is used to returns the common elements present in the both sets..
s1={10,15,20,25,30,35}
s2={1,2,3,15,20,72}
print(s1.intersection(s2))
print(s1&s2)

# difference method:
# it is used to return s1 elements not s2 not common elements
s1={1,2,3,4,5,6,7,8}
s2={3,4,5,15,25}
print(s1.difference(s2))
print(s1-s2)

# symmetric difference:
# it is used to return all elemnets in s1 and s2 but not common elements..
s1={10,20,30,40}
s2={10,50,60}
print(s1.symmetric_difference(s2))
print(s1^s2)


# subset and superset:
a={1,2,3,4,5,6,7,8}
b={2,3,4}
print(b.issubset(a))
print(a.issuperset(b))

#set comprehension:
#If you want to create a set from iterable objects like list,tuple,range,dict etc
#By writing very less code in efficient way then we can go for set comprehensions.
s=set()
for i in range(10):
    s.add(i)
print(s)

# by using set comprehension:
s={i for i in range(10)}
print(s)


# Frozenset:
# Frozenset is similar to set datastructure but the small difference is there ,
# where the set is mutable and frozenset is immutable...so that we cant perform modification operations
s={23,33,43,53,63}
fs=frozenset(s)
print(fs)
print(type(fs))

# frozenset is immutable in nature we cant use remove and add
s={23,43,53,63}
fs=frozenset(s)
print(fs)
print(type(fs))
fs.add(26)
fs.remove(52)

# merging set elements:
s1={10,20,30}
s2={10,20}
s3=s1+s2
print(s3)







# while loop:

s={1,2,56,47,25}
s1=list(s)
i=0
while i<len(s1):
    print(s1[i])
    i=i+1