for i in range(10):
    print(i)

# start , stop, skip value:
for i in range(1,11,2):
    print(i)

n=int(input(" enter your number"))
for i in range(n):
    print(i)

n=int(input(" enter number :"))
for i in range(1,11):
    print(f" {n} * {i}= {n*i}")

a="ramalakshmi"
for i in a:
    print(i)

a="poojitha"
n=len(a)
for i in range(0,n,2):
    print(a[i])

x=[" apple", " goa", "banana"]
for i in x:
    print(i)

def hide_char():
    name="rama"
    for i in name:
        if i=='a':
            continue
        print(i,end='')
hide_char()