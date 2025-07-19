# config.py

import os

# Base directory of the project (girl_in_space)
BASE_DIR = os.path.dirname(__file__)

# Corrected asset paths
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')

PLAYER_IMAGE_NAME = 'girl.gif'
ASTEROID_IMAGE_NAME = 'asteroid.gif'
STAR_IMAGE_NAME = 'star.gif'

PLAYER_IMAGE = os.path.join(IMAGES_DIR, PLAYER_IMAGE_NAME)
ASTEROID_IMAGE = os.path.join(IMAGES_DIR, ASTEROID_IMAGE_NAME)
STAR_IMAGE = os.path.join(IMAGES_DIR, STAR_IMAGE_NAME)

BACKGROUND_MUSIC = os.path.join(SOUNDS_DIR, 'background_music.wav')
STAR_COLLIDE_SOUND = os.path.join(SOUNDS_DIR, 'star_collides.wav')
GAME_OVER_SOUND = os.path.join(SOUNDS_DIR, 'game_over.wav')

BG_COLOR = "#0E2148"

STAR_COLLISION_DISTANCE = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# Game flags
is_paused = False
is_muted = False
is_game_on = False
is_quitting = False
pause_message = None

def get_highscore_path():
    user_data_dir = os.path.expanduser("~")
    game_dir = os.path.join(user_data_dir, ".girl_in_space")
    os.makedirs(game_dir, exist_ok=True)
    return os.path.join(game_dir, "highscore.txt")

HIGH_SCORE_FILE = get_highscore_path()
