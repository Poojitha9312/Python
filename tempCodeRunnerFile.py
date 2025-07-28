class Outer:
    def __init__(self):
        print("Outer class")
    class Inner:
        def __init__(self):
            print("Inner class")
# #outer class object creation
o=Outer()

# #inner class object creation in different ways
i=o.Inner()
i1=Outer.Inner()
i2=Outer().Inner()
