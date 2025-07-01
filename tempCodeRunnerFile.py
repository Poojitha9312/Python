l=[10,20,30,40,50,10,60,10,70]
print(" printing the original list")
for i in l:
    print(i,end=" ")
l.remove(20)
print(" printing the list after removal of 20 element")
for i in l:
    print(i,end="  ")
