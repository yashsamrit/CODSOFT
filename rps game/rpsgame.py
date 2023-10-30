import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("\nRock, Paper, Scissors Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    player_choice = input("Enter your choice (1/2/3/4): ")

    if player_choice == "4":
        print("Thanks for playing!")
        break
    elif player_choice in ("1", "2", "3"):
        player_choice = ["rock", "paper", "scissors"][int(player_choice) - 1]
        computer_choice = get_computer_choice()
        print(f"You chose {player_choice}")
        print(f"Computer chose {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
    else:
        print("Invalid choice. Please try again.")
