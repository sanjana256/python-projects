import random
game=["rock", "paper", "scissors"]

def user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in game:
            return choice
        print("Invalid choice. Please try again.")


def computer_choice():
    return random.choice(game)

def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def print_instructions():
    """
    Prints the game instructions to guide the user on how to play.
    """
    print("\nWelcome to Rock, Paper, Scissors!")
    print("You will play against the computer.")
    print("\nInstructions:")
    print("1. You will be prompted to choose between 'rock', 'paper', or 'scissors'.")
    print("2. The computer will randomly select one of these options.")
    print("3. The winner is determined based on the following rules:")
    print("   - Rock crushes scissors")
    print("   - Paper covers rock")
    print("   - Scissors cuts paper")
    print("4. After each round, the scores will be updated and displayed.")
    print("5. You can choose to play another round or exit the game at any time.")
    print("Let's get started!\n")

def main():
    print_instructions()
    user_score = 0
    computer_score = 0

    while True:
         user = user_choice()
         computer = computer_choice()
         print(f"Computer chose: {computer}")
         result = winner(user, computer)
         print(result)
    
         if result == "You win!":
             user_score += 1
         elif result == "You lose!":
             computer_score += 1
        
         print(f"Score - You: {user_score} | Computer: {computer_score}")
        
         play_again = input("Do you want to play another round? (yes/no): ").lower()
         if play_again != 'yes':
          print("Thanks for playing!")
          break
main()




