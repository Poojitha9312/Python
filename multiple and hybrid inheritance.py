# 🧩 Multiple and Hybrid Inheritance in Python

## 🔹 What is Inheritance Recap?
# > **Inheritance** allows a new class to reuse and extend the functionality of another class.  
# > The new class (Child / Derived class) inherits attributes and behaviors (methods) from the existing class (Parent / Base class).

# Python supports various types of inheritance:  
# ✅ Single  
# ✅ Multilevel  
# ✅ Multiple  
# ✅ Hierarchical  
# ✅ Hybrid

## 🧩 1️⃣ Multiple Inheritance

### 📘 Definition:
# > In **Multiple Inheritance**, a single child class inherits from **multiple parent classes**.

# 🧠 **Syntax:**

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

# 🧩 Diagram:

#        class A         class B
#              \         /
#               \       /
#                \     /
#                 class C(A, B)


### ✅ Example 1 — Multiple Parents, One Child

class A:
    def method1(self):
        print('A class method1')

class B:
    def method2(self):
        print('B class Method2')

class C(A, B):
    def method3(self):
        print('C class Method3')

c = C()
c.method1()
c.method2()
c.method3()


# 🧾 **Output:**
# A class method1
# B class Method2
# C class Method3

# ✅ **Explanation:**
# - Class `C` inherits from **A** and **B**.
# - So `C` can access both parent class methods.


### ✅ Example 2 — Method Resolution Order (MRO)

# If both parent classes have **the same method name**, Python resolves which one to call based on the **Method Resolution Order (MRO)** — **left-to-right** order in inheritance.

class A:
    def method1(self):
        print('A class method')

class B:
    def method1(self):
        print('B class Method')

class C(A, B):  # A has higher priority (leftmost parent)
    pass

c = C()
c.method1()

# 🧾 **Output:**
# A class method


# ✅ **Explanation:**
# - Python follows **MRO (Method Resolution Order)**.
# - It looks for `method1` in:
#   - Class `C` → then in Class `A` → then in Class `B` → finally in `object`.

# 🧠 You can check the MRO using:
# print(C.mro())

# 🧾 Output:
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]



### 🧠 Real-World Example: Multiple Inheritance
class Father:
    def skills(self):
        print("Father: Driving, Cooking")

class Mother:
    def skills(self):
        print("Mother: Dancing, Singing")

class Child(Father, Mother):
    def skills(self):
        print("Child: Playing")
        super().skills()  # Calls Father (first in MRO)

c = Child()
c.skills()


# 🧾 **Output:**
# Child: Playing
# Father: Driving, Cooking


# ✅ **Explanation:**
# - The `super()` call in `Child` goes to the **first parent** in the MRO (Father).
# - MRO ensures consistent and predictable order.



## 🧩 2️⃣ Hybrid Inheritance

### 📘 Definition:
# > **Hybrid Inheritance** is a combination of **two or more types** of inheritance (e.g., Single + Multilevel, Multiple + Hierarchical, etc.).

# 🧩 It represents **complex relationships** between multiple classes.


### 🧩 Diagram:

    #        class A
    #       /       \
    #  class B        class C
    #       \         /
    #        \       /


# Here:
# - A → B and C represent **Hierarchical Inheritance**
# - B and C → D represent **Multiple Inheritance**

# So the total pattern forms a **Hybrid Inheritance**.


### ✅ Example — Hybrid Inheritance (Hierarchical + Multiple)

`
class A:
    def method1(self):
        print("A class method1")

class B(A):
    def method2(self):
        print("B class method2")

class C(A):
    def method3(self):
        print("C class method3")  # Hierarchical Inheritance

class D(B, C):
    def method4(self):
        print("D class method4")  # Multiple Inheritance

d = D()
d.method1()
d.method2()
d.method3()
d.method4()


# 🧾 **Output:**
# ```
# A class method1
# B class method2
# C class method3
# D class method4


# ✅ **Explanation:**
# - `B` and `C` are derived from `A` (Hierarchical Inheritance).  
# - `D` is derived from both `B` and `C` (Multiple Inheritance).  
# - Together, this structure forms **Hybrid Inheritance**.

### 🧠 MRO in Hybrid Inheritance


print(D.mro())

# 🧾 **Output:**
# ```
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# ✅ **MRO ensures that Python knows which class method to execute first**, preventing ambiguity.


## ⚙️ `super()` Function and Constructor Chaining
# > The `super()` function in Python is used to **call the parent class’s method or constructor**.


### ✅ Example — Using `super()` in Multiple Inheritance

class A:
    def __init__(self):
        print("A Constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B Constructor")

class C(B):
    def __init__(self):
        super().__init__()
        print("C Constructor")

c = C()

# 🧾 **Output:**
# A Constructor
# B Constructor
# C Constructor


# ✅ **Explanation:**
# - Each `super()` call triggers the parent constructor.
# - This ensures **constructor chaining** through the inheritance hierarchy.



## 🧩 Hybrid Real-World Example: Educational Hierarchy
class Person:
    def details(self):
        print("I am a Person")

class Teacher(Person):
    def teach(self):
        print("I teach Students")

class Student(Person):
    def study(self):
        print("I am learning")

class TeachingAssistant(Teacher, Student):
    def assist(self):
        print("I help the teacher and students")

ta = TeachingAssistant()
ta.details()
ta.teach()
ta.study()
ta.assist()

# 🧾 **Output:**
# I am a Person
# I teach Students
# I am learning
# I help the teacher and students

# ✅ **Explanation:**
# - `Teacher` and `Student` both inherit from `Person` → Hierarchical Inheritance.  
# - `TeachingAssistant` inherits from both `Teacher` and `Student` → Multiple Inheritance.  
# - Together they form **Hybrid Inheritance**.


# ✨ *“Inheritance isn’t just about reusing code — it’s about building logical relationships between real-world entities.”* 🧬🐍