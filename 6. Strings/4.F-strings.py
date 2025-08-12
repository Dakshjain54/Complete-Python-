letter = "Hey my name is {} and i am from {}"
name = input("Enter your name : ")
countrie = input("Enter your countrie name : ")
print(letter.format(name, countrie))

# 2nd mathod
print(f"Hey my name is {name} and i am from {countrie}")
print(f"Hey my name is {{name}} and i am from {{countrie}}")