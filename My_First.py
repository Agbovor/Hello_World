import random

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
