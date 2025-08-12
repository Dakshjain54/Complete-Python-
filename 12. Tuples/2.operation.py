# countries = ("Spain", "Italy", "India", "England","Germany")
# temp = list(countries)
# temp.append("Russia")  #add item
# temp.pop(1)              #remove item
# temp[2] = "Finland"     #change item
# countries = tuple(temp)
# print(countries)


# countries2 = ("China", "Dubhi", "Hong kong")
# add = countries + countries2
# print(add)

# METHODS

tuple1 = (0, 1, 2, 3, 4, 3, 5, 3, 6, 2, 1)
res = tuple1.count(2)
print("count = ", res)

res = tuple1.index(6)
res = tuple1.index(6,4,9)
print("index = " , res)

res = len(tuple1)
print("Length = " , res)