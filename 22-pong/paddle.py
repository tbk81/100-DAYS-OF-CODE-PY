from turtle import Turtle

START_POS = (-700, 0)
MOVE_DIST = 50
NORTH = 90
SOUTH = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()
    
    def create_paddle(self):
        paddle = Turtle("square")
        paddle.hideturtle()
        paddle.penup()
        paddle.color("white")
        paddle.setheading(90)
        paddle.shapesize(stretch_len=5, stretch_wid=1)
        paddle.setpos(x=-385, y=0)
        paddle.showturtle()

    def up(self):
        new_ypos = self.ycor() + 20
        self.goto(self.xcor(), new_ypos)
    
    def down(self):
        # self.heading(SOUTH)
        self.backward(MOVE_DIST)
