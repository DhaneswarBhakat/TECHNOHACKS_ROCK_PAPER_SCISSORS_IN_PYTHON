import random
import tkinter as tk
from tkinter import messagebox

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_choice = player_choice_var.get()

    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)
    messagebox.showinfo("Result", result)

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x300")
window.configure(bg='#f9e3a1')

# Create a label
label = tk.Label(window, text="Choose one of the following:", font=("Arial", 12), bg='#f9e3a1')
label.pack(pady=10)

# Create radio buttons for player's choice
player_choice_var = tk.StringVar()
player_choice_var.set("rock")
for choice in ['rock', 'paper', 'scissors']:
    rb = tk.Radiobutton(window, text=choice.capitalize(), variable=player_choice_var,
                        value=choice, indicatoron=0, width=10, font=("Arial", 10), bg='#a1d2f9', fg='white')
    rb.pack(pady=5)

# Create a button to play the game
play_button = tk.Button(window, text="Play", command=play_game, font=("Arial", 12), bg='#f98181', fg='white')
play_button.pack(pady=10)

# Run the main loop
window.mainloop()
