from turtle import Turtle
import random

class BackgroundStar:
    def __init__(self, screen_width, screen_height, count=50):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.stars = []

        for _ in range(count):
            star = Turtle("circle")
            star.penup()
            star.color("white")
            star.shapesize(0.05, 0.05)  # Tiny dots
            star.speed(0)
            self.random_position(star)
            self.stars.append(star)

    def random_position(self, star):
        x = random.randint(-self.screen_width//2 + 10, self.screen_width//2 - 10)
        y = random.randint(-self.screen_height//2 + 10, self.screen_height//2 - 10)
        star.goto(x, y)

    def twinkle(self):
        for star in self.stars:
            chance = random.randint(1, 20)
            if chance == 1:
                star.hideturtle()
            elif chance == 2:
                star.showturtle()
            elif chance == 3:
                self.random_position(star)
