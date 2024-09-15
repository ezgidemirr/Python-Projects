# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)   #tüm animasyon yok olur, while loop oluşturup scree.update()>> her seferinde

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")  #case sensitive
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    screen.update()   #screen.tracer() ile beraber 0,0 noktasından itibaren animasyonu silmeye yarıyor
    time.sleep(0.1)
    ball.move_the_ball()

    #bouncing from wall
    if ball.ycor() > 283  or ball.ycor() < -283:
        ball.bounce()

    #detect collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320 :
        ball.bounce_paddle()


    #when ball misses right paddle
    if ball.xcor() > 395 :
         ball.reset_position()
         scoreboard.count_score_left()

    # when ball misses leftt paddle
    if ball.xcor() <-395:
        ball.reset_position()
        scoreboard.count_score_right()


screen.exitonclick()
