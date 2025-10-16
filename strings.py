# what is string?
# string can be defined as sequence of characters represented in quotation marks
a="hietechsolutions"
print(a)

print(type(a)) #we can use '' or "" or ''' ''' or """ """
# in python strings are immutable.....

#Accessing The elements of a string
#We can access elements of a string by using 1.Index 2.Slice Operator

#1.Index
#We can access the elements by positive and negative index as well.
s1="Welcome to python"
print(s1[3])
print(s1[7])
print(s1[8])
print(s1[-1])

#2.Slice Operator
#Slice represet a part of a string
s1="Welcome to python"
print(s1[1:5])
print(s1[0:10:2])
print(s1[::])
print(s1[::2])
print(s1[:8:2])
print(s1[-5:-1])
print(s1[-10:-1:2])
print(s1[::])
print(s1[::-2])
print(s1[:-8:-2])

# string methods:
# checking starting and ending of string:
s1="welcome python"
print(s1.startswith("welcome"))
print(s1.startswith("Welcome"))
print(s1.endswith("python"))
print(s1.endswith("Python"))

# checking what type of character present in given string
# 1.isalpha()
s1="welcomepython"
print(s1.isalpha())

s1="welcome python"
print(s1.isalpha())

# here it returns false becuase spaces are given in string

s1="Welcomepython"
print(s1.isalpha())

# 2.isalnum()
# if it contains alphabets and numericals it returns true
# if it is containing only numbers otherwise alphabets then also
# it will return true
s="1helloworld"
print(s.isalnum())

s="1245"
print(s.isalnum())

s="python"
print(s.isalnum())


#3.isdigit()
# if it contains only digits then only it will return true
s="1234"
print(s.isdigit())

s="123hai"
print(s.isdigit())

# 4.islower
s="hello"
print(s.islower())

s="123hello"
print(s.islower())

s="Hello"
print(s.islower())

# 5.isupper()
s="HELLO"
print(s.isupper())

s="hELLO"
print(s.isupper())

s="123HELLO"
print(s.isupper())

# 6.istitle
# istitle means first letter should be capital
s="Ramakrishna"
print(s.istitle())

#7.isspace:
s="  "
print(s.isspace())

s=" . "
print(s.isspace())

# changecase methods:
#1.upper
s="welcome to python"
print(s.upper())

# 2.lower:
s="WELCOME"
print(s.lower())

# 3.swapcase:
# here swap means it will give when it is lower it returns upper
# when it is upper it returns lower
s="welcome python"
print(s.swapcase())

#4.title
# Each word start with capital
s="Welcome python programming"
print(s.title())

# 5. capitalize
#First word will be in capital
s="hai python"
print(s.capitalize())

# Length:
s="WELCOME TO PYTHON"
print(len(s))

# count:
s1="Hello World"
print(s1.count('o'))
print(s1.count('o',6)) #starts from 6th index

# replacement of string:
# replace
s1="Hello World"
b=s1.replace("World","divya")
print(s1)
print(b) #original string cannot replace because it is immutable

# split Method
s1="Hello World"
print(s1.split())  #It returns a list
print(s1.split('o'))  #It split while 'o' comes

#Join Method
s1="Hello World"
print('*'.join(s1))    # H*e*l*l*o* *W*o*r*l*d

s1=["Hello", "World"]
print('*'.join(s1))    # Hello*World

s1=("Hello", "World")
print('.'.join(s1))    # Hello.World

#strip Method (Remove space from string)
s1="  Rama  "
print(s1)
print(len(s1))
print(len(s1.strip()))
print(s1.strip())

#Fill Method
s1="Rama"
print(s1.zfill(6))
  #Here zfill is 6 and s1 is 4 then 6-4=2 it gives 2 zeros
  # output:00Rama

#rjust method
s1="Rama"
print(s1.rjust(8))
#Here rjust is 8 and s1 is 4 then 8-4=4 it gives 4 spaces moves the s1 to right

s1="Rama"
print(s1.rjust(7, "*")) # ****Rama

s1="Rama"
print(s1.ljust(7, "*"))  # Rama****

#Center Method
s1="Rama"
print(s1.center(7,"*"))

s1="Rama"
print(s1.center(12,"*"))# ****Rama****

#enumerate method
s1="Rama"
for i in enumerate(s1):
    print(i)





