import tkinter as tk
from tkinter import messagebox
import random

user_score = 0
computer_score = 0

def user_choice(choice):
    global user_score, computer_score
    game = ['rock', 'paper', 'scissors']
    user = choice
    computer = random.choice(game)

    result = winner(user, computer)
    update_ui(user, computer, result)
    
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    
    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")

def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def update_ui(user, computer, result):
    try:
        img_user = tk.PhotoImage(file=f"images/player_{user}.png")
        img_computer = tk.PhotoImage(file=f"images/computer_{computer}.png")
        
        user_label.config(image=img_user)
        computer_label.config(image=img_computer)
        result_label.config(text=f"Computer chose: {computer}\n{result}")

        user_label.image = img_user
        computer_label.image = img_computer
        
        root.after(1000, play_again)  # Display the prompt after 1 second
    except tk.TclError as e:
        messagebox.showerror("Image Load Error", f"Error loading image: {e}")

def play_again():
    if messagebox.askyesno("Play Again", "Do you want to play another round?"):
        result_label.config(text="Choose an option to start the game")
        user_label.config(image='')
        computer_label.config(image='')
    else:
        root.quit()

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x400")

try:
    img_rock = tk.PhotoImage(file="images/rock.png")
    img_paper = tk.PhotoImage(file="images/paper.png")
    img_scissors = tk.PhotoImage(file="images/scissors.png")
except tk.TclError as e:
    messagebox.showerror("Image Load Error", f"Error loading image: {e}")

button_frame = tk.Frame(root)
button_frame.pack(side='top', pady=20)

rock_button = tk.Button(button_frame, image=img_rock, command=lambda: user_choice('rock'))
rock_button.pack(side='left', padx=10)

paper_button = tk.Button(button_frame, image=img_paper, command=lambda: user_choice('paper'))
paper_button.pack(side='left', padx=10)

scissors_button = tk.Button(button_frame, image=img_scissors, command=lambda: user_choice('scissors'))
scissors_button.pack(side='left', padx=10)

display_frame = tk.Frame(root)
display_frame.pack(side='top', pady=20)

user_label = tk.Label(display_frame)
user_label.pack(side='left', padx=10)

computer_label = tk.Label(display_frame)
computer_label.pack(side='left', padx=10)

result_label = tk.Label(root, text="Choose an option to start the game")
result_label.pack(side='bottom', pady=10)

score_label = tk.Label(root, text="User: 0 | Computer: 0")
score_label.pack(side='bottom', pady=10)

root.mainloop()





