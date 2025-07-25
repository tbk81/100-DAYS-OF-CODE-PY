from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


L_POSITION = (-375, 0)
R_POSITION = (365, 0)

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

l_paddle = Paddle(L_POSITION)
r_paddle = Paddle(R_POSITION)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    elif ball.xcor() > 370:
        ball.pos_reset()
        scoreboard.l_point()
    elif ball.xcor() < -385:
        ball.pos_reset()
        scoreboard.r_point()

screen.exitonclick()
