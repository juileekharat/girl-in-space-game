# main.py

from turtle import Screen
import pygame
from core.game_loop import start_game

pygame.init()
pygame.mixer.init()

screen = Screen()
screen.title("Girl In Space")
screen._root.resizable(False, False)
start_game(screen)
screen.mainloop()
