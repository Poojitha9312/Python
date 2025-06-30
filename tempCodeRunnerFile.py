class employee:
    def __init__(self,ename,eage,eid):
        self.ename=ename
        self.eage=eage
        self.eid=eid
    def employee_details(self):
        print(f"my name is {self.ename}")
        print(f"my age is {self.eage}")
        print(f"my id is {self.eid}")
s1=employee("ram",30,1026)
s1.employee_details()