class Duck:
    def swim(self):
        print("Duck is swimming")
    
    def fly(self):
        print("Duck is Flying")
class Whale:
    def swim(self):
        print("Whale is Swimming")

def search(x):
    x.swim()
    x.fly()
    
d=Duck()
w=Whale()
search(d)
search(w)
        
for i in [Duck(),Whale()]:
    i.swim()
    i.fly()