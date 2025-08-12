class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Sound made by a animal")

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="dog") 
        self.breed = breed

    def make_sound(self):
        print("Bark!")    

class cat(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="cat") 
        self.breed = breed

    def make_sound(self):
        print("miiaaauuuu!")  

d = dog("dog", "doger")
d.make_sound()

a = animal("dog", "dog")
a.make_sound()

c = cat("cat", "cater")
c.make_sound()