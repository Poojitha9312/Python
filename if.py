a=8
b=9
c=10
print(a)
print(b)
print(c)
if a>b & a<c:
    print("a is big")
if b>c  & b<a:
    print("b is big")
if c>a &  c<b:
    print("c is big")
    
# runtime:
a=int(input("Enter Your Number :"))
b=int(input("Enter Your Number :"))
c=int(input("Enter Your Number :"))
if a<b & a<c:
    print("a is big")
if b>c & b<a:
    print("b is big")
if  c>a & c>b:
    print(" c is big")