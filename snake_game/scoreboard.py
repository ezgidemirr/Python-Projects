
from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.new_score = 0
        self.high_score =0
        self.color("white")
        self.penup()
        self.goto(0, 305)
        self.update_score()
        self.hideturtle()  #hides the arrow shape at the center (turtle)


    def update_score(self):
        self.clear()  #clears before new score
        self.write(f"Score: {self.new_score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 13, "normal"))

    def reset(self):
        if self.new_score > self.high_score:
             self.high_score = self.new_score
        self.new_score = 0
        self.update_score()

    def increase_score(self):
        self.new_score += 1
        self.update_score()

    #def game_over(self):
        #self.clear() eğer score ve konum görmek istiyorsan sil
       # self.color("white")
        #self.goto(0, 0)
        #self.write(f"GAME OVER!", move=False, align="center", font=("Arial", 20, "normal"))

