n=int(input("enter n value:"))
factorial=1
i=1
while i<=n:
    factorial=factorial*i
    i=i+1
print(f"The factorial of {n} is {factorial}")