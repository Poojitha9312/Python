s="srinivasu"
for i in s:
    print(i,end=" ")
n=int(input("Enter Your Number:"))
for i in range(1,16):
    print("%d *%d = %d" %(n,i,n*i))
s="ramalkashmi"
n=len(s)
for i in range(0,n):
    if s[i]=='i':
        break
    print(s[i],end=" ")   