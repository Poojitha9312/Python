l=[1,2,3,4,10,20,30]
for i in range(3,6):
   ele=eval(input(f" Enter the {i} th element of the list" ))
   print(l.insert(i,ele))
   print(l)