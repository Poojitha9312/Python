# filter function:
# filter function is used to filter value in a sequence...
# filter function is a higher order function that means 
# if a function takes function as a argument...

# syntax of filter function:
# filter(function,sequence)
# argument function should return either true or false...
#function: 
'''function that tests if each element of a sequence true or not.'''
#sequence:
'''sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.'''
# NOTE:filter gives true output only

# write a program to print even in a list by using filter function
def even(y):
    if y%2==0:
        return True
    else:
        return False
l=[10,15,30,27,92,46]
r=list(filter(even,l))
print(r)
print(type(r))
for i in r:
    print(i)

# here it is an iterable object so we can use for loop

# second program using lambda function:
# write a program to print even in a list using lambda function
l=[10,20,30,77,51,97]
r=list(filter(lambda y:y%2==0,l))
print(r)
print(type(r))
for i in r:
    print(i)

# if we want to print in set format:
l=[10,20,30,77,51,97]
r=set(filter(lambda y:y%2==0,l))
print(r)
print(type(r))
for i in r:
    print(i)

# By using lambda function we can write in single line also:
l=[10,20,30,47,56,21]
print(list(filter(lambda y:y%2==0,l)))


#WAP to print the vowels is present in the specific elements with filter.
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


# WAP to print the vowels is present in the specific elements with filter by using lambda
l=['h','e','r','a','r','s','p','k']
vowels=['a','e','i','o','u']
r=tuple(filter(lambda y: y in vowels,l ))
print(r)
print(type(r))
for i in r:
    print(i)

# By using lambda function can write in single line:
l=['h','e','r','a','r','s','p','k']
print(list(filter( lambda y:y in ['a','e','i','o','u'],l)))

# Another way using lambda function:
print(list(filter(lambda i:i in ['a', 'e', 'i', 'o', 'u'],['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'])))

# write a program to print even items from dictionary:
d={1:"ram",2:"krishna",3:"ruchi",4:"ramya"}
def sample(i):
        if i[0]%2==0:
            return True
        else:
            return False  
r=list(filter(sample,d.items()))
print(r)
print(type(r))

# By using lambda function we can write in single line:
d={1:"ram",2:"krishna",3:"ruchi",4:"ramya"}
print(list(filter(lambda i:i[0]%2==0 ,d.items())))