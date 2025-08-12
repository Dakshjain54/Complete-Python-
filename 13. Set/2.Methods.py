s1 = {1, 2, 5, 6}
s2 = {6}
# print(s1.union(s2))

# s1.update(s2)
print(s1,s2)

# comman number
print(s1.intersection(s2))

# comman ke alava
print(s1.symmetric_difference(s2))

# Difference
print(s1.difference(s2))

# isdisjoint() both are diffrent
print(s1.isdisjoint(s2))

# issuperset()
print(s1.issuperset(s2))

# issubset()
print(s2.issubset(s1))

# add()
s1.add(9)
print(s1)

# remove()  it raise any error
s1.remove(9)
print(s1)

# discard()  it does not raise any arror
s1.discard(9)
print(s1)

# pop()
item = s1.pop()
print(s1)
print(item)

# clear()  clears all items in the set and prints an empty set

