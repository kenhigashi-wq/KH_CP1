# KH 2nd fix the game practice

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0 # attempts don't equal zero I think.
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")
        guess = int(guess)  # First make this a int, cuz the computer can't compare a str and an int and say which is bigger, im pretty sure this is a I think this is a runtime error
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess < number_to_guess: # Logic error, just switch the <> and low, high with 21 and 23
            print("Too low! Try again.")# SO BASICALLY TWO ERRORS.
        elif guess > number_to_guess:
            print("Too high! Try again.")  
        else:
            print("That shouldn't happem")
        continue
    print("Game Over. Thanks for playing!")
        
start_game()