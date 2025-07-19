from tkinter import messagebox
from turtle import Turtle
import config
import os


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.load_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-150, 210)
        self.update_score()

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_score()
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Courier", 25, "bold"))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", False, "center", font=("Courier", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def load_highscore(self):
        if os.path.exists(config.HIGH_SCORE_FILE):
            try:
                with open(config.HIGH_SCORE_FILE) as f:
                    self.highscore = int(f.read())
            except:
                self.highscore = 0  # handle corrupt file

    def save_highscore(self):
        with open(config.HIGH_SCORE_FILE, mode='w') as f:
            f.write(str(self.highscore))

    def reset_highscore(self):
        if not config.is_game_on:
            confirm = messagebox.askokcancel("Confirm Reset", "Do you want to reset the highscore to 0?")
            if confirm:
                self.highscore = 0
                self.save_highscore()
                self.goto(-150, 210)
                self.update_score()
