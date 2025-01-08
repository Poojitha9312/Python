i=1
while i<=10:
    print(i,end=" ")
    i=i+1
# Runtime:
a=int(input("Enter Your Number :"))
b=int(input("Enter Your Number :"))
while a<=b:
    print(a)
    a=a+1
i=1      


while i<=10:
    if i%2==0:
        print("This is Even Number",i)
    else:
        print("This is Odd Number :",i)
    i=i+1
# Runtime:
a=int(input("Enter Your Start Number:"))
b=int(input("Enter Your End Number:"))
while a<=b:
    if a%2==0:
        print("This is Even Number",a)
    else:
        print("This is Odd Number:")
    a=a+1
#  Table Number:
n=int(input("Enter Your Number :"))
i=1
while i<=15:
    print("%d * %d =%d" %(n,i,n*i))
    i=i+1
# using if-else in while loop:
i=int(input("Enter Your Number :"))
while i<=12:
    print(i,end=" ")
    if i==10:
        break
    i=i+1
i=int(input("Enter your Number:"))
b=int(input("Enter Your Number :"))
while i<=b:
    print(i,end=" ")
    if i==15:
        break
    i=i+1
# Using String tp print characters:
i=0
a="Ramalakshmi"
while i<len(a):
    if a[i]=='h':
        break
    print(a[i],end=" ")
    i=i+1
i=1
while i<10:
    print("*",end=" ")
    i=i+1
# To print sum of N natural Numbers:
i=1
sum=0
while i<10:
    sum=sum+i
    i=i+1
    print("sum is :", sum)
    print(i)
 