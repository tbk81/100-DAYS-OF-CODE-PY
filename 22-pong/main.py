# TODO 1. Create the screen (h=600xw=800, black bkg)
from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

# TODO 2. Create and move a paddle
paddle1 = Paddle()

# TODO 3. Create another paddle

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

# TODO 4. Create the ball and make it move
# TODO 5. Detect collision with wall and bounce
# TODO 6. Detect collision with paddle
# TODO 7. Detect when paddle misses
# TODO 8. Keep score

screen.exitonclick()
