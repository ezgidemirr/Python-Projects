# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player= Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.turtle_move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect passing
    if player.ycor() > 300:
        player = Player()
        screen.onkey(player.turtle_move, "Up")
        scoreboard.count_score()
        car_manager.increase_speed()


    for car in car_manager.all_cars:

      #detect collision with car
      if player.distance(car) < 24:
          game_is_on = False
          car_manager.game_over()




screen.exitonclick()