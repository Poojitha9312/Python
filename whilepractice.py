# basic program:
while True:
    print("this is true")

while False:
    print(" this is false")
else:
    print(" this is else")

# second program:
i=1
while i<=10:
    print(" value of i is :", i)
    i=i+1
else:
    print("loop ends now")

# third program:
a=int(input("enter a value:"))
while (a<=30):
    print(" value of a is :", a)
    a=a+1


# write a program to print table:
i=1
n=int(input(" Enter the n value :"))
while i<=10:
    print(f"{n} *{i} ={n*i}")
    i=i+1
else:
    print(" loop ends now")

# wap to print stars:
i=1
while i<10:
    print("*", end=' ')
    i=i+1

# wap to print sum of N natural numbers:
i=1
sum=0
while i<10:
    sum=sum+i
    i=i+1
print(" The sum of N natural numbers is :", sum)

# using else with while loop:
i= int(input(" Enter i value :"))
while i<10:
    print(i)
    i=i+1
    if i==9:
        break
else:
    print(" while loop is exhausted")

# using string to print characters:
y="poojitha"
i=0
while i<len(y):
    print(y[i])
    i=i+1
    if y[i]=='t':
        break


