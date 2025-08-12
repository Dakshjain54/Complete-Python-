'''
Set:
Set are unordered collection of data items. they store multiple items in a single variable.
Set are unchangeable.
Set occur in random order.
You cannot change the values inside a list in a set 
'''

s = {2, 3, 2, 5, 3}
print(s)

info = {"car", 18, False, 6.5, 18}
print(info)

empty = set()
print(type(empty))

for value in info:
    print(value)