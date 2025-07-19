from turtle import Turtle
import random
import config

class Star:

    def __init__(self):
        self.star_list = []

    def create_star(self):
        random_chance = random.randint(1, 20)
        if random_chance == 1:
            new_star = Turtle(shape=config.STAR_IMAGE)
            new_star.penup()
            random_y = random.randint(-230, 200)
            new_star.goto(400,random_y)
            self.star_list.append(new_star)

    def move_star(self):
        for star in self.star_list:
            star.backward(5)




