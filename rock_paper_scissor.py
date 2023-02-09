#Rock Scissor and Paper Game

import random

def condtion(input_statet):
    if input_statet == 1:
        print(paper)
    elif input_statet == 0:
        print(rock)
    else:
        print(scissors)

def printing(user_choice, computer_choice):
    print("You chose")
    condtion(user_choice)
    print("Computer chose")
    condtion(computer_choice)

rock = "🪨"
paper = "📃"
scissors = "✂️"
computer_choice = random.randint(0,2)
print("Type: 0 for Rock, 1 for Paper, 2 for Scissors")
user_choice = int(input("Whad do you choose?"))

if user_choice > 2 and user_choice < 0:
    print("Invalid number, nubmer must be from 0 to 2")
elif user_choice == 2 and computer_choice == 0:
    printing(user_choice,computer_choice)
    print("You lost the game!")
elif computer_choice == 2 and user_choice == 0:
    printing(user_choice,computer_choice)
    print("You won the game!")
elif user_choice > computer_choice:
    printing(user_choice,computer_choice)
    print("You won the game!")
elif user_choice < computer_choice:
    printing(user_choice,computer_choice)
    print("You lost the game!")
else:
    printing(user_choice,computer_choice)
    print("No one wins")
