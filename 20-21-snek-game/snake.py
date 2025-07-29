from turtle import Turtle

START_X_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
NORTH = 90
WEST = 180
EAST = 0
SOUTH = 270


class Snake:

    def __init__(self):
        self.seg_li = []
        self.create_snake()
        self.head = self.seg_li[0]

    def create_snake(self):
        for pos in START_X_POS:
            self.add_seg(pos)

    def move(self):
        for seg in range(len(self.seg_li) - 1, 0, -1):
            new_x = self.seg_li[seg - 1].xcor()
            new_y = self.seg_li[seg - 1].ycor()
            self.seg_li[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def add_seg(self, pos):
        tur_obj = Turtle("square")
        self.seg_li.append(tur_obj)
        tur_obj.color("white")
        tur_obj.penup() 
        tur_obj.setpos(pos)

    def extend(self):
        self.add_seg(self.seg_li[-1].position())

    def reset_snake(self):
        for seg in self.seg_li:
            seg.goto(1000, 1000)
        self.seg_li.clear()
        self.create_snake()
        self.head = self.seg_li[0]

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def down(self):
        if self.head.heading() != NORTH:
            self.seg_li[0].setheading(SOUTH)
