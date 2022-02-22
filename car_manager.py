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

    def generate_cars(self):
        random_num = random.randint(0, 5)
        if random_num == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            car_y_cor = random.randrange(-250, 250, 20)
            new_car.goto(300, car_y_cor)
            self.all_cars.append(new_car)

    def move_car(self):
        for each_car in self.all_cars:
            each_car.forward(self.car_speed)

    def increase_speed_on_level_up(self):
        self.car_speed += MOVE_INCREMENT
