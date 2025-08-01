try:
    print(1)
    print(2)
    print("File open code")
    print(4)
    print(10/0)
    print("File close code") #dont write clean-up code inside the try block because it can't execute
except FileNotFoundError as e:
    print(e)
finally:
    print("Finally Block executed")