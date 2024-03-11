

# Create a number guessing game. Where you have to generate a random number in between 1 to 100 and user have to prompt a number for guess.
# if its high or low number let the user know and guide them through the process to guess correct number.

import random

target_number = random.randint(1, 100)
guess_count = 0

while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    guess_count += 1

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {target_number} correctly in {guess_count} guesses!")
        break


# Output:
# Guess the number (between 1 and 100): 50
# Too high! Try again.
# Guess the number (between 1 and 100): 25
# Too high! Try again.
# Guess the number (between 1 and 100): 12
# Too low! Try again.
# Guess the number (between 1 and 100): 18
# Too low! Try again.
# Guess the number (between 1 and 100): 21
# Too low! Try again.
# Guess the number (between 1 and 100): 23
# Too low! Try again.
# Guess the number (between 1 and 100): 24
# Congratulations! You guessed the number 24 correctly in 7 guesses!
# Note: The number of guesses may vary as it is a random number guessing game.