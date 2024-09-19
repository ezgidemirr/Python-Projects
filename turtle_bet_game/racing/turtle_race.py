# This is a sample Python script.
import turtle
from turtle import Turtle, Screen
import random

is_race_on =False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet ", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)


turtle_green= Turtle()
turtle_blue= Turtle()
turtle_purple= Turtle()
turtle_yellow= Turtle()
turtle_orange= Turtle()
turtle_red = Turtle()

turtle_green.shape("turtle")
turtle_blue.shape("turtle")
turtle_purple.shape("turtle")
turtle_yellow.shape("turtle")
turtle_orange.shape("turtle")
turtle_red.shape("turtle")


turtle_green.penup()
turtle_blue.penup()
turtle_purple.penup()
turtle_yellow.penup()
turtle_orange.penup()
turtle_red.penup()


turtle_red.color("red")
turtle_red.goto(-180,-120)
turtle_green.color("green")
turtle_green.goto(-180, -70)
turtle_blue.color("blue")
turtle_blue.goto(-180,-20)
turtle_purple.color("purple")
turtle_purple.goto(-180,30)
turtle_yellow.color("yellow")
turtle_yellow.goto(-180,80)
turtle_orange.color("orange")
turtle_orange.goto(-180,130)


all_turtles= [turtle_orange,turtle_yellow,turtle_purple,turtle_green,turtle_blue,turtle_red]

if user_bet:
    is_race_on = True

while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color= turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won!!  The {winning_color} turtle is the winner!" )
            else:
                print(f"Sorry! You've lost! The {winning_color} turtle is the winner!")

        rand_pace = random.randint(0, 10)
        turtles.forward(rand_pace)




screen.exitonclick()