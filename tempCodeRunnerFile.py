class student:
    class_var = "I am a class variable"
    
    def method(self):
        print("This is a method.")

# Accessing the __dict__ attribute of the class
print(student.__dict__)