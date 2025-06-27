class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        if self.age<18:
            self.status="Minor"
        else:
            self.status="Adult"

        
p1=Person("Ram",30)
print(p1.__dict__)
   


   
  
    
  