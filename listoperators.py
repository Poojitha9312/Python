#list operators:
#concatenation
# Repetition
# Membership
# Iteration
# length
# 1. Concatenation:
# concatenation operator means it joins the two lists
# program of concatenation: "+" is the concatenation operator
p1=[1,2,3,4,5]
p2=[6,7,8,9,10]
print(p1+p2)

# 2.Repetition :
# Repetition operator enables the list to be repeated in multiple times
# program of Repetition:"*" is the repetition operator
p1=["red","blue","pink"]
print(p1*2)

# Membership :
# Membership operator means it returns true if the particular item is there in list
# otherwise it returns false:"in,not in" is the membership operator
#program of Menbership:
p1=[1,2,3,4,5]
print(2 in p1)
print(4 not in p1)
print(6 not in p1 )
#Iteration:
# for loop is used to iterate all the list elements:
#program of Iteration:
p1=[1,2,3,4,5]
for i in p1:
    print(i,end=" ")
# Length:
# It is used to get the length of the list:
p1=[1,2,3,4,5]
print(len(p1))






