l=['h','e','r','a','r','s','p','k']
def sample(y):
    vowels=['a','e','i','o','u']
    if (y in vowels):
        return True
    else:
        False
r=list(filter(sample,l))
print(r)
print(type(r))