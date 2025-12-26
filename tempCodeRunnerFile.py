a = 10
def sample():
    a = 20
    print(a)              # local
    print(globals()['a']) # global

sample()