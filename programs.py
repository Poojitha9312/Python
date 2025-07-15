# ----------Armstrong number--------------#
''' In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
'''

# Example:
n=int(input("enter n value:"))
m=n
s=0
while n>0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if s==m:
    print("given number is armstrong")
else:
    print("given number is not armstrong")

#--------Factorial of given number--------
'''The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one,0!=1 ''' 

# by using for loop:
n=int(input("enter n value:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(f"The factorial of {n} is {factorial}")



