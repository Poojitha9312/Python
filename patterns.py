n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()



 # program to print *  in row format:
n=5
for i in range(n):
    for j in range(i+1):
        print(i,end=" ")
    print()


# low-high: n=0,1,2,3,4
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


# high-low:
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

# low-high(spaces) and high-low(*):
n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print() 

   


   


