from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 8


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.init_speed= STARTING_MOVE_DISTANCE

    def create_car(self):
        chance= random.randint(1,5)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y= random.randint(-240, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
          car.setheading(180)
          car.forward(self.init_speed)  #car.backward kullanabilirsin

    def increase_speed(self):
         self.init_speed += MOVE_INCREMENT
    def game_over(self):
        game_overr= Turtle()
        game_overr.write(f"GAME OVER!", move=False, align="center", font=("Arial", 20, "normal"))