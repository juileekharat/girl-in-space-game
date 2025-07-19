# core/game_loop.py
import tkinter
from turtle import Terminator
import pygame
import config
import time

from core.ui import show_play_again_message
from core.game_controls import pause_game, resume_game, mute_sound, unmute_sound, restart_game, quit_game
from core.ui import show_options

from components.asteroid import Asteroid
from components.player import Player
from components.scoreboard import Scoreboard
from components.star import Star
from components.background_stars import BackgroundStar

def start_game(screen):
    config.is_paused = False
    config.is_quitting = False

    pygame.mixer.music.load(config.BACKGROUND_MUSIC)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # Add this:
    if config.is_muted:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(0.3)

    screen.clear()
    screen.bgcolor(config.BG_COLOR)
    screen.addshape(config.PLAYER_IMAGE)
    screen.addshape(config.ASTEROID_IMAGE)
    screen.addshape(config.STAR_IMAGE)
    screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
    screen.tracer(0)

    bg_stars = BackgroundStar(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    asteroid = Asteroid()
    star = Star()
    scoreboard = Scoreboard()
    player = Player()

    show_options()

    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_down, "Down")
    screen.onkey(pause_game, "p")
    screen.onkey(resume_game, "r")
    screen.onkey(mute_sound, "m")
    screen.onkey(unmute_sound, "u")
    screen.onkey(lambda: restart_game(screen, start_game), "s")
    screen.onkey(lambda: quit_game(screen), "q")
    screen.onkey(scoreboard.reset_highscore, "x")

    try:
        config.is_game_on = True
        while config.is_game_on:
            if config.is_quitting:
                return
            if config.is_paused:
                screen.update()
                time.sleep(0.1)
                continue

            time.sleep(0.03)
            screen.update()

            bg_stars.twinkle()
            asteroid.create_asteroid()
            asteroid.move_asteroid()
            star.create_star()
            star.move_star()

            for current_star in star.star_list[:]:
                if current_star.distance(player) < config.STAR_COLLISION_DISTANCE:
                    if not config.is_muted:
                        pygame.mixer.Sound(config.STAR_COLLIDE_SOUND).play()
                    scoreboard.increase_score()
                    current_star.hideturtle()
                    star.star_list.remove(current_star)

            for current_asteroid in asteroid.asteroid_list[:]:
                if current_asteroid.distance(player) < 15:
                    if not config.is_muted:
                        pygame.mixer.Sound(config.GAME_OVER_SOUND).play()
                    pygame.mixer.music.stop()
                    scoreboard.game_over()
                    show_play_again_message(screen, start_game, quit_game)
                    config.is_game_on = False
    except (Terminator, tkinter.TclError):
        pass
