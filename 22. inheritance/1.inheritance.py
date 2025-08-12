'''
Inheritance:
When a class derives from another class. the child will inherit all the public
and protected properties and methods from the parents class.
In addition, if can have its own properties and methods.this is called inheritance. 
'''

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
class programmer(Employee):
    def showLanguage(self):
        print("The default langauge is python")




e1  = programmer("John", 101)
e1.showDetails()
e1.showLanguage()
