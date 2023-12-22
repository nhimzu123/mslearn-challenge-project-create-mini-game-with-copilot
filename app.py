# Create a rock, paper, scissors game
# This is a game between the player and the computer
# The computer will randomly choose rock, paper, or scissors
# The player will choose rock, paper, or scissors from the command line with input() function,
# if player enters anything other than rock, paper, or scissors, the program will ask the user to enter again
# At each round, the player should be informed if they won or lost or tied with the computer
# By the end of each round, the player can choose to play again or quit the game with "yes" or "no" input
# Store and display the player's score and computer's score.

# Import random module
import random

# Create a list of choices
choices = ["rock", "paper", "scissors"]

# Create a variable to store the player's score  and computer's score
player_score = 0
computer_score = 0

# Create a title for the game
print("Welcome to the Rock, Paper, Scissors Game!")

# Create a variable to store game round
round = 1

# Create a while loop to keep the game running
while True:
    # Print out the round number
    print('-----------------------------------')
    print(f"Round {round}")

    # Receive input from the player
    player = input("Please enter rock, paper, or scissors: ")

    # Create a condition to check if the player's input is valid and request user to re-enter if not valid using continue while loop
    while player.lower() not in choices:
        print("\nInvalid input. Please enter rock, paper, or scissors.")
        
        player = input("Please enter rock, paper, or scissors: ")
    
    # Create a variable to store the computer's choice
    computer = random.choice(choices)

    # Create a condition to check if the player and computer tied
    if player.lower() == computer:
        print("You tied with the computer!")
        print(f"Your choice: {player.lower()}")
        print(f"Computer's choice: {computer}")
        print(f"Your score: {player_score}")
    
    # Create a condition to check if the player won
    elif (player.lower() == "rock" and computer == "scissors") or (player.lower() == "paper" and computer == "rock") or (player.lower() == "scissors" and computer == "paper"):
        player_score += 1

        print("You won!")
        print(f"Your choice: {player.lower()}")
        print(f"Computer's choice: {computer}")
        print(f"Your score: {player_score}")
    # Create a condition to check if the player lost
    else:
        computer_score += 1

        print("You lost!")
        print(f"Your choice: {player.lower()}")
        print(f"Computer's choice: {computer}")
        print(f"Your score: {player_score}")
    
    # Create a condition to check if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")

    # Create a condition to check if the player wants to quit the game and increase the round number
    if play_again.lower() == "no":
        print(f"Thank you for playing!")
        print(f"Your final score: {player_score}")
        print(f"Computer's final score: {computer_score}")
        break
    else:
        round += 1
        continue