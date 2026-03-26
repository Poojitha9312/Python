class parent:
    def sample(self):
        print("I like fruits")
    
class child(parent):
    def sample(self):
        print("I like Ice cream and pizza")# Method overriding
c1=child()
c1.sample()