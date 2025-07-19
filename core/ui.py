# core/ui.py

from turtle import Turtle
import config

def show_options():
    if config.is_quitting:
        return
    hints = [
        ("P⏸️", 160),  # Pause
        ("S🔁", 200),  # Restart
        ("Q❌", 240),  # Quit
        ("M🔇/U🔊", 285)  # Mute/Unmute
    ]
    for label, x in hints:
        hint = Turtle()
        hint.hideturtle()
        hint.color("white")
        hint.penup()
        hint.goto(x, 215)
        hint.write(label, align="left", font=("Courier", 13, "normal"))

def show_play_again_message(screen, start_game, quit_game):
    if config.is_quitting:
        return
    message = Turtle()
    message.hideturtle()
    message.color("white")
    message.penup()
    message.goto(0, -80)
    message.write("Press SPACE to play again\nPress Q to quit\nPress X to Reset Highscore", align="center", font=("Courier", 18, "bold"))

    screen.listen()
    screen.onkey(lambda: start_game(screen), "space")
    screen.onkey(lambda: quit_game(screen), "q")
