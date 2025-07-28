from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rado_chance = random.randint(1, 6)
        if rado_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            rando_start = random.randint(-250, 250)
            new_car.goto(300, rando_start)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x_pos = car.xcor() - self.car_speed
            car.goto(new_x_pos, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
