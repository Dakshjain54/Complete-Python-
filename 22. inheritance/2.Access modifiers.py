'''
Access modifiers:
are used to limit the access of class variable and class methodes outside 
of class while implementing the concept of inherritance.

Thpes of access specifiers
1. Public Access modifiers
2. Private Access modifiers
3. Protected Access modifiers
'''

'''
Public Access modifiers:
All the variables and methods in python are by default public.
any instance variable in a class followed by self keyword  
'''
class Employee:
    def __init__(self):
        self.name = "Daksh"

a = Employee()
print(a.name)

'''
Private Access modifiers:
Private members of a class are those members which are only accessible inside the class.
we canot use private members outside the class.
'''
class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()
# print(a.__name) # Cannot be accessed directly
print(a._Employee__name) # Cannot be accessed indirectly
print(a.__dir__())

'''
Protected Access modifiers:
In object oriented programming (OOP), the term "protected" is use to 
describe a member of a class that is intended to be accessible only
by the class itself and its subclasses.
'''
class student:
    def __init__(self):
        self._name = "Daksh"
    def _funName(self): # protected method
        return "code with daksh"
class Subject(student):   # inherited class 
    pass

obj = Subject()
obj1 = student()
print(dir(obj))

# calling by object of student class
print(obj._name)
print(obj._funName())

# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
