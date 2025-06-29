class person:
    school_name="Sri Chaitanya"
    
    @classmethod
    def cls_method(cls):
        print(f"My school name is {cls.school_name}")
        person.another_cls_method()
        cls.another_cls_method()
        
    @classmethod
    def another_cls_method(cls):
        print(f"My school name is {cls.school_name}")
        
person.cls_method()

s1=person()
s1.cls_method()
s1.another_cls_method()
   
        
  
   


   
  
    
  