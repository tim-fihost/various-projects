
import random
stages = [
    '---------------',
    '            |  ',
    '            0  ',
    '           /|\ ',
    '           / \ ',
    '    You  Lost  ',
]
lives = len(stages)
stage_range = 0
word_list = ["camel",'apple',"wolf"]
chosen_word = word_list[random.randint(0,2)] 
print(chosen_word)
display = ["_"] *len(chosen_word)
print(display)
game_condition = False
print(lives)
while not game_condition:
    guess = input("Guess a letter: ").lower()
    print(guess)
    for i in range(len(chosen_word)):
        address = chosen_word[i]
        if guess == address:
            display[i] = address
    print(display)
    if "_" not in display:
        game_condition = True
        print("Congratulations!,You Won the game")
        print(display)
    if guess not in chosen_word:
        for i in range(stage_range):
            print(stages[i])
        lives -=1
        stage_range +=1
        if lives == 0:
            print("You lost!")
            break