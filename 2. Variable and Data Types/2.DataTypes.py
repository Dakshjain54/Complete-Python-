# Data type specifies the type of value a variable holder. This is required in programming to do various operations without causing an error.
a = complex(8, 2)
a1 = 9
b = "Daksh"
c = True
d = None
print(a+a1)
print("The type of a is ", type(a))
print("The type of a1 is ", type(a1))
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of d is ", type(d))

# List is an ordered collection of data with elements separated by a comma and ebclose within square breackets
#List is a mutable
list = [8, 2.3, [-4, 5], ["Apple, Banana"]]
print(list)

#Truple is an ordered collection of data with elements seprated by a comma and ebclose within parentheses
#Truple is a immutable
#mutable = chnage
#immutable = no chnage
tuple = (("parrot", "sparrow"), ("Lion", "Tiger") )
print(tuple)

#Dict: A dictionary is an unordered collection of data containing a Key:value pair are enclosed within curly brakets
dict = {"name":"Daksh", "age":20, "canVote":True}
print(dict)