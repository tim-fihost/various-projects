import random
import turtle as t
tim = t.Turtle()
screen = t.Screen()
SIDE =["right","left"]
colors = ["green yellow","green","antique white","dark red","slate blue","medium blue"]
def lib_choice():
    goto_side = random.choice(SIDE)
    if goto_side == "right":
        tim.right(90)
    else:
        tim.left(90)
tim.shape("circle")
tim.pensize(15)
tim.speed("fastest")
screen.bgcolor("black")
for i in range(200):
    tim.forward(100)
    lib_choice()
    tim.color(random.choice(colors))
  