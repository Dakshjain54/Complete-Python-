# a = True
# print(a)
# print(a:=False)

# number = [1, 2, 3, 4, 5]
# while (n:= len(number))>0:
#     print(number.pop())

# foods = list()
# while True:
#     food = input("What food you like?:")
#     if food == "quit":
#         break
#     foods.append(food)

# bye using walrus operator
foods = list()
while(food := input("What food is you like?: "))!= "quit":
    foods.append(food)
    
