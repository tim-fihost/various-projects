import random
def level(str_level):
    if str_level == 'hard':
        return 5
    else:
        return 10
number = random.randint(0,100)
user_choice = input("Choose the level 'hard' or 'easy': ")
chances = level(user_choice)
print("Number must be between 0 and 100!")
while True:
    print(f"You have {chances} chances!")
    user_guess = int(input("Guess the number: "))
    if user_guess > number:
        print("Number is too high!")
        chances-=1
    elif user_guess < number:
        print("Number is too low!")
        chances-=1
    else:
        print("==========YOU WON==========")
        print("==========Corret===========")
        break
    if chances == 0:
        print("=========You lost==========")
        print(f"Number was {number}")
        break
    print("===========================")