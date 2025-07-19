from turtle import Turtle
import config

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(config.PLAYER_IMAGE)
        self.penup()
        self.goto(-350, 0)

    def go_up(self):
        if self.ycor() < 200:
            self.sety(self.ycor() + 15)

    def go_down(self):
        if self.ycor() > -200:
            self.sety(self.ycor() - 15)

