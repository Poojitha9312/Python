from abc import ABC, abstractmethod
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

class Child(Test):
    def m1(self):
        print("Hello")
c=Child()
c.m1()