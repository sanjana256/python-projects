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

def main():
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


