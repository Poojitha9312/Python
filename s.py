n=5
for i in range(n):
    for j in range(n):

        if i==0 or i==n//2 or i==1 and j==0:
            print("*",end=" ")
    for j in range(n):
        if i==n-1 or j==n-1 and i==3:
            print("*",end=" ") 
        else:
            print(" ",end=" ")       
  
    print( )
    