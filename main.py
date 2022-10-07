import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Help the turtle cross the Road")
screen.tracer(0)

player = Player()

screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect colision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    #Detect if the player reaches the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.next_level()


screen.exitonclick()