import os

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

score_user1 = 0
score_user2 = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    user1_choice = int(input("User 1: Type 0 for rock, 1 for paper, 2 for scissors: "))
    clear_screen()

    user2_choice = int(input("User 2: Type 0 for rock, 1 for paper, 2 for scissors: "))
    clear_screen()

    if user1_choice < 0 or user1_choice > 2:
        score_user2 += 1
        print("Invalid number entered by User 1. User 2 wins this round!")
    elif user2_choice < 0 or user2_choice > 2:
        score_user1 += 1
        print("Invalid number entered by User 2. User 1 wins this round!")
    else:
        print("User1 chose:")
        print(game_image[user1_choice])

        print("User2 chose:")
        print(game_image[user2_choice])

        if user1_choice == user2_choice:
            print("It's a draw 🤝")
        elif (user1_choice - user2_choice) % 3 == 1:
            print("User 1 wins 🏆")
            score_user1 += 1
        else:
            print("User 2 wins 🏆")
            score_user2 += 1

    print("\nCurrent Score -> User1:", score_user1, "| User2:", score_user2)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Final Score of User1:", score_user1, "| User2:", score_user2)
        print("Thanks for playing! ANDI MALLI VACHI AADANDI EE GAMEUUUU ")
        break
