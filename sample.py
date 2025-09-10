n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


# low-high:
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#high-low:
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()