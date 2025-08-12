# words = {
#     "madad" : "Help",
#     "kursi" : "chair",
#     "chutha" : "Dog",
#     "aaja" : "Come",
# }

# word = input("Enter word: ")
# print(words[word])




# numbers = [input("Enter 8 numbers")]

# unique_numbers = set(numbers)

# print("Unique numbers:", unique_numbers)

# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') 
# print(len(s))


# fav_lang = {}

# for i in range(4):
#     name = input(f"Enter the name of friend {i+1}: ")
#     language = input(f"Enter {name}'s favorite language: ")
#     fav_lang[name] = language

# print("\nFavorite Languages Dictionary:")
# print(fav_lang)

# You cannot change the values inside a list in a set 
# s = {8, 7, 12, "Harry", '[1,2]'} 
# print(s)
# s.remove(7)
# s.add(5)
# print(s)

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))

# greatest = max(num1, num2, num3, num4)
# print(f"\nThe greatest number is: {greatest}")


# d = 300
# a = float(input("Enter Maths marks: "))
# b = float(input("Enter Physics marks: "))
# c = float(input("Enter BEE marks: "))
# total = a+b+c
# total_per = (total/d)*100
# print(total)
# print(total_per,"%")

# if(a<33):
#     print("failed in Maths")
# elif(b<33):
#     print("failed in Physics")
# elif(c<33):
#     print("failed in BEE")

# if((total/d)*100<40):
#     print("Final result fail")    
# else:
#     print("Final result pass")    

# a = input("Enter anything: ")
# if(len(a)<10):
#     print("Yes it contains less than 10 characters")
# elif(len(a)==10):
#     print("contains 10 characters only")

# else:
#     print("No it does't contains less than 10 characters")


names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

search_name = input("Enter the name to search: ")

if search_name in names:
    print(f"{search_name} is present in the list.")
else:
    print(f"{search_name} is NOT present in the list.")




