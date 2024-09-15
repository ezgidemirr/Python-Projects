# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
from turtle import Screen, Turtle
from snake import Snake
from scoreboard import Scoreboard
from food import Food


screen = Screen() #creating screen
screen.setup(width= 650, height= 650)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake= Snake()  #calling snake functionality
food = Food()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move() #call ederken self.move diye etme

    #detect collision with food
    if snake.head.distance(food) < 14:
        food.rand_position()
        scoreboard.increase_score()
        snake.extend()
        # eğer mainde food= Food() call edilirse her seferinde yeni turtle (circle create edilir),
        # sadece rand_position call etmek yerini değiştirir sadece 1 food olur

    # detect collision with wall
    if  snake.head.xcor() > 318 or  snake.head.xcor() < -318 or snake.head.ycor() > 318 or  snake.head.ycor() < -318:
        #game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset_snake()


    # detect collision with tail
    for segment in snake.segments[1:]: #ilk eleman hariç tüm list alma (head), bunu yapınca alttaki if'e gerek kalmıcak
       #if segment == snake.head:  #yılanın kafasını hesaba katarsak dirket game over oluyor, bunu engellemek için
          # pass                        #python slicing attribute
       if snake.head.distance(segment) < 10 :
           #game_is_on = False
           #scoreboard.game_over()
           scoreboard.reset()
           snake.reset_snake()




screen.exitonclick()