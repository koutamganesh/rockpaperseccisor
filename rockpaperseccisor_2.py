import random

rock = '''
    it's rock
'''

paper = '''
    it's paper
'''

scissors = '''
    it's scissors
'''

game_image = [rock, paper, scissors]

user_choice = int(input("Enter your choice: Type 0 for rock, 1 for paper, 2 for scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("Invalid number. You lose!")
else:
    print("You chose:")
    print(game_image[user_choice])

    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_image[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("User wins 🏆")
    elif user_choice == 2 and comp_choice == 0:
        print("Computer wins 🏆")
    elif user_choice == comp_choice:
        print("It's a draw 🤝")
    elif user_choice > comp_choice:
        print("User wins 🏆")
    else:
        print("Computer wins 🏆")
