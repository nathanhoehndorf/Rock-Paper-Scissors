import tkinter as tk
import random

user_choice = ""
result = ""

choices = ['Rock', 'Paper', 'Scissors']
wins = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}


def who_wins():
    global result
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        output.set("It's a Tie!")
    elif user_choice == wins[comp_choice]:
        output.set("You Lose.")
    elif comp_choice == wins[user_choice]:
        output.set("You Win!")
    else:
        output.set("Something went wrong.")


def set_user_choice(symbol):
    global user_choice
    user_choice = symbol
    who_wins()


root = tk.Tk()
root.title("Rock Paper Scissors")

frame = tk.Frame(root)
rock_button = tk.Button(frame, text="Rock", command=lambda: set_user_choice("Rock"))
rock_button.grid(row=1, column=1)

paper_button = tk.Button(frame, text="Paper", command=lambda: set_user_choice("Paper"))
paper_button.grid(row=1, column=2)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: set_user_choice("Scissors"))
scissors_button.grid(row=1, column=3)

frame.pack()

output = tk.StringVar()
output.set("")

label = tk.Label(root, textvariable=output)
label.pack()

root.mainloop()
