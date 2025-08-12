class employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"the name is {self.name}")  

class dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"the dance is {self.dance}") 

class dancerEmployee(employee, dancer):
    def __init__(self, dance ,name ):
        self.dance = dance
        self.name = name

    def __str__(self):
        return f"{self.dance} and {self.name}"    

o = dancerEmployee("DJ", "Daksh")
print(o)
o.show()
print(dancerEmployee.mro())