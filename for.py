n="srinivasu"
for i in n:
    print(i,end="")
#
n=int(input("Enter Your Table Number :"))
for i in range(1,16):
    print("%d * %d  =%d" %(n,i,n*i))
for i in range(1,11):
    print("*",end=" ")
s=["snehitha","poojitha","Bujji babu"]
for i in s:
    print(i)
s="poojitha"
n=len(s)
for i in range(0,n):
    if s[i]=='h':
        break
    print(s[i])
s="poojitha"
n=len(s)
for i in range(0,n,2):
    print(s[i])
    




