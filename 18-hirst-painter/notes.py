import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("circle")
turtle.colormode(255)


# tim.color("red")


# Draw a square
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# Draw a dotted line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw 7 shapes in a row
# def color_gen():
#     return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
#
# def shape(sides):
#     tim.pencolor(color_gen())
#     for _ in range(sides):
#         tim.right(360 / sides)
#         tim.forward(100)
#
#
# for shape_num in range(3, 11):
#     shape(shape_num)

# Random walk
# tim.shapesize(.25, .25, .25)
# tim.pensize(10)
# def color_gen():
#     return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
#
#
# def rando_walk():
#     tim.pencolor(color_gen())
#     dir_int = random.randint(0, 360)
#     tim.setheading(dir_int)
#     tim.forward(25)
#
#
# for _ in range(25):
#     rando_walk()

# Spirograph
tim.speed(0)
def color_gen():
    return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)

def spiro():
    tim.pencolor(color_gen())
    tim.circle(100)
    tim.left(6)


for _ in range(60):
    spiro()

screen = Screen()
screen.exitonclick()
