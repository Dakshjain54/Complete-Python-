
st = input("Enter mag ")

words = st.split(" ")
coding = input("1 of coding and 0 or dicoding: ")
coding = True if(coding == "1") else False
if(coding):
    newords = []
    for word in words:
        if(len(word)>=3):
            # r1 = ''.join(random.choices(string.ascii_lowercase,))
            # r2 = ''.join(random.choices(string.ascii_lowercase,))
            r1 = "asd"
            r2 = "bhg"
            newst = r1 + word[1: ] + word[0] + r2
            newords.append(newst)
        else:
            newords.append(word[:: -1])
    print(" ".join(newords))
else:
    newords = []
    for word in words:
        if(len(word)>=3):
            newst = word[3:-3]
            newst = newst[-1] + newst[:-1]
            newords.append(newst)
        else:
            newords.append(word[:: -1])
    print(" ".join(newords))