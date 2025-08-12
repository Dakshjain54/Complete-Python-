class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show(self):
        print(f"Name: {self.name}")    
        print(f"Species: {self.species}")  

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="dog") 
        self.breed = breed
    def show(self):
        animal.show(self) 
        print(f"Breed: {self.breed}")   
        
class gold(dog):
    def __init__(self, name, color):
        dog.__init__(self, name, breed="kanaksh")
        self.color = color
    def show(self):
        dog.show(self)
        print(f"Color: {self.color}")    


o = gold("Tommy", "Red")
o.show()
print(gold.mro())