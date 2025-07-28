class Outer:
    def __init__(self):
        print("Outer class")
    class Inner:
        def __init__(self):
            print("Inner Class") 
    i=Inner()   
    
o=Outer()