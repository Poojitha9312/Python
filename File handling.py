# File handling is an essential concept that allows you to read from and write to files. Python provides built-in functions to handle files in an easy and efficient way. 
# '''

#Create a sample file sample1.py and create the below text
# Hello Welcome to python.

#Now do operations on demo.txt
#Example:
''' open   read   close'''
s=open('sample1.py',mode='r')
print(s.read())
s.close()

#Example:
''' open write close'''
s=open('sample1.py',mode='w')
s.write("Bye Bye")
s.close()

#Example
''' open append close'''
s=open('sample1.py',mode='a')
s.write("Bye Bye append")
s.close()

#Example:
''' open read and write close'''
s=open('sample1.py',mode='r+')
print(s.read())
s.write("r+ mode")
s.close()

#Example:
''' open write and read close'''
s=open('sample1.py',mode='w+')
print(s.tell()) #tell is used to know the current cursor pointer place
s.write("w+ mode")
print(s.tell())
s.seek(0) #seek is used to Move the file pointer to a specific position.
print(s.tell())
print(s.read())
s.close()

