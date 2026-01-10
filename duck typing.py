'''
Duck typing is to determine if an object is suitable for a purpose by checking for the presence of certain methods and properties rather than objects actual type.
'''
#  If it looks like a duck, swims like a duck,and quacks like a duck,then it probably is a duck...
#  which simply means it doesnt matter it is duck or not if the behaviour of the bird match with the duck then it is a duck....

# Another example:
# A teacher says:
# “Anyone who can write may answer the question.”
# Students may have:
# Pen
# Pencil
# Marker

# The teacher does not care what you are holding.
# The teacher only cares:
# Can you write?


#Example
class A:
    def m1(self):
        print('A-m1')
class B:
    def m1(self):
        print('B-m1')
class C:
    def m1(self):
        print('C-m1')
        
def search(x):
    x.m1()

a=A()
search(a)

b=B()
search(b)

c=C()
search(c)


#Example
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

'''   
Duck is swimming
Duck is Flying
Whale is Swimming
AttributeError: 'Whale' object has no attribute 'fly' 
'''

# 💡 **Explanation:**
# - Python doesn’t check if `i` is of type `Duck`.
# - It just assumes `i` can `swim()` and `fly()`.
# - When it finds `Whale` missing `fly()`, it throws an error.

# This is **duck typing failure** due to missing expected behavior.



## ✅ Example 3 — Real-Time Example: Payment Systems


class CreditCard:
    def pay(self, amount, tax):
        print(f"Paid ₹{amount + tax} using Credit Card")

class UPI:
    def pay(self, amount, tax):
        print(f"Paid ₹{amount - tax} using UPI (discount applied)")

class Wallet:
    def pay(self, amount, tax):
        print(f"Paid ₹{amount * tax} using Wallet (reward points applied)")

def checkout(payment_method):
    payment_method.pay(1000, 100)

# Creating objects
credit = CreditCard()
upi = UPI()
wallet = Wallet()

# Duck typing in action
checkout(upi)       # Paid ₹900 using UPI (discount applied)
checkout(wallet)    # Paid ₹100000 using Wallet (reward points applied)
checkout(credit)    # Paid ₹1100 using Credit Card


# 🧾 **Output:**
# ```
# Paid ₹900 using UPI (discount applied)
# Paid ₹100000 using Wallet (reward points applied)
# Paid ₹1100 using Credit Card


### 🧠 Explanation:
# - `checkout()` accepts **any object** that defines a `pay()` method.
# - It doesn’t matter whether it’s a `CreditCard`, `UPI`, or `Wallet`.
# - As long as the object supports the required behavior (`pay()` method),  
#   the code works — that’s **Duck Typing**.


## 🧩 When to Use Duck Typing

# ✅ Use Duck Typing when:
# - You want **flexible and reusable** functions.
# - You don’t care about class inheritance — only **method presence**.
# - You’re implementing **loose coupling** between modules.

# ❌ Avoid Duck Typing when:
# - You require **strict type safety**.
# - You’re working on **large-scale, type-sensitive projects** (use type hints or ABCs instead).



## 🧩 Duck Typing vs Traditional Typing

# | Feature | Traditional Typing | Duck Typing |
# |----------|--------------------|--------------|
# | Type Checking | At compile-time | At runtime |
# | Flexibility | Low | High |
# | Example Languages | Java, C++, C# | Python, JavaScript |
# | Based On | Class hierarchy | Method behavior |
# | Polymorphism | Requires inheritance | Requires same methods |


## 🧩 Practical Real-World Example


class File:
    def read(self):
        print("Reading data from file...")

class NetworkStream:
    def read(self):
        print("Reading data from network...")

class Keyboard:
    def read(self):
        print("Reading input from keyboard...")

def read_data(source):
    source.read()

read_data(File())
read_data(NetworkStream())
read_data(Keyboard())


# 🧾 **Output:**

# Reading data from file...
# Reading data from network...
# Reading input from keyboard...
# ```

# ✅ Here, all three classes are **unrelated** — yet they can be passed to `read_data()`  
# because they all define a `read()` method.



## 🧩 Benefits of Duck Typing

# | Benefit | Description |
# |----------|--------------|
# | ✅ Flexibility | Works with any object having required methods |
# | 🧠 Simplicity | No need for complex inheritance hierarchies |
# | ♻️ Reusability | Functions can handle multiple unrelated objects |
# | 🔄 Extensibility | Add new classes easily without changing existing code |



## ⚠️ Drawbacks of Duck Typing

# | Limitation | Description |
# |-------------|--------------|
# | ❌ Runtime Errors | Errors occur only when a method is missing |
# | 🧩 Harder Debugging | No static type checking |
# | 🚫 Readability | May confuse beginners when unrelated classes interact |


# ✨ *“Duck Typing makes Python flexible — it’s not about who you are, but what you can do.”* 🦆🐍
