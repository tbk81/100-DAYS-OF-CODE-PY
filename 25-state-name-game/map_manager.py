from turtle import Turtle


class MapManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def show_state(self, name, coordinates):
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(coordinates)
        new_state.write(name)




