'''
Enumerate function:
The enumerate function is a built-in function in python that allows 
you to loop over a sequence and get the index and value of each element
in the sequence at the same time. 
'''

marks = [12, 35, 65, 95, 55, 12, 1 , 4, 5]

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Daksh, awesome")

