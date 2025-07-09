s=open('zsample.py',mode='w+')
print(s.tell()) #Cursor position
s.write("Bye")
print(s.tell())
s.seek(0) 
print(s.tell())
print(s.read())
# s.close()