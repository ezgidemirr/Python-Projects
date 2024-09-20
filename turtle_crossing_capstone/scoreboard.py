from turtle import Turtle

FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 1
        self.penup()
        self.hideturtle()
        self.goto(-255,270)
        self.write(f"Level:{self.score}", move=False, align="center", font=(FONT))

    def count_score(self):
        self.clear()
        self.score +=1
        self.write(f"Level: {self.score}", move=False, align="center", font=(FONT))



