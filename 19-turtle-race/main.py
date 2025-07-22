from turtle import Turtle, Screen
import random

start_race = False
screen = Screen()
screen.setup(width=500, height=400)
usr_bet = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race? Enter a color:")
print(usr_bet)

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
all_turtles = []
y_pos = -70

for c in colors:
    tur_obj = Turtle(shape="turtle")
    tur_obj.color(c)
    tur_obj.penup()
    tur_obj.goto(x=-240, y=y_pos)
    y_pos += 30
    all_turtles.append(tur_obj)

if usr_bet:
    start_race = True

while start_race:
    for turtle in all_turtles:
        if turtle.xcor() > 221:
            winning_turtle = turtle.pencolor()
            start_race = False
            if winning_turtle == usr_bet:
                print(f"You win! The winning turtle was {winning_turtle}.")
            else:
                print(f"You lose! The winning turtle was {winning_turtle}.")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
