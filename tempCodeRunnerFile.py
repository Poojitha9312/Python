class Myclass:
    pass

print(issubclass(Myclass,object)) # True because Myclass is a subclass of object.

a=Myclass()
print(isinstance(a,object))