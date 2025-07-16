d={1:"ram",2:"krishna",3:"ruchi",4:"ramya"}
def sample(i):
        if i[0]%2==0:
            return True
        else:
            return False  
r=list(filter(sample,d.items()))
print(r)
print(type(r))