"""
10 dots x-axis and 10 dots y-axis
Dots are 20 in size
Space by 50
"""
import turtle as t
from choice_colors import color_list
import random

screen = t.Screen()
# screen.screensize(100, 100)

hirst = t.Turtle()
t.colormode(255)
t.speed(0)


def make_dot():
    color = random.choice(color_list)
    t.dot(20, color)


def make_row(p1, p2):
    for _ in range(10):
        t.penup()
        t.setposition(p1, p2)
        t.pendown()
        make_dot()
        p1 += 50


pos1 = -300
pos2 = -300

make_row(pos1, pos2)
make_row(pos1, -250)
make_row(pos1, -200)
make_row(pos1, -150)
make_row(pos1, -100)
make_row(pos1, -50)
make_row(pos1, 0)
make_row(pos1, 50)
make_row(pos1, 100)
make_row(pos1, 150)

screen.exitonclick()
