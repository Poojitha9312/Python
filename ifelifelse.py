marks=int(input("please Enter Your marks :"))
if marks>85 and marks<100:
    print(" Your Grade is A")
elif marks>60 and marks<85:
    print("Your Grade is B")
elif marks>50 and marks<40:
    print("Your Grade is c")
else:
    print("You are fail")
    
#calculator program Runtime:
a=int(input("Enter Your Number :"))
b=int(input("Enter Your Number :"))
print(" press the \n + to add \n - to sub \n to *mul \n / to  div")
choice=input("Enter your choice :")
if choice=="+":
    print(f"The addition of {a} and {b} is {a+b}")
if choice=="-":
    print(f"The Substraction of {a} and {b} is {a-b}")
if choice=="*":
    print(f"The multiplication of {a}  and {b} is {a*b}")
if choice=="/":
    print(f"The Division of {a} and {b} is {a/b}")

