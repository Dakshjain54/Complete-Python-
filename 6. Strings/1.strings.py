'''
String?
In python, anything that you enclose betwwen single and double 
quotation marks is considered a sting. A string is essentially 
a sequence or array of textual data. Str are used when working 
with unicode characters 

'''

name = "Daksh"
friend = "ROhan"
anotherFriend = 'Ram'
apple = '''He said,
hi daksh
hey I an good
I want to eat an apple'''
print("hello," + name)
# print(apple)
print(name[0])
print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# Looping through the string
print("Lest use a for loop\n")
for character in apple:
    print(character)