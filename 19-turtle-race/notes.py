from turtle import Turtle, Screen

tur_obj = Turtle()
screen = Screen()


def move_forward():
    tur_obj.forward(10)


def move_backward():
    tur_obj.backward(10)


def move_left():
    tur_obj.left(10)


def move_right():
    tur_obj.right(10)


def clear_screen():
    tur_obj.clear()
    tur_obj.penup()
    tur_obj.hideturtle()
    tur_obj.home()
    tur_obj.pendown()
    tur_obj.showturtle()


screen.listen()
screen.onkey(fun=move_forward, key="w")  # When passing a func into a func do not include ()
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()
