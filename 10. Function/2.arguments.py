# DEFAULT ARGUMENT
def average(a=9, b=1):
    print("The average is ", (a+b)/2)

average(1,5)
average(6)
average(b=8)

# KEYWORD ARGUMENT
average(b=52, a=56)

# REQUIRED ARGUMENT
def sum(a, b=9):
    print("The sum is ", a+b)

sum(52)
sum(21, 52)

# VARIABLE-LENGTH ARGUMENT

def calaverage(*numbers):
    sum1 = 0
    for i in numbers:
        sum1 = sum1 + i
    print("The average is ", sum1 /len(numbers))

calaverage(1,2,3,4,5,6,7,8,9)

# RETURN ARGUMENT
def calaverage(*numbers):
    sum1 = 0
    for i in numbers:
        sum1 = sum1 + i
    return sum1 /len(numbers)

c = calaverage(1,2,3,4,5,6,7,8,9)
print(c)