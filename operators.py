# operator: operator is a special symbol which performs operations on  two operands
# a=20
# b=10
# c=a+b
# print(c)
# Arithmetic opertaor:(+,-,*,/,%,//,**)
# 1. Addition(+)
a=20
b=10
add=a+b
print(add)

# 2. subtraction(-)
a=20
b=10
sub=a-b
print(sub)

#3. Multiplication(*)
a=20
b=10
mul=a*b
print(mul)

#4.division(/)   (Quotient)
div=a/b
print(div)

# 5.Modulus(%)  (reminder)
mod=a%b
print(mod)


# 6.Floor division:(//)
fdiv=a//b
print(fdiv)

# 7.exponential
pow=a**b
print(pow)


#2.comparision operator  (<,>,<=,>=,==,!=)
x=5
y=10

if x<y:
    print(" x is less than y")

if y>x:
    print(" y is greater than x")

if x<=y:
    print(" x is lessthan or equal to y")

if y>=x:
    print(" y is greaterthan or equal to x ")

if x==y:
    print(" x is equal to y")

if x!=y:
    print(" x is not equal to y")
    
# 3. Assignment operator (=,+=,-=,/=,//=,**=)
x=10
print(x)

x=10
x+=3
print(x)

x=13
x-=3
print(x)

x=10
x/=3
print(x)

x=3
x//=3
print(x)

x=3
x**=3
print(x)


# 4.logical operator  (and,or,not)
a=10
b=20
c=a>9 and b>19
print(c)

a=10
b=20
c=a>9 or b>20
print(c)

a=10
b=20
c=not a>9 or b>20
print(c)

# 5.memebership operator (in, not in)
x=["apple","banana"]
print("apple" in x)

x=["apple", "banana"]
print(" pineapple"  not in x)


#6.Identity operator:(is,is not)
x=["apple","banana"]
y=["apple","banana"]
z=x

# if the two variables are not pointing to same address location then is not operator returns true otherwise it returns false
print(x is not z)
print(x is not y)


 #is means two variables are pointing to same address location then is operator returns true otherwise it returns false
print(x is z) 
print(x is y)

#7.bitwise operator: (a&b,a|b,a^b)
a=10
b=8
# a&b = 1000
print(a&b)

# a|b = 1010
print(a|b)

# a^b = 0010
print(a^b)