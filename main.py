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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:

    # detect collision of player with car
    for each_car in car_manager.all_cars:
        if player.distance(each_car) < 28.28:
            player.collision_detected()
            game_is_on = False

    # detect if turtle has reached the finish line, if Yes, Level up and send back to start line.
    if player.is_at_finish_line():
        player.back_to_start()
        car_manager.level_up()
        scoreboard.level += 1
        scoreboard.update_score()

    car_manager.generate_cars()
    car_manager.move_car()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
