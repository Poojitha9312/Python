class College:
    def __init__(self):
        self.__balance=50000
    def getbalance(self):
        return self.__balance
c=College()
print(c.getbalance())