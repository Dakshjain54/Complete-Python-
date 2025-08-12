'''
OS Module in python:
is a built-in library that provide functions fir interactiog with the operating system.
it allows you to perform a wide variety of tasks, such as reading and writing files.
interacting with the file system, and running system commands.
'''

import os

if(not os.path.exists("data")):
    os.mkdir("data")
for i in range(0,10):
    os.mkdir(f"data/day {i+1}")
    os.rename(f"data/day {i+1}", f"data/class {i+1}")
