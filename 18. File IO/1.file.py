'''
File IO:
Before we can perform any operations on a file, we must first open it. python provides the open()
function to open a file. it takes tow arguments: the name of the file and the mode in which the file should be opened. 
The mode can be 'r' for reading, 'w'for writing, or 'a' for appending
'''
# Reading a file
# f = open('myfile2.txt', 'r')

# text = f.read()
# print(text)
# f.close()

# writing a file
# f = open('myfile2.txt', 'a')

# f.write("HEllo daksh")
# f.close()

with open('myfile2.txt', 'r') as f:
    taxt = f.read()
    print(taxt)
     
