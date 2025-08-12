'''
Class:
A class is a blueprint or a template for creating objects, providing initial values 
for state (member variables or attributes), and implementations of behavior (member functions or methods). 
The user-defined objects are created using the class keyword.

self parameter:
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition.
'''
# class
class person:
    name = "daksh"
    age = 18

    def info(self):
        print(f"{self.name} is a {self.age} years old. ")

# object
a = person()
b = person()
# print(a.name)
b.name = "Alokk"
b.age = 17
a.info()
b.info()

'''
OBJECT:
An object is an instance of a class, and it contains its own data and methods.
For example, you could create a class called "Person" that has properties such as name and age, 
and methods such as speak() and walk(). Each instance of the Person class would be a unique 
object with its own name and age, but they would all have the same methods to speak and walk.
'''