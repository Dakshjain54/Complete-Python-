'''
Map, Filter and Reduce:
This are built-in function that allow you to apply a function to a sequence of element
and return a new sequence. it is also known as higher-order function

MAP:
The map function appliedd a function to each element in a sequence and return 
a new sequence containing the transform element.
'''

# def cube(x):
#     return x*x*x

# cube = lambda x: x*x*x
# # print(cube(2))

# l = [1, 2, 3, 4, 5, 6, 7]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# print(l)
# newl = list(map(cube, l))
# print(newl)  

'''
Filter:
The filter function filters a squence of elements based on a given predicate
and return a new sequence containing only the element that meet the predicate.
'''
# def filter_function(a):
#     return a>4

# newnewl = list(filter(filter_function, l))
# print(newnewl)

'''
Reduce:
The reduce function is a higher-order function that applied a function to a 
sequence and return a single value. 
it is a part of the function module in python  
'''

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)

print(sum)

 