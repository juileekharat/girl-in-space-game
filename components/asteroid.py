from turtle import Turtle
import random
import config

class Asteroid:

    def __init__(self):
        self.asteroid_list = []

    def create_asteroid(self):
        random_chance = random.randint(1, 35)
        if random_chance == 1:
            new_asteroid = Turtle(config.ASTEROID_IMAGE)
            new_asteroid.penup()
            # new_asteroid.speed("fastest")
            random_y = random.randint(-230, 200)
            new_asteroid.goto(400,random_y)
            self.asteroid_list.append(new_asteroid)

    def move_asteroid(self):
        for asteroid in self.asteroid_list:
            asteroid.backward(5)




