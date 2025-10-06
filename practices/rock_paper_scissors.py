#KH rock paper scissors game

import random

user_score = 0
computer_score = 0

while True:
    print("\nType r for rock, p for paper, or s for scissors. Type 'quit' to stop playing.")
    user_choice = input("Your choice: ").lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        print("Final Score - You:", user_score, "Computer:", computer_score)
        break
    elif user_choice == "r" or user_choice == "p" or user_choice == "s":
        if user_choice == "r":
            user_word = "rock"
        elif user_choice == "p":
            user_word = "paper"
        else:
            user_word = "scissors"

        computer_choice = random.choice(["r", "p", "s"])
        if computer_choice == "r":
            computer_word = "rock"
        elif computer_choice == "p":
            computer_word = "paper"
        else:
            computer_word = "scissors"

        print("Computer chose:", computer_word)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "r" and computer_choice == "s") or \
             (user_choice == "p" and computer_choice == "r") or \
             (user_choice == "s" and computer_choice == "p"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print("Score - You:", user_score, "Computer:", computer_score)
    else:
        print("Invalid input. Type r, p, s, or quit.")

