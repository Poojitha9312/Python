#----------------- Assertion------------------------
'''
--->Assert is keyword in python which is used for debugging.
--->Debugging is the process of finding and fixing bugs.
--->If we want to verify something then we can use assertion.
'''

#Example:
a=100
print(1)
print(2)
assert a==100 #If the cond is true then execute next code, If it is false raise exception and stop the flow of execution.
print(3)
print(4)

#Example:
a=100
print(1)
a=20
print(2)
assert a==100  #AssertionError because a is updated to 20
print(3)
print(4)

#Example: By default Assertion Not gives any message in this example we will give Message
a=100
print(1)
a=20
print(2)
assert a==100," a value is updated" #message
print(3)
print(4)

#Example:If u want to give dynamic result
password=100
print(1)
password=20
print(2) 
assert password==100,f"AssertionError because password is updated to {password}"
print(3) 
print(4)

#Example:
x = 5
assert x > 0, "x should be positive"
assert x < 3, "Sorry X is not less than 3"

#Example:
l=["Ram","Gopi","Seetha"]
assert input("Enter your name:") in l, "This name is not present"
print(l)

#Example:
l=["Ram","Gopi","Seetha"]
try:
    assert input("Enter your name:") in l, "This name is not present"
except AssertionError as e:
    print(e)
print(l)

