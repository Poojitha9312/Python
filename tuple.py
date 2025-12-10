# tuple is an  inbuild datastructure in python..It is similar to list data structure but the main difference is 
# tuple is immutable in nature while list is mutable in nature........
# tuple is immutable in nature once we create tuple object we cannot made any modifications on it...
# () paranthesis symbol is used to create tuple...


# creation of empty tuple():
t=()
print(t)
print(type(t))


# creation of tuple with single value:
t=(10)
print(t)
print(type(t))
 # here single value cannot taken as a tuple it will takes it as a integer......


t=(10,)
print(t)
print(type(t))
# here by putting , comma with single value then it will be a tuple......


# creation of tuple with different data items:
t=(10,"ram",8.2,20,False)
print(t)
print(type(t))

# creation of tuple  without using paranthesis:
t=10,20,"ram",8.2,60
print(t)
print(type(t))


# convertion of list elements to tuple elements by using tuple function:
l=[10,20,30,40,50]
t=tuple(l)
print(t)
print(l)

# # characterstics of tuple:
# tuple is immutable in nature
# tuple maintaining order
#tuple can hold different data items
#  duplicate elements are allowed
# () paranthesis is optional but it is recommended
# tuple supports both positive and negative index


 # we can acess the tuple elements using positive inedx, negative index, also using slicing....
t=(10,20,"ram",5.6,30)
print(t)
print(type(t))
print(t[0])
print(t[4])
print(t[-1])
print(t[-3])
print(t[::])
print(t[1:4])
print(t[-1:0:-3])


# # creation of tuple elements using eval() function:
t=eval(input("enter tuple elements:"))
print(t)



# creation of tuple using range function:
t=tuple(range(11))
print(t)
print(type(t))
for i in t:
    if i==8:
        break
    print(i)

# creation of tuple using string:
a="welcome to HIETECH SOLUTIONS"
print(a)
t=tuple(a)
print(t)
print(type(t))


# Accessing elements by using nested tuple:
t=(10,20,30,[1,2,3],(40,50,60))
print(t)
print(t[0])
print(t[1])
print(t[3][0])

print(t[4] [2])

# modifying tuple elements:
t=(10,20,30,"poojitha")
print(t)
t[2]=98
# print(t)  # Here it shows an error because in tuple we cannot modify the elements, tuple is immutable

x=("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# concatenation:
# here + symbol is used to combine two tuples...This is called Concatenation
t=(10,20,30)
l=(1,2,3)
s=(" divya","snehi", "ruci")
p=t+l+s
print(p)


# Repetition:
# We can also repeat the elements in a tuple for a given number of times using the * operator.
# Both + and * operations result in a new tuple.'''

t=(10,20,30)
l=t*3
print(l)


# # traversing tuple elements with for loop:
t=(10,"pooji","snehi",50,60)
for i in t:
    print(i)


# # Traversing list elements using while loop:
t=(1,2,3,8.2,"pooji",False)
i=0
while i<len(t):
    print(t[i])
    i=i+1

# using len method:
t=(10,20,30,"pooji")
print(len(t))


# using Min Method:
t=(1,2,3,40,50,60)
print(min(t))


# using Max Method:
t=(10,20,30,40,50)
print(max(t))

# using sort Method:  Ascending order
t=(10,20,3,50,60,1)
l=sorted(t)
print(l)

# sort method : descending order
t=(90,20,1,3,5,8)
l=sorted(t,reverse=True)
print(l)

# deleting tuples:
t=(10,20,30,40)
del t[1]
# Type error: tuple doesn't supprot object deletion
# we cant del entire tuple also

# packing in tuple:
a=10
b=20
c=30
d="pooji"
e=8.2
t=a,b,c,d,e
print(t)
print(type(t))

# unpacking tuple:
t=("ram",10,20,30,8.2)
a,b,c,d,e=t
print(a,b,c,d,e)
# At the time of unpack no.of variables and no.of values must be same

# Inbuilt tuple methods:
t1=(10,20,30,50)
t2=(10,20,30,40)
print(t1==t2)
print(t2<t1)




