# ROCK PAPer SCISSORS GAME
import random
while True:
    def rock_paper_scissors():
        print("Welcome to Rock, Paper, Scissors!")
    player_choice = input("Enter your choice (R for rock, P for paper, S for scissors): ")
    choices = ["R", "P", "S"]
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "R" and computer_choice == "S") or \
         (player_choice == "P" and computer_choice == "R") or \
         (player_choice == "S" and computer_choice == "P"):
        print("You win!")
    else:
        print("Computer wins!") 
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() != "Y":
        print("Thanks for playing!")
        break



