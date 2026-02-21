import tkinter as tk
import random

choices = ["Rock 🪨", "Paper 📄", "Scissors ✂️"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    comp_choice = random.randint(0, 2)

    user_label.config(text="You chose: " + choices[user_choice])
    comp_label.config(text="Computer chose: " + choices[comp_choice])

    """if user_choice == comp_choice:
        result_label.config(text="It's a Draw 🤝")
    elif (user_choice - comp_choice) % 3 == 1:
        result_label.config(text="You Win! 🏆")
        user_score += 1
    else:
        result_label.config(text="Computer Wins! 💻🏆")
        computer_score += 1"""

    if user_choice == 0 and comp_choice == 2:
        result_label.config(text="You Win! 🏆")
        user_score+=1
    elif user_choice == 2 and comp_choice == 0:
        result_label.config(text="Computer Wins! 💻🏆")
        computer_score+=1
    elif user_choice == comp_choice:
        result_label.config(text="It's a Draw 🤝")
    elif user_choice > comp_choice:
        result_label.config(text="User wins 🏆")
        user_score+=1
        computer_score+=1
    else:
        result_label.config(text="computer 🏆")

    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x450")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 18, "bold"))
title.pack(pady=15)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock 🪨", width=12, height=2,
          command=lambda: play(0)).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Paper 📄", width=12, height=2,
          command=lambda: play(1)).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Scissors ✂️", width=12, height=2,
          command=lambda: play(2)).grid(row=0, column=2, padx=10)


user_label = tk.Label(root, text="", font=("Arial", 12))
user_label.pack(pady=10)

comp_label = tk.Label(root, text="", font=("Arial", 12))
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=15)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0",
                       font=("Arial", 12))
score_label.pack(pady=10)



root.mainloop()
