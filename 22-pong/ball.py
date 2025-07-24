from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shapesize()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y_pos = self.ycor() + self.y_move
        new_x_pos = self.xcor() + self.x_move
        self.goto(new_x_pos, new_y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

