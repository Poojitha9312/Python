# program 1:
for i in range(10):
    print(i)

# program 2:
for i in range(1,11,2):
    print(i)

for i in range(2,11,2):
    print(i)

# write  a program to print range of natural numbers n run time:
n=int(input(" Enter the number up to which you want to print natural numbers :"))
for i in range(n):
    print(i)

# write a program to print the characters in the string:
x=" rama krishna"
for i in x:
    print(i)

for i in range(0,10):
    print(i,end=" ")


# write a program to print the skipping characters from string:
a="snehitha"
n=len(a)
for i in range(0,n,2):
    print(a[i])
# program:
x=[" apple", " goa", "cherry"]
for i in x:
    print(i)
  
num=int(input("enter your number :"))
for i in range(1,16):
    print(f"  {num}  * {i}  ={num*i} ")

def hide_char():
    name="Rama"
    for i in name:
        if i=="a":
            continue
        print(i,end="")
hide_char()
    