"""
A Number Guessing Game using Python. The
objective of this project is to design an interactive game where the computer selects a
random number between 1 and 100, and the user attempts to guess it. Your program will
need to generate a random number, handle user input, and provide feedback based on the
user's guesses.
- By
Md Atiqur Rahman
"""

import random

while True:
    random_number = random.randint(1, 100)
    #print("random number:", random_number)
    print("Welcome to the Number Guessing Game!")

    attempts = 0
    while True:
        try:
            guessing_number = int(input("Try to guess the number between 1 and 100: "))
            attempts += 1
            if guessing_number > random_number:
                print("Too high!")
            elif guessing_number < random_number:
                print("Too Low!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
