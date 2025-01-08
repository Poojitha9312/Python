a=int(input("Enter Your Number :"))
if a>20:
    print("a is above 20")
    if a>30: print("a is also above 30")
    else:
        print("not above 30")
else:
    print("all statements are failed")
# shorthand ifelse:
a=5
b=10
print("A is small")if a<b else print("b is big")