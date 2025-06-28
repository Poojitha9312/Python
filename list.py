# list is a collection of dissimilar datatypes like int,float,boolean, string
# list is mutable in nature..mutable means changeable after creation of object
# we can do any modifications on it..... 
#  list can be in square brackets[] and separated by comma

# creation of  empty list:
l=[]
print(l)

# creation of list:
l=[10,20,"poojitha",8.2,"snehitha"]
print(l)

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
print(l)
print(l[::])
print(l[0:4])
print(l[-1])
print(l[-3:])
print(l[-5:])


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



# write a program to print elements in the list along with positive index and negative index value:
l=[10,20,33,45,51,61]
n=len(l)
for i in range(n):
    print("  {}   at present index is {}  /  {}".format((l[i]),i,i-n))

# updaating the list elements:
l=[10,2,3,4,50,60,8,9]
l[2]=20
print(l)
l[1:4]=45,30
print(l)
   

# update the list elements by using iteration  method:

l=[1,2,3,4,10,20,30]
for i in range(3,6):
   ele=eval(input(f" Enter the {i} th element of the list" ))
   print(l.insert(i,ele))
   print(l)

# write a program to print the list elements in reverse order:
l=[10,20,30,40,50]
n=len(l)-1
while n>=0:
    print(l[n])
    n=n-1

# write a program to to check whether your lucky number is in list or not(membership operator)
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
choice=int(input(" enter your choice :"))
if choice in l:
    print(" your lucky number is present in the list")
else:
    print(" your lucky number is not there in the list")

# write a program to find min value in the list:
l=[10,20,15,17,22,33,44,1,55,60]
min=l[0]
for i in l:
    if i<min:
        min=i
print(" Minimum value is :",min)


# write a program to find max value in the list:
l=[10,20,30,90,40,50,60,70]
max=l[0]
for i in l:
    if i>max:
        max=i
print(" Maximum value is :", max)


# write a program to print new_list:
l=["hai","hello"]
s=["ram","seetha","lasya"]
new_list=[]
for i in l:
    for j in s:
        new_list.append(i+j)
print(new_list)


# write a program to print first and last character in a word:
l=["ram","seetha","lasya"]
new_list=[]
for i in l:
    new_list.append(i[0] + i[-1])
print(new_list)


# enumerate function: the requirement of enumerate is to print index value and the value also
l=[10,20,30,40,50]
for i in enumerate(l):
    print(i)

y=["apple","banana","goa"]
x=enumerate(y)
print(list(x))


#  Nested list:
# if a list present inside a list is called nested list
l=[10,20,30,["divya","lasya","kavya"],40,50]
print(l)
print(l[1])
print(l[3])
print(l[5])
print(l[3][0])
print(l[3][1])
print(l[3][2])

# nested list in a matrix:
l=[[10,20,30],[40,50,60] ,[70,80,90]]
print(l)

# To print Row wise matrix:
print(l[0])
print(l[1])
print(l[2])
print(l[2][2])


# if we want to create a list from iterable objects like list,set,tuple,range,dict
# by using comprehension we can write in easy code
l=[]
for i in range(11):
    l.append(i)
print(l)

# by using comprehension we can write in single line:
l=[i for i in range(11)]
print(l)