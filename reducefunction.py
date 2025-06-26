#Reduce function:
'''The reduce() function receives two arguments, a function and an iterable. However, it doesn't return another iterable, instead it returns a single value.
Reduce function present inside the functools, so we have to import it before using reduce function.'''

# adding sum of all elements in the list....
from functools import reduce
l=[1,2,3,4,5]
def sample(a,b):
    return a+b
r=reduce(sample,l)
print(r)
print(type(r))

# By  using lambda function:
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda a,b:a+b,l))


# finding out square of all elements in the list by using lambda function......
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda a,b:a*b,l))

#Difference between reduce and accumulate
'''
reduce gives final output but accumulate gives iterable output
accumulate syntax:(iterable,function)
'''
#reduce example
from functools import reduce
result=reduce(lambda a,b:a+b,[2,3,4,5])
print(result)

#accumulate example
from itertools import accumulate
result=list(accumulate([2,3,4,5],lambda a,b:a+b))
print(result)