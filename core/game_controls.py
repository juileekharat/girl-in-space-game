# core/game_controls.py

from turtle import Turtle
from tkinter import messagebox
import pygame
import config

def pause_game():
    if not config.is_game_on or config.is_paused or config.is_quitting:
        return
    config.is_paused = True
    pygame.mixer.music.pause()

    config.pause_message = Turtle()
    config.pause_message.hideturtle()
    config.pause_message.color("white")
    config.pause_message.penup()
    config.pause_message.goto(0, -80)
    config.pause_message.write("⏸️ Paused\nPress R to resume", align="center", font=("Courier", 18, "bold"))

def resume_game():
    if not config.is_game_on or not config.is_paused or config.is_quitting:
        return
    config.is_paused = False
    pygame.mixer.music.unpause()
    if config.pause_message:
        config.pause_message.clear()

def mute_sound():
    if config.is_game_on and not config.is_muted:
        config.is_muted = True
        pygame.mixer.music.set_volume(0)

def unmute_sound():
    if config.is_game_on and config.is_muted:
        config.is_muted = False
        pygame.mixer.music.set_volume(0.3)

def restart_game(screen, start_game):
    if config.is_game_on:
        confirm = messagebox.askokcancel("Confirm Restart", "Do you want to restart the game?")
        if confirm:
            config.is_game_on = False
            pygame.mixer.music.stop()
            start_game(screen)

def quit_game(screen):
    import config
    if config.is_game_on:
        confirm = messagebox.askokcancel("Confirm Quit", "Do you want to quit the game?")
        if not confirm:
            return
    config.is_quitting = True
    config.is_game_on = False
    pygame.mixer.music.stop()
    screen.bye()
    raise SystemExit  # 🛑 Ensures no further code runs

