'''
Local and global variables:
A local variable is a variable that is defined within a function and is only 
accessible within that function. is distroyed when the function returns 

A globle variable is a variable that is defined outside of a function and is 
accessible from within any function in your code
'''

x= 4
print(x)

def hello():
    global x
    x = 10
    y = 5
    print(f"The local x is {y}")
    print("hello daksh")
    

hello()
print(f"The global x is {x}")

