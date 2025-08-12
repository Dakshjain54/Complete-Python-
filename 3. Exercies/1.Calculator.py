# a = 5
# b = 6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation: ")

if c == "+":
    print( a, "+", b, "=" , a+b)
elif c == "-":
    print( a, "-", b, "=" , a-b)
elif c == "*":    
    print( a, "*", b, "=" , a*b)
elif c == "/":
    print( a, "/", b, "=" , a/b)
elif c == "%":
    print( a, "%", b, "=" , a%b)
elif c == "**":
    print( a, "**", b, "=" , a**b)

    

