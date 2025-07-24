from turtle import Turtle

MOVE_DIST = 20

class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setpos(start_pos)

    def up(self):
        new_y_pos = self.ycor() + MOVE_DIST
        self.goto(self.xcor(), new_y_pos)

    def down(self):
        new_y_pos = self.ycor() - MOVE_DIST
        self.goto(self.xcor(), new_y_pos)
