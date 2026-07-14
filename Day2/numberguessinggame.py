import random
secret_number=random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a Integer number between 1 and 100.")
while True:
    guess=int(input("Guess the number: "))
    if guess>100 or guess<1:
        print("Please guess a number between 1 and 100.")
    elif guess<secret_number:
        print("Wrong guess! The number is higher than your guess.")
    elif guess>secret_number:
        print("Wrong guess! The number is lower than your guess.")
    elif guess==secret_number:
        print("Congratulations! You guessed the correct number:", secret_number)
        break
    else:
        pass


