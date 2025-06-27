# nested loop:
# A nested loop means placement of loop inside another loop....
# nested loop concept applies for both for and while loop

# syntax for nested while:
# while condition: (outer loop)
#    code executes outer loop
#     while condition:  (inner loop)
#          code executes inner loop

# syntax for nested for loop:
# for outer variable in outer sequence:
#     code executes outer loop
#     for inner variable in inner sequence:
#            code executes inner loop



# while-while loop:
i=1
while i<=3:
    print(i)   
    j=1
    while j<=3:
        print(j)
        j=j+1
    i=i+1

i=1
while i<=3:
    print("ram")
    j=1
    while j<=3:
        print("seetha")
        j=j+1
    i=i+1
    

x=[1,2]
y=[4,5]
i=0
while i<len(x):    # len(x)=2- (0,1), len(y)=2(0,1)
    j=0
    while j<len(y): 
        print(x[i], y[j])  
        j=j+1
    i=i+1  

for i in range(1,11):
    for j in range(2,4) :
        print(i*j,end=" ")
    print()
  
   


adj=["red","big","tasty"]
fruits=["apple","goa","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
    print()

