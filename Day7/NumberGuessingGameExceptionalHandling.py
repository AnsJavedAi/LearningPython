# Number Guessing Game with Exceptional Handling

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Type 'q' anytime to quit.\n")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            user_input = input("Enter your guess: ")
            
            if user_input.lower() == 'q':
                print(f"You quit the game. The number was {secret_number}.")
                break
            
            guess = int(user_input)
            attempts += 1
            
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100.")
            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError as e:
            print(f"Invalid input: {e}\n")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the game
number_guessing_game()