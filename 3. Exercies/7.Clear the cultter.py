import os

files = os.listdir("exercies7")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"exercies7/{file}", f"exercies7/{i}.png")
        i = i+1