def add(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
    yield a%b
    yield a+20
    yield b+40
    yield a-2
    yield a+1
x=add(10,20)
print(type(x))
# here x is an generator object
print(x.__next__())
print(next(x))
print(next(x))
print(next(x))