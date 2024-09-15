# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Turtle, Screen

var1= Turtle()
screen = Screen()

def move_forwards():
    var1.forward(10)

def move_backwards():
    var1.backward(10)


def move_left():
    new_heading = var1.heading() - 15
    var1.setheading(new_heading)


def move_right():
    new_heading= var1.heading() + 15
    var1.setheading(new_heading)


def clear():
    var1.clear()
    var1.penup()
    var1.home()
    var1.pendown()


screen.listen()
screen.onkey(key= "w", fun= move_forwards)
screen.onkey(key= "a", fun= move_left)
screen.onkey(key= "s", fun= move_backwards)
screen.onkey(key= "d", fun= move_right)
screen.onkey(key= "c", fun= clear)
screen.exitonclick()
