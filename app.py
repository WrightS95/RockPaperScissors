#rock, paper, scissors

#no matter your choice, computer chooses a random one
#rock = rock
#rock<paper
#rock>scissors...and so on

import random
choices = ["Rock", "Paper", "Scissors"]
playing = input("Would you like to play? Y/N ")
#test
while playing == "Y":
    user_choice = input("Rock, Paper, or Scissors?  ")
    computer_choice = random.choice(choices)
    if user_choice == "N":
        print("Bye!")
        break
    if user_choice == "Rock":  # --------------user choice = rock
        print(f"{computer_choice}")
        if computer_choice == "Rock":
            print("Tie!")
        if computer_choice == "Scissors":
            print("You win!")
        if computer_choice == "Paper":
            print("You lose!")
        if user_choice == "N":
            print("Bye!")
            break
    if user_choice == "Paper": # --------------user choice = paper
        print(f"{computer_choice}")
        if computer_choice == "Rock":
            print("You win!")
        if computer_choice == "Scissors":
            print("You lose!")
        if computer_choice == "Paper":
            print("Tie!")
        if user_choice == "N":
            print("Bye!")
            break
    if user_choice == "Scissors": # --------------user choice = scissors
        print(f"{computer_choice}")
        if computer_choice == "Rock":
            print("You lose!")
        if computer_choice == "Scissors":
            print("You tie!")
        if computer_choice == "Paper":
            print("You win!")
        if user_choice == "N":
            print("Bye!")
            playing = False
            break
else:
    print("Your loss!")










