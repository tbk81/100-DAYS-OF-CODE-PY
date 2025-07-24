# TODO 1. Create the screen (h=600xw=800, black bkg)
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

L_POSITION = (-375, 0)
R_POSITION = (365, 0)

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

# TODO 2. Create and move a paddle
l_paddle = Paddle(L_POSITION)

# TODO 3. Create another paddle
r_paddle = Paddle(R_POSITION)

# TODO 4. Create the ball and make it move
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
# TODO 5. Detect collision with wall and bounce

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
w

# TODO 6. Detect collision with paddle
# TODO 7. Detect when paddle misses
# TODO 8. Keep score

screen.exitonclick()
