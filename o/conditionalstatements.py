# Conditional statements : conditional statements are also known as decision making statements...
# we need to use this conditional statements to execute the block of code if the given condition is true or false
# Following are conditional statements:
#                        1) if
#                        2) if-else
#                        3)if-elif
#                        4) nested if
#                        5) shorthand-if
#                        6) shorthand-if-else


# 1) If : If statement is the most simple decision making statement. It is used to whether the certain 
# block of code executed or not

# syntax :
# if (condition):
#        statement execute if  block condition is true

# basic program
if (5>2):
    print("this is if")

# write a program to print largest number:
a=int(input("Enter a value :"))
b=int(input("Enter b value  :"))
c=int(input(" Enter c value :"))
if a>b and a>c:
    print(" a is big")
if b>c and b>a:
    print(" b is big")
if c>a and c>b:
    print(" c is big")


# 2) If-else: The if statement tells us that if condition is true it will execute the specfic block of code
# otherwise it wont...but if we want to do something else if the condition is false, then we use else statement

# syntax: 
# if (condition):
#           execute this if block condition is true
#else:
#   execute this block if condition is false'''

# basic program:
if 5<2:
    print(" this is if")
else:
    print(" this is else")

# # write a program to print large number:
a=int(input(" Enter a value :"))
b=int(input(" Enter b value :"))
c=int(input(" Enter c value :"))
if a>b and a>c:
    print(" a is big")
elif b>c:
    print(" b is big")
else:
    print(" c is big")

# # write a program to print even or odd:
n=int(input(" Enter your value :"))
if n%2==0:
    print(" you have given even number")
else:
    print(" you have given odd number")

# # write a program to check whether the person is eligible to vote or not:
age=int(input("Enter your age :"))
if age>=18:
    print(" You are eligible to vote now")
else:
    print(" you have to wait")


# if-elif:
if 5<2:
    print("this is if")
elif 5<2:
    print(" this is elif") 
else:
    print(" this is else")

# write a program to print student marks:
marks=int(input(" Enter your marks :"))
if marks>85 and marks<100:
    print(" congrats you have scored A+grade")
elif marks>65 and marks<=80:
    print("You have scored  A grade")
elif marks>45 and marks<=60:
    print(" you have scored B grade")
elif marks>30 and marks<=40:
    print(" you have scored C grade")
else:
    print(" sorry you are fail")


# calculator program:
a=int(input(" Enter a value :"))
b=int(input(" Enter b value :"))
print(" press the \n + to add \n - to sub \n * to muln  \n /to div")
choice=input(" Enter your choice")
if choice=='+':
    print(a+b)
elif choice=='-':
    print(a-b)
elif choice=='*':
    print(a*b)
elif choice=='/':
    print(a/b)
else:
    print(" choose correct option")

# nested-if:
x=int(input("Enter your x value :"))
if x>10:
    print("  x is above ten")
    if x>20:
        print(" x is above 20")
    else:
        print(" x is not above 20")
else:
    print(" All above cases are failed")

# shorthand-if:
a=20
b=10
if a>b: print(" a is big")

# shorthand-ifelse:
a=20
b=10
print(" a is big") if a>b else print(" b is big")


