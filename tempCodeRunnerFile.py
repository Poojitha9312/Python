class College:
    def __init__(self):
        self.__balance=50000
    def getbalance(self,password):
        if password==2025:
            return self.__balance
        else:
            return "You are not authorised user"
c=College()
print(c.getbalance(2025))