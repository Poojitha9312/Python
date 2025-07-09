# Why we are using dictionary:
# By using list,set,tuple we will store only values
# sometimes as s programmer we required to key and value as a pair
# in that case we can go for dictionary....

# what is dictionary?
# dict is a inbuild datastructure in python, it is used to store 
# key and value as a pair..{} is used in dict...

# # basic example:
d={"name":"snehitha","age":14,"school_name":"hamsavahini"}
print(d)
print(d["name"])


# characterstics of dict:
# dict is mutable in nature, so that we can do modifications..
# duplicate keys are not allowed, but duplicate values are allowed
# dict is dynamic in nature based on our req you can increase and 
# decrease the size..
# we cant apply indexing and slicing
# different types of dataitems allowed
# dict keys are case sensitive

# diff ways to create dict..
# creation of empty dict:
d={}
print(d)
print(type(d))

# creating a dict directly:
d={1:"snehi",2:"divya",3:"ruchi",4:"prasanthi"}
print(d)
print(d[3])

d={"name":"ram","age":15,"marks":[82,70,80,90],"pass":True,"adress":("kkd")}
print(d)

# duplicate keys are not allowed:
d={"name":"poojitha","Name":"snehi"}
print(d)

d={"name":"poojitha","name":"snehi"}
print(d)


# creation of empty dict using dict:
d=dict()
print(d)
print(type(d))

# Accessing the dict elements by using dict key:
# we can access the dict elements by using dict key
d={1:"pooji",2:"ruchi",3:"snehi"}
print(d)
print(d[3])
print(d[5]) # here it will show an key error...

# from sequence having each item as a pair 
d=dict([(1,"Apple"),(2,"Raju"),("Name","ravi")])
print(d)

d=dict(((1,"Apple"),(2,"Raju")))
print(d)

d=dict({(1,"Apple"),(2,"Raju")})
print(d)

# create a dict dynamically:
d={}
while True:
    key=input("Enter the Key :")
    value=input("Enter the value :")
    d[key]=value
    choice=input("Enter the choice you want to add more elements in to dictionary Y/N:")
    
    if choice=='N':
        break

print(d)

# check wheteher key existed or not:
d={1:"snehi","school_name":" hamsavahini","roll_no":26}
print(d)
print("school_name" in d)

# Accessing the dict elements using for loop:
d={1:"rama",2:"krishna"}
for i in d:
    print(i,d[i])
# here keys=i, value=d[i]

# Add and modification of dict elements:
d={1:"rama",2:"snehi"}
print(d)
d[3]="vasu"
print(d)
# modification:
d={1:"poojitha",2:"ruchi",3:"snehi",4:"lakshmi"}
print(d)
d[4]="lavanya"
print(d)
d[10]=25
print(d)# here we are modifying the elements using Key not indexnum..

# deleting a key value from dictionary:
d={1:"snehi","school_name":"hamsavahini","roll_no":26,"place":"kkd"}
print(d)
del d["place"]
print(d)

del  d   #entire dictionary deleted 
print(d)

# METHODS:
# get method:
# it is used to return the value associated with key..
# if the key is not there then it returns the default value...
d={"name": "rama","roll_no":25,"place":"kkd"}
print(d)
print(d.get("name"))
print(d.get(2))

# Items Method:
# it returns the both keys and value of dictionary..
d={1:"ram",2:"snehi",3:"ruchi"}
print(d.items())

# if we want one by one value:
d={1:"ram",2:"snehi",3:"ruchi"}
for i in d.items():
    print(i)

# pop() Method:
# it is used to remove the key and the value associated with it...
# it the key is not present it will raise an error...
# in dict pop method we have to give atleast one argument if we dont give it will raise an Typerror...
d={1:"ram",2:"snehi",3:"ruchi"}
print(d)
print(d.pop(1))
print(d)
print(d.pop())
print(d.pop(5))

#popitem Method:
# it is used to remove the last inserted item and returns the item in tuple format...
d={1:"ram",2:"snehi",3:"ruchi"}
print(d.popitem())
print(d)

# keys method:
# this method returns only keys in the form of list...
d={1:"ram",2:"snehi",3:"ruchi"}
print(d.keys())
for i in d.keys():
    print(i)

# values Method:
# This method returns the only values in the dictionary...
d={1:"ram",2:"snehi",3:"ruchi"}
print(d.values())
for i in d.values():
    print(i)

# setdefault Method:
# here as an argument we will provide key and value:
# it is used to return the value associated with that specific key
# if the key is not available then key and value will be added as a new item to the dictionary...
d={1:"ram",2:"snehi",3:"ruchi"}
print(d.setdefault(4,"harini"))
print(d)
d={1:"ram",2:"snehi",3:"ruchi"}
print(d.setdefault(2,"puji"))
print(d)

# update Method:
# suppose if we have two dictionaries...
# It is used to add all items d2 in d1 dict...
d1={1:"ram",2:"snehi",3:"ruchi"}
d2={4:"school_name",1:"teja"}
d1.update(d2)
print(d1)

#copy Method
#It is used to copy all the item from one dict to another dict.
d1={1:"Ram",2:"Krishna"}
d2=d1.copy()
print(d1)
print(d2)
print(id(d1))   #112233
print(id(d2))   #112234

#Both dict are pointing to different memory locations so if we will made any changes on any particular dictionary it will not reflect to another dict.

d1={1:"Ram",2:"Krishna"}
d2=d1   #assign
print(d1)
print(d2)
print(id(d1))  #112233
print(id(d2))  #112233

#clear Method
#It is used to remove all the items of a dict but then our dict will become empty.
d1={1:"Ram",2:"Krishna"}
print(d1)
d1.clear()
print(d1)

#fromkeys Method
#It is used to create a new dict from given iterable(list, tuple, range etc) and value(it is optional)

l=[10,20,30]
d=dict.fromkeys(l)
print(d)

t=(10,20,30)
d=dict.fromkeys(t)
print(d)

r=range(5)
d=dict.fromkeys(r)
print(d)

r=range(5)
d=dict.fromkeys(r,"Hello")
print(d)

r=range(3)
l=["Ram","Banti","Chanti"]
d=dict.fromkeys(r, l)
print(d)


#Count the No of occurance present inside the string.
s="Rama"
d={}
for i in s:
    d[i]=d.get(i, 0)+1
print(d)

for i, j in d.items():
    print(f'{i} is present {j} times')


#Access the elements from dictionary at run time
d={}
while True:
    name=input("Enter the name to get the place:")
    place=d.get(name)
    print(f"Hi {name} you are from {place}")
    
    choice=input("Do you want to search more[Y/N]:")
    
    if choice=="N":
        break



#Dictionary Comprehensions
d={i:i for i in range(0,5)}
print(d)
print(type(d))

d={i:i*i for i in range(0,5)}
print(d)
print(type(d))

l=[10,20,30,40]
d={i:3*i for i in l}
print(d)

name=["Rama", "Krishna","Gopal"]
d={i:len(i) for i in name}
print(d)

#Merging Dict Elements
d1={"Name":"Rama"}
d2={"Place":"Kakinada"}
d3={**d1, **d2}
print(d3)
    





