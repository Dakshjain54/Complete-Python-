'''
Recursion:
IS the process of defining something in terms of itself.
'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(2))    
print(factorial(3))    
print(factorial(4))    
print(factorial(5))    
print(factorial(6))    

# Fibonacci sequence
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
     

print(fibonacci(3))    