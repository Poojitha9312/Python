# 🧩 Inheritance (IS-A Relationship) in Python


## 🔹 What is Inheritance?

# > **Inheritance** is a mechanism in Object-Oriented Programming that allows a new class (child) to acquire the properties and behavior of an existing class (parent).

# - The **existing class** is called the **Base / Parent / Super class**.
# - The **new class** is called the **Derived / Child / Subclass**.



### 🧠 Syntax:


# class Parent:
#     # base class properties and methods

# class Child(Parent):
#     # derived class properties and methods




### ✅ Example:


class A:  # Base / Parent class
    def method1(self):
        print("A class Method1")

    def method2(self):
        print("A class Method2")

class B(A):  # Derived / Child class
    def method3(self):
        print("B class Method3")

b = B()
b.method3()
b.method1()


# 🧾 **Output:**
# ```
# B class Method3
# A class Method1


# ✅ Here,  
# - Class `B` inherits from class `A`.  
# - So `B` can access both **its own methods** and **parent methods**.



### 🧩 Real-World Example: IS-A Relationship


#             Person
#             *    *
#      IS-A  *      * IS-A
#           *        *
#          *          *
#     Employee        Student
# ```

# 🧠 Interpretation:
# - `Employee IS-A Person`
# - `Student IS-A Person`

# This type of relationship represents **inheritance**.



## 🧠 Example: Inheriting Instance Variables

class A:
    def __init__(self):
        self.x = 10
        self.y = 20
        
class B(A):
    def Details(self):
        print(f'x is {self.x}')
        print(f'y is {self.y}')

b = B()
b.Details()

# 🧾 **Output:**

# x is 10
# y is 20


# ✅ The `B` class inherits both instance variables `x` and `y` from class `A`.



### ❌ Without Inheritance (Code Duplication)


class A:
    def __init__(self):
        self.x = 10
        self.y = 20

class B:
    def __init__(self):  # Repeated code
        self.x = 10
        self.y = 20
    def Details(self):
        print(f'x is {self.x}')
        print(f'y is {self.y}')

b = B()
b.Details()


# 🧾 **Output:**
# ```
# x is 10
# y is 20


# 🚫 **Problem:** Code duplication — If you modify logic in one class, you need to repeat changes elsewhere.  
# ✅ **Solution:** Use **Inheritance** for **code reusability**.



## ✅ Advantages and Disadvantages of Inheritance

### 🟢 Advantages:
# 1. **Code reusability** — eliminates redundant code.  
# 2. **Reduces code size** — simplifies maintenance.  
# 3. **Extensibility** — easily add new functionality (override methods).

### 🔴 Disadvantages:
# 1. **Tight coupling** — if the parent class changes, it directly affects all child classes.  
# 2. **Increased complexity** in deep inheritance hierarchies.



### ⚠️ Example: Tight Coupling in Inheritance


class A:
    def m1(self):
        self.x = 10  # if changed, affects all child classes
        print(f"Value of x is {self.x}")

class B(A):
    pass

b = B()
b.m1()


# 🧾 **Output:**
# ```
# Value of x is 10


# If you modify `x` in parent class `A`, it automatically reflects in `B` —  
# proving inheritance creates **tight coupling**.



### ⚙️ Example: Changes in Child Do Not Affect Parent
class A:
    def m1(self):
        self.x = 10
        print(f"Value of x is {self.x}")

class B(A):
    def m2(self):
        self.x = 20  # local to B

b = B()
b.m1()


# 🧾 **Output:**
# Value of x is 10

# ✅ Child modifications don’t affect parent — the inheritance direction is **one-way**.



## 🧩 1️⃣ Single Inheritance

### 📘 Definition:
# In **Single Inheritance**, one **child class** inherits from one **parent class**.


# Parent → Child


# 🧠 **Syntax:**

class Parent:
    pass

class Child(Parent):
    pass


### ✅ Example 1 — Simple Single Inheritance
class A:
    def method1(self):
        self.x = 10
        self.y = 20
        print(f"value of x is {self.x}")
    def method2(self):
        self.z = 30
        print(f"value of z is {self.z}")

class B(A):
    pass        

b = B()
b.method1()
b.method2()


# 🧾 **Output:**
# ```
# value of x is 10
# value of z is 30



### ✅ Example 2 — Parent vs Child Access
class A:
    def method1(self):
        print("A class Method1")
    def method2(self):
        print("A class Method2")

class B(A):
    def method3(self):
        print("B class Method3")

a = A()
a.method1()
a.method2()

b = B()
b.method3()
b.method1()
b.method2()

# 🧾 **Output:**
# A class Method1
# A class Method2
# B class Method3
# A class Method1
# A class Method2


# ✅ The **child class** can access both parent and its own methods.  
# ❌ The **parent class** can access only its own methods.



### ✅ Example 3 — Inheriting All Types of Members
class A:
    a = 10
    print(f"value of a is {a}")
    
    def __init__(self):
        self.b = 15
        print(f"value of b is {self.b}")
    
    def method1(self):
        y = 20
        self.x = 30
        print(f"value of x is {self.x}")
        print(f"value of y is {y}")
        
    @classmethod
    def cm(cls):
        cls.cmv = 40
        print(f"value of cmv is {cls.cmv}")
        
    @staticmethod
    def sm():
        smv = 50
        print(f"value of smv is {smv}")

class B(A):
    pass        

b = B()
b.method1()
b.cm()


# 🧾 **Output:**
# value of a is 10
# value of b is 15
# value of x is 30
# value of y is 20
# value of cmv is 40
# value of smv is 50


# ✅ The **child class (`B`)** can access:
# - Instance variables  
# - Class variables  
# - Static methods  
# - Class methods  
# - Instance methods  
# - Constructors of the **parent class (`A`)**


# ✨ *“Inheritance promotes reusability — you write once, and use everywhere.”* 🧬🐍