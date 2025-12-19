# list is a collection of dissimilar datatypes like int,float,boolean, string
# list is mutable in nature..mutable means changeable after creation of object
# we can do any modifications on it..... 
#  list can be in square brackets[] and separated by comma
# creation of  empty list:
l=[]
print(l)

# creation of list:
l=[10,20,"poojitha",8.2,"snehitha",True]
print(l)
print(type(l))

# list function():
# we can change tuple and dict elements  in to list by using list function

l=list((10,20,30,40))
print(l)
print(type(l))

# creation of list  dynamically using eval():
l=eval(input("enter your list:"))
print(l)
print(type(l))

# creation of list using range function:
l=list(range(20))
print(l)

l=list(range(1,20,2))
print(l)

# characterstics of list:
# list is maintaining order in which order we inserted elements in same order stored in list...
# list can hold different dataitems..
# list is dynamic in nature based on our requirement we can increase or decrease the size of the list....
# list is mutable in nature means which is changeable, we can modify the list items..
# we can access the list elements by using positive and negative and slicing



# Accessing elements in the list  by using positive index and negative index:
l=[10,20,30,40,50,60]
print(l)

print(l[0])
print(l[3])
print(l[5])
print(l[-1])
print(l[-4])

# Accessing elements by using slicing:
l=[10,20,30,"poojitha",8.2,"snehitha"]
print(l) # [10, 20, 30, 'poojitha', 8.2, 'snehitha']
print(l[::])   # [10, 20, 30, 'poojitha', 8.2, 'snehitha']
print(l[0:4])  # [10, 20, 30, 'poojitha']
print(l[-1])  # snehitha
print(l[-1:-5]) # []
print(l[-5:]) # [20, 30, 'poojitha', 8.2, 'snehitha']



l=[10,{"name": "rama"},list((20,40))]
print(l)
print(type(l))


# printing elements using for loop:
l=[10,20,30,"poojitha",8.2,50,"snehitha"]
for i in l:
    print(i)

# another for loop using condition:
l=[10,20,2,4,13,11,60,59]
for i  in l:
    if i%2==0:
        print(i)

# printing elements using while loop:
l=[10,20,30,8.5,"snehitha"]
i=0
while i<len(l):
    print(l[i])
    i=i+1


l=[10,20,31,41,51]
i=0
while i<len(l):
    if i==3:
     print(l[i])
    i=i+1

# using split function:
m="WELCOME TO HIE TECH SOLITIONS"
l=m.split('O')
print(l)






