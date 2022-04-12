import random

while True:
    user_action = input("Enter a choice, rock, paper, scissors")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print ("You chose " + user_action + " and the computer chose " + computer_action + ".\n")

    if user_action == computer_action:
        print ("Both you and the computer chose " + user_action + " It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print ("Rock beats Scissors. You Win :)")
        else:
            print ("Paper beats Rock, You Lose :(")
    elif user_action == "paper":
        if computer_action == "rock":
            print ("Paper beats Rock. You Win :)")
        else:
            print ("Scissors beats Paper. You Lose :(")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors beats Paper, You Win :)")
        else:
            print("Rock beats Scissors, You Lose :(")
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "n":
        break