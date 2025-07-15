s=open('zsample.py',mode='w+')
print(s.tell()) #tell is used to know the current cursor pointer place
s.write("w+ mode")
print(s.tell())
s.seek(0) #seek is used to Move the file pointer to a specific position.
print(s.tell())
print(s.read())
s.close()