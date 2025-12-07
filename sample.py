i=1
while(i<10):
    print(i)
    i=i+1
    
# taking run time:
a=int(input("enter your a value:"))
while(a<=30):
    print(a)
    a=a+1
    
# write a program to print table:
n=int(input("enter your number:"))
i=1
while(i<=10):
    print(f"{n}*{i}={n*i}")
    i=i+1
    
# write a program to print stars:
i=1
while(i<10):
    print("*",end='')
    i=i+1

# write a program to print sum of n natural numbers:
i=1
sum=0
while(i<10):
    sum=sum+i
    i=i+1
print("the sum of natural numbers",sum)

# For-loop:
for i in range(10):
    print(i)
    
for i in range(1,11,2):
    print(i)
    
# write a program to print table:
n=int(input("enter your number:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
    
# write a program to print characters in string:
s=" ram krishna "
for i in s:
    print(i)
    

# write a program to print list items:
x=["apple","goa","banana"]
for i in x:
    print(i)


# nested loops:

# while loop:
i=1
while(i<=3):
    print(i)
    j=1
    while(j<=3):
        print(j)
        j=j+1
    i=i+1
    

# for-loop:
for i in range(1,11):
    for j in range(2,4):
        print(i*j,end=' ')
    print()


# patterns:
# low-high:
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
    
# jumping statements:
for i in range(1,7):
    if i==4:
        break
    print(i)

for i in range(1,7):
    if i==5:
        continue
    print(i)
    
    
for i in range(10):
    pass