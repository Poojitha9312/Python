class parent:
    def sample(self):
        print(" I like fruits")
class child(parent):
    def sample1(self):
        print("I like pizza")
c1=child()
c1.sample1()
c1.sample()