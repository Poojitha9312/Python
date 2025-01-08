i=1
while i<=10:
    if i%2==0:
        print("number is even ", i)
    else:
        print("number is odd",i)
    i=i+1
    
#RUNTIME:
a=int(input("Enter Your  Startring Number :"))
b=int(input("Enter Your Ending Number :"))
while a<=b:
    if a%2==0:
        print("Your Number is even",a )
    else:
        print("Your Number is odd",a)
    a=a+1
# table number:
n=int(input("Enter Your Table Number :"))
i=1
while i<=12:
    print("%d * %d =%d"  %(n,i,n*i))
    i=i+1
# using string:
i=0
s="srinivasu"
while i<len(s):
    if s[i]=='u':
        break
    print(s[i])
    i=i+1
    
    
   