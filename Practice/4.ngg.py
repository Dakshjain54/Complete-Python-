import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    

    secret_number = random.randint(1, 100)
    attempts = 0

    
    while secret_number:
        try:

            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

           
            
        except ValueError:
            print("Please enter a valid number!")

number_guessing_game()