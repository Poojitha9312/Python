# jumping statements :
# jumping statements in python are used to after a flow of loop like you want to skip a part of loop or terminate a loop


# break
#break is used to terminate the loop
# syntax: break
for i in range(1,7):
    if i==4:
        break
    print(i)
    

# continue:
# It is uesd to skip the part of specific iteration
# syntax:  continue
for i in range(1,7):
    if i==4:
        continue
    print(i)

# pass: it is used to ignore
for letter in "python":
               if letter=="t":
                   pass
               print("This is pass block")
               print ("Current Letter :", letter)
               print( "Good bye!")


 



