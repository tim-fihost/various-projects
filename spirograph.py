import turtle as t 
import random
tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")
screen.colormode(255)
def colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
def draw(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(200)
        tim.setheading(tim.heading() + size_of_gap)
        tim.pencolor(colors())
draw(5)
    