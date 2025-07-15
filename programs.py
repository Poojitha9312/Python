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



