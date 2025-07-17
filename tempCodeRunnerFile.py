def sample():
    yield 1
    yield 2
    yield 3
x=sample()
print(type(x))
for i in x:
    print(i)