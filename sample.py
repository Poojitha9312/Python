name="snehitha"
age=13
print("My name is ", name, "My  age is ", age)
print("My name is %s and My age is %d" %(name,age))
print("My name is {}  and My age is {}".format(name,age))
print(f"My name is {name} and My age is {age}")

x=int(input("Enter Your Number :"))
print(x)
y=int(input("Enter Your Number :"))
print(y)
z=x+y
print(f"The addition of {x}  and {y}  is {x+y}")
#Relational operator:
x=35
y=45
a=(x>y)
print(a)
b=(x<y)
print(b)
c=(x>=y)
print(c)
d=(x<=y)
print(d)
e=(x==y)
print(e)
f=(x!=y)
print(f)

#Logical operator:
#and , or ,not 
a=35
b=50
x=a<b and a>b
print(x)
y=a>=b and a!=b
print(y)
z=a<=b or a==b
print(z)
g=a>=b or a!=b
print(g)


