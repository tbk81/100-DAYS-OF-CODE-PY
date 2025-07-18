from turtle import Turtle, Screen

tur_obj = Turtle()
screen = Screen()

def move_forward():
    tur_obj.forward(10)

screen.listen()
screen.onkey(fun=move_forward, key="w")  # When passing a func into a func do not inclue ()

screen.exitonclick()
