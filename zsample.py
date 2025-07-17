def add(a,b):
    yield a+b
    yield a-b
    yield a*b
x=add(10,20)
print(x.__next__())
print(x.__next__())
print(next(x))

