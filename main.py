import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # detect collision of player with car
    for each_car in car_manager.all_cars:
        if player.distance(each_car) < 28.28:
            game_is_on = False
            print("collision detected")

    # detect if turtle has reached the finish line, if Yes, Level up and send back to start line.
    if player.is_at_finish_line():
        player.back_to_start()
        car_manager.level_up()

    car_manager.generate_cars()
    car_manager.move_car()
