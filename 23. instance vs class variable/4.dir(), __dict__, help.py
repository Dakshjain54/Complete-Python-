# 1. dir() method
# x = [1, 2, 3]
# print(dir(x))
# print(x.__add__)

# 2. __dict__ method
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = person("daksh", 18)        
print(p.__dict__)

# 3. help() method
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Daksh", 19)        
print(p1.__dict__)
print(help(person))