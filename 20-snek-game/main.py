from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snek Game")
screen.tracer(0)

seg_li = []

# start_x_pos = 0
# for _ in range(3):
#     tur_ogj = Turtle("square")
#     seg_li.append(tur_ogj)
#     tur_ogj.color("white")
#     tur_ogj.penup()
#     tur_ogj.setpos(x=start_x_pos,y=0)
#     start_x_pos -= 20

start_x_pos = [(0,0), (-20, 0), (-40, 0)]
for pos in start_x_pos:
    tur_ogj = Turtle("square")
    seg_li.append(tur_ogj)
    tur_ogj.color("white")
    tur_ogj.penup()
    tur_ogj.setpos(pos)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    # for seg in seg_li:
    #     seg.forward(20)
    for seg in range(len(seg_li) - 1, 0, -1):
        new_x = seg_li[seg - 1].xcor()
        new_y = seg_li[seg - 1].ycor()
        seg_li[seg].goto(new_x, new_y)
    seg_li[0].forward(20)





screen.exitonclick()
