'''
Lists:
Lists sre ordered collection of data items.
They store multiple items in s single variable.
Lists items are sseparated by commas and enclosed within square brackets[]
You cannot change the values inside a list in a set 
'''
marks = [3,5,4,"daksh", 25, 2, 1, 5 , 3, 5,9]
print(marks)
print(len(marks))
print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3])

# if 5 in marks:
#     print("Yes")
# else:
#     print("no")

# same thing applies for srings as well!    
# if "ak" in "daksh":
#     print("yes")

# print(marks)
# print(marks[1:-1])
# print(marks[1::2])

lst = [i for i in range(10)]
print(lst)
lst = [i for i in range(20+1) if i%2==0]
print(lst)