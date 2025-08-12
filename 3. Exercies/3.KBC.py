# KBC

questions = [
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", "none", 2],
    ["What is the national animal of India?", "Peacock", "Elephant", "Tiger ", "Lion", "none", 3],
    ["Which is the largest planet in our solar system?", "Earth", "Jupiter ", "Mars", "Saturn", "none", 2],
    ["Who is known as the Father of the Nation in India?", "Sardar Patel", " Jawaharlal Nehru ", "Bhagat Singh ", "Mahatma Gandhi", "none", 4],
    ["Which is the smallest state in India by area?", "Goa ", "Sikkim  ", "Tripura", "Nagaland", "none", 1],
    ["Who was the first woman Prime Minister of India?", " Sarojini Naidu ", "Pratibha Patil  ", "Sushma Swaraj", "Indira Gandhi ", "none", 4],
    ["Who discovered gravity?", "Albert Einstein ", "Isaac Newton   ", "Galileo Galilei", "Nikola Tesla", "none", 2],
    ["Which Mughal emperor built the Taj Mahal?", "Akbar ", "Babur  ", "Jahangir", " Shah Jahan", "none", 4],
    ["In which year was the e-commerce company Amazon founded?", "1992 ", "1994   ", "1998", "2000", "none", 2],
    ["Which business magnate wrote the book “The Road Ahead”?", "Bill Gates ", "Jeff Bezos   ", "Warren Buffett", "Elon Musk", "none", 1]
    ]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 50000, 160000, 320000]

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"Ques: {question[0]}")
    print(f"1. {question[1]}          2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")
    reply = int(input("Enter your answer (1-4):  "))
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 7):
            money = 50000
        else:
            money = 320000
    
          
    else:
        print("Wrong answer!")        
        break
print(f"Your take home money is {money}")