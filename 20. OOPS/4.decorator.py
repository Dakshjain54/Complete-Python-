'''
Python Decorators:
Python decorators are a powerful and versatile tool that allow you to modify the 
behavior of functions and methods. They are a way to extend the functionality of a 
function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a 
new function that modifies the behavior of the original function. The new function 
is often referred to as a "decorated" function. The basic syntax for using a 
decorator is the following:
'''

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello Daksh")

def add(a,b):
    print(a+b)
# greet(hello)()
hello()
greet(add)(1, 2)


 
