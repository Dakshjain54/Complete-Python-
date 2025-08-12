ep1 = {122: 45, 123: 89, 567: 69, 526: 99}
ep2 = {222: 65, 566: 97}
print(ep1)
print(ep2)

ep1.update(ep2)
print(ep1)

ep1.pop(122)
print(ep1)

ep1.popitem()
print(ep1)

ep1.clear()
print(ep1)