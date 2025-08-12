class maths:
    def __init__(self, num):
        self.num = num

    def addcount(self, n):
        self.num = self.num + n    

    @staticmethod
    def add(a,b):
        return a+b     

a = maths(5)
print(a.num)
a.addcount(6)
print(a.num)  


print(maths.add(5,6))