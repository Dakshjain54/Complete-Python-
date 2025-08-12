'''
Dictionaries:
are the ordered collection of data items.
They store multiple items in a single variable.
Dictionary items are Key-value pairs. 
'''

dic = {
    344: "Daksh",
    524: "hritik",
    548: "alok",
    582: "aditya"
}

print(dic[548])

info = {'name': 'Daksh', 'age': 19, 'eligible': True}
print(info)
# print(info['name'])  # it Rise any error
# print(info.get('name'))  #it does not raise any arror

print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())    