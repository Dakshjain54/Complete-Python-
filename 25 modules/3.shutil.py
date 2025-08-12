import shutil
import os

shutil.copy("25 modules/3.shutil.py", "copy.py")        #for files ko copy kerta h 
shutil.copytree("25 modules", "25 copy")                #for folders ko copy kerta h 
shutil.move("25 modules/3.shutil.py", "3.shutil.py")    #for folder me se bhar kerne ke liye
shutil.rmtree("25 copy")                                # ye folder ko remove kerta h file ko nhi 
os.remove("copy.py")                                    # ye file ko kerta h 