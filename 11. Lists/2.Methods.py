l = [11,1,2,4,3,5,1,6]
print(l)
# Methods:
l.append(7)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(11))

print(l.count(1))

l.insert(2, 524)
print(l)

m =[100,200,300]
k = l+m
print(k)

l.extend(m)
print(l)