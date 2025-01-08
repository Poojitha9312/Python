a=10
b=20
if a>b:
    print("a is big")
else:
    print(" b is big")
    
#Runtime:
a=int(input("Enter Your Number :"))
b=int(input("Enter Your Number :"))
if a<b:
    print("b is big")
else:
    print("a is big")
    
# compile time:
a=10
b=20
c=30

if a>b & a>c:
    print(" a is big")
elif b>c:
    print("b is big")
else:
    print("c is big")
# Runtime:
a=int(input("Enter Your Number :")) 
b=int(input("Enter your Number :")) 
c=int(input("Enter Your Number :"))
if a>b & a>c:
    print("a is big")
elif b>c:
    print("b is big")
else:
    print("c is big")