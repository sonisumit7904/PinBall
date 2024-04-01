import pygame
import os,sys
pygame.font.init()

# GENERAL VARIABLES
gameW, gameH = 400, 600
playerW, playerH = 60, 120
gridLength = 5

# COLORS
colors = {
    'ball': (234,206,205),
    'flipper': (226, 135, 80),
    'wall': (30, 23, 36),
    'releaser': (18, 13, 21),
    'bg': (56, 45, 62),
    'score': (95,86,100),
    'white': (255,255,255),
    'black': (0,0,0)
}

# FONTS
ttf_path = os.path.join(sys.path[0], "fonts/muli.ttf")
muli = {
    "15": pygame.font.Font(ttf_path,15),
    "20": pygame.font.Font(ttf_path,20),
    "30": pygame.font.Font(ttf_path,30),
    "70": pygame.font.Font(ttf_path,70)
}

# ACCELERATION // 1.11m/s
TABLE_ACCELERATION = 0.2

# STATES
TITLE_SCREEN = 1
GAME_OVER = 2
STAGE_ONE = 3
STAGE_TWO = 4
