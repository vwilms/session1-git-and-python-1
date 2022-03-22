from random import randint  # Import the randint function from the random package
# import random

number = randint(1, 100)  # Generate a random number between 1 and 100
print(number)  # Print the number (to make testing easier)

# Ask the user for a guess, and convert the result to an integer
guess = int(input('Guess the number (between 1 and 100): '))

while number != guess:
    if guess < number:
        print("Guess is too low!")
        guess = int(input('Try again: '))
    elif guess > number:
        print("Guess is too high!")  
        guess = int(input('Try again: '))
print("Correct!")

# Homework: extend the above program so that:
#   1) it generates a number between 1 and 100,
#   2) it gives higher/lower feedback on an incorrect guess.
