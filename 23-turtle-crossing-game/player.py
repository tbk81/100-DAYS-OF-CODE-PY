from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y_pos)

    # def move_down(self):
    #     new_y_pos = self.ycor() - MOVE_DISTANCE
    #     self.goto(self.xcor(), new_y_pos)

    # def move_left(self):
    #     new_x_pos = self.xcor() - MOVE_DISTANCE
    #     self.goto(new_x_pos, self.ycor())

    # def move_right(self):
    #     new_x_pos = self.xcor() + MOVE_DISTANCE
    #     self.goto(new_x_pos, self.ycor())
