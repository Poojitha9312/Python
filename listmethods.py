# list Methods:
# append,insert,copy,clear,sort,reverse,remove,pop,index,extend,count


# 1. append() : it adds an element to the end of the list
l=[10,20,30,40]
print(l)
l.append(50)
print(l)
l.append(70)
print(l)


#2. insert(): 
# by using append function we add elements to end of list, there is a drawback in that method. if we want to add
# element at the specified location then we use insert method in python... here location means index value...
l=[10,20,30,40,53,63]
print(l)
l.insert(3,89)
print(l)
l.insert(1,100)
print(l)


# if we given index value crossed the maximum index value in the list, then it will be added at the end of the list.
# then it will acts as an append..what append will do add element to end of list...if we give negative index it will
# added to starting of the list

l=[10,20,"snehitha",40,50,60]
print(l)
l.insert(10,100)
print(l)
l.insert(-15,25)
print(l)

# updating the list elements by using insert method:
l=[10,20,30,40,50,60,70]
for i in range(3,6):
    ele=eval(input(f" Enter the {i}  th  element of the list :"))
    l.insert(i,ele)
    print(l)


# 3. count():
# it is used to count an element presence number of times in the list
l=[10,20,"snehitha","poojitha",4.2,10,10,30,40,40,40,50]
print(l)
print(l.count(30))
print(l.count(40))


# we want to count multiple values go for for iteration:
l=[10,20,30,10,40,10,50,10,30,10]
num=int(input(" Enter your number :"))
count=0
for i in range(len(l)):
    if l[i]==num:
        count=count+1
print(count)

# 4.index():
# it is used to return the index value of specific element
l=[20,10,10,30,40,50,63,73,83]
print(l)
print(l.index(10))
print(l.index(83))
 
# Note:  if an element 3 times in the list , then the index value returns the lowest value index

# using while loop in index method:
l=[10,20,30,10,40,50,10,60,70,80]
i=0
count=0
search=int(input(" Enter  the value you want to search :"))
while i<len(l):
    if l[i]==search:
        print(f"The {search} value is present at the inex valueis {i} ")
        count=count+1
    i=i+1
print(f"the {search} value count is {count} times ")

# for loop:
l=[1,2,3,1,2,4,5,6,1,2]
index=[]
n=int(input(" enter your number :"))
for i in l:
    if i==n:
        index.append(i)
        
print(len(index))


 # 5. Remove():
# It is used to remove the specific element  from the list
# if the specified element present multiple times , then it will remove first occorrence
l=[10,20,30,40,50,10,60,10,70]
print(l)
l.remove(20)
print(l)

# using for loop in remove:
l=[10,20,30,40,50,10,60,10,70]
print(" printing the original list")
for i in l:
    print(i,end=" ")
l.remove(20)
print(" printing the list after removal of 20 element")
for i in l:
    print(i,end="  ")



# 6.pop():
# by default it will remove the last element, but if we want to remove an specific element then we will provide specific
# element index value
l=[10,20,30,40,50,60,70,80,90,100]
l.pop()
print(l)
l.pop(2)
print(l)

# using for iteration  to pop the index value
l=[10,20,30,40,50]
n=int(input(" Enter your number :"))
for i in l:
    l.pop(n)
    break
print(n)
print(l)

# difference between remove and pop:
# the main difference is in remove method if we want to  remove specific element then we have to give 
# element value..... but in pop we have to give index value of the specific element.......

# 7.Extend(): extend means expand
# It is used to add all the elements of the list to another list



# 8. reverse(): 
# it is used to reverse the elements
l=[10,20,30,40,50]
print(l)
l.reverse()
print(l)

# 9.sort():
# It is used to print elements either ascending order or descending order
l=[2,4,3,1,5,8,7]
l.sort()
print(l)

# if we want to print in descending order 
l=[1,2,3,4,5,6,7,8]
l.sort(reverse=True)
print(l)


# using for loop
l=[2,4,3,1,5,8,7]
i=0
for i in l:
    l.sort()
print(l)

# using while loop:
l=[1,2,3,4,5,6,7,8]
i=0
while i<len(l):
    l.sort(reverse=True)
    i=i+1
print(l)

# sort method to print alphabetics in ascending  order:
l=["goa","banana","mango","apple"]
l.sort()
print(l)

# sort method  to print alphabets in descending order:
l=["apple","banana","carrot", "mango","strawberry" ]
l.sort(reverse=True)
print(l)


# if list contains the string values also:
# l=[1,3,5,2,"snehitha","poojitha"]
# l.sort()
# print(l)



# 10. clear(It is used to clear all the elements in the list)
l=[10,20,30,40,50]
l.clear()
print(l)

 # 11.del:
# It is used to delete the  specific elements in the list by using index value
l=[5,15,25,35,45]
print(l)
del l
print(l)

l=[10,20,30,40,50]
print(l)
del l[2]
print(l)


# 12. copy Method:
# It is used to copy of list. In copy Method if we made any modification in the new list
# it wont be reflected in the original list,both are in different location
l=[10,20,30,"snehitha",8.2,"lakshmi"]
p=l.copy()
print(p)
print(id(l))
print(id(p))
# # if we made any modification
p[2]=25
print(p)
print(l)

# note: if we assign (means equal one list to another list)  if we made any changes it will reflect both
# l=[10,20,30,40,50]
v=l
print(l)
print(v)
# note: if we assign the list to another list
print(id(l))
print(id(v))

v[3]=15
print(v)
print(l) # here we can observe modification refelects in the original list also


# 13.concatenation of list:
# jointing of list is known as concatenation
# Here we can use + symbol to joint the list
l=[10,20,30]
p=["poojitha"," snehitha"]
v=l+p
print(v)
# here we also joint multiple list, but we cant joint a integer value to list(s=10)

# 14. Repetition of list:
# It will  repeat list  by specified number of times
# * is uesed for repetition of list
l=[10,20,30]
v=l*3
print(v)

# 15. sum Method:
l=[1,2,3,4]
print(sum(l))


# length Method:
l=[1,2,3,4]
print(len(l))

# write a program to print elements in the list along with positive index and negative index value:
l=[10,20,33,45,51,61]
n=len(l)
for i in range(n):
    print("  {}   at present index is {}  /  {}".format((l[i]),i,i-n))

# updating the list elements:
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