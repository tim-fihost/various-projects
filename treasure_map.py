#Treasure game!!!
'''
Program allow to enter the position of the treasure
using a two-digit system. The first digit input is the colomn
number, second digit input is the row'''
game_map = [
    ['⬜','⬜','⬜'],
    ['⬜','⬜','⬜'],
    ['⬜','⬜','⬜']
]
print("==================")
for i in game_map:
    print(i)
print("==================")
print("Where do you want to put treasure?")
user_colomn = int(input("Give the colomn: "))
user_row = int(input("Give the row: "))
game_map[user_colomn][user_row] = "❌"
print("==================")
for i in game_map:
    print(i)
print("==================")