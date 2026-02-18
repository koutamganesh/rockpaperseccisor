import random
rock='''
     rock
'''
paper='''
     paper
'''

scissors='''

      scissors

'''
game_image=[rock,paper,scissors]
user_choice=int(input("enter your choice: Type 0 for rock,1 for paper,2 for scissors: "))
print(game_image[user_choice])
comp_choice=random.randint(0,2)
print(game_image[comp_choice])
if user_choice>=3 or user_choice<0:
    print("invalid number.you loosd")
else:
    if user_choice==0 and comp_choice==2:
        print(game_image[user_choice])
    elif user_choice==2 and comp_choice==0:
        print(game_image[comp_choice])
    elif user_choice==comp_choice:
        print("its a draw")
    elif user_choice<comp_choice:
        print(game_image[comp_choice])
    elif user_choice>comp_choice:
        print(game_image[user_choice])
