# with open('myfile2.txt', 'r') as f:
#     print(f.read())
#     print(type(f))
#     f.seek(10)  # Move to the 10th byte in the file

#     print(f.tell())

#     data = f.read(10)  # Read the next 5 bytes
#     print(data)


# Truncate:
with open('myfile2.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(5)

with open('myfile2.txt', 'r') as f:
    print(f.read())
