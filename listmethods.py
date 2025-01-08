#append: It adds an element to the last of the index
l1=["Pink","blue","skyblue"]
l1.append("green")
print(l1)

# insert: It adds an element at defined index value:
l1=["pink","red","orange"]
l1.insert(2,"black")
print(l1)

#extend: It adds elements of one list to another list:
l1=[1,2,3,4,5]
l2=[6.7,8]
l1.extend(l2)
print(l1)

#remove: It removes an element from list:
l1=["apple","banana","grapes","strawberry","goa"]
l1.remove("grapes")
print(l1)

#pop: It removes and returns an element at the given index:
l=["telugu","social","maths","english","hindi"]
l.pop(2)
print(l)


#clear: It clears all the elements in the list:
p=["blue","yellow","green"]
p.clear()
print(p)

#index: It returns the index value of the element:
p1=["telugu","social","hindi","english","maths"]
print(p1.index("hindi"))

#count:

p2=["goa","banana","apple","grapes","goa"]
print(p2.count("goa"))

# reverse:
l1=[1,2,3,4,5,6]
l1.reverse()
print(l1)

#sort:
l2=["red","blue","pink","yellow","skyblue"]
l2.sort()
print(l2)

#copy:
l1=[1,2,3,4]
l2=l1.copy()
print(l2)



