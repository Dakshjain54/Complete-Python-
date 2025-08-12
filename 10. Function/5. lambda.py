'''
Lambda function:
is a small anonymous function without a name.
It is define using the lambda keyword and has the following syntax:

'''

# def double(x):
#     return x*2

# both are same
def appl(fx, value):
    return 6 + fx(value)
 
double = lambda x: x*x
cube = lambda x: x*x*x

print(double(5))
print(cube(5))
print(appl(lambda x: x*x*x*x, 2))