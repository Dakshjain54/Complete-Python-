import random

def RPS():
  print("welcome to rock paper scissor game")
  
  player_input = input("Enter your choice (rock, paper, scissor): ")
  comuter_choice = random.choice(["rock", "paper", "sissor"])
  
  print(f"you choose {player_input} and computer choose {comuter_choice}")
  
  if player_input == comuter_choice:
    print("the game is draw")
  elif player_input == "rock" and comuter_choice == "scissor":
    print("you won the game")
  elif player_input == "paper" and comuter_choice == "rock":
    print("you won the game")
  elif player_input == "scissor" and comuter_choice == "paper":
    print("you won the game")
  else:
    print("you lost the game")          

RPS()
