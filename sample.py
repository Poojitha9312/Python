from sample1 import  *
import os

if os.path.exists('sample1.txt'):
    with open('sample1.txt', 'r') as file:
        print("File content:\n", file.read())
else:
    print("The file does not exist.")