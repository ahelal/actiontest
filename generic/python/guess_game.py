#!/usr/bin/env python3 


import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 1

    print("Welcome to the number guessing game!")
    print("I have selected a number between 1 and 10. Can you guess it?")

    while True:
        user_guess = input("Enter your guess: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if user_guess < 1 or user_guess > 10:
            print("Your guess is out of bounds. Please guess a number between 1 and 10.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number()
