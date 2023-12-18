import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_selection, computer_selection):
    if player_selection == computer_selection:
        return "It's a draw!"
    elif (player_selection == "rock" and computer_selection == "scissors") or \
         (player_selection == "paper" and computer_selection == "rock") or \
         (player_selection == "scissors" and computer_selection == "paper"):
        return "Congratulations! You are victorious."
    else:
        return "Alas! The machine has defeated you this time."


while True:
    player_choice = input("Select your choice (rock, paper, scissors): ").lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please choose again.")
        continue

    computer_choice = get_computer_choice()
    print(f"\nYou chose {player_choice}, your opponent chose {computer_choice}.\n")

    result_message = determine_winner(player_choice, computer_choice)
    print(result_message)

    if input("Do you wish to challenge again? (yes/no): ").lower() == "no":
        print("Thank you for playing! Farewell!")
        break
    else:
        continue


