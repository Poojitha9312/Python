from itertools import accumulate
result=list(accumulate([1,2,3,4,5],lambda a,b:a+b))
print(result)