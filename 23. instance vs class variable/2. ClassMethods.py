class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} adn company is {self.company}")

    @classmethod
    def changeCompany(cls, newcompany):
        cls.company = newcompany    


e1 = Employee()
e1.name = "daksh"
e1.show()
e1.changeCompany("tesla")
e1.show()
print(Employee.company)

