from turtle import Turtle
from random import randint


class Food(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("circle")  #don't need to food.turtle() no need for new variable inherits from turtle
         self.penup()
         self.shapesize(stretch_wid=0.5,stretch_len=0.5) #halves the shape size
         self.color("red")
         self.speed("fastest")
         self.rand_position()  #ilk foodun 0,0 da başlamamasını sağladı bunu buraya yazmak!!

     def rand_position(self):
         self.goto(randint(-306,306), randint(-306,306)) #you can create variable rand_x and rand_y and put that inside goto()
         # eğer mainde food= Food() call edilirse her seferinde yeni turtle (circle create edilir),
         #sadece rand_position call etmek yerini değiştirir sadece 1 food olur