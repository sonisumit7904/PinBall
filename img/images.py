import pygame, constants
import os,sys

menu_path = os.path.join(sys.path[0], "img/menu.png")
playButton_path = os.path.join(sys.path[0], "img/playbutton.png")
gameOver_path = os.path.join(sys.path[0], "img/GAMEOVER.png")
brick_path = os.path.join(sys.path[0], "img/redthingy.png")
burst_path = os.path.join(sys.path[0], "img/blueburst.png")
bumper_path = os.path.join(sys.path[0], "img/orangeface.png")
button_path = os.path.join(sys.path[0], "img/button.png")
plunger_path = os.path.join(sys.path[0], "img/startbouncything.png")
# ball = pygame.transform.scale(pygame.image.load("img/ball.png"),(40,40))
menu = pygame.transform.scale(pygame.image.load(menu_path),(constants.gameW,constants.gameH))
playButton = pygame.transform.scale(pygame.image.load(playButton_path),(int(0.3*703),int(0.3*212)))
gameOver = pygame.transform.scale(pygame.image.load(gameOver_path),(constants.gameW,constants.gameH))

brick = pygame.transform.scale(pygame.image.load(brick_path),(int(0.3*318),int(0.3*121)))
burst = pygame.transform.scale(pygame.image.load(burst_path),(int(0.3*338),int(0.3*338)))
bumper = pygame.transform.scale(pygame.image.load(bumper_path),(int(0.3*128),int(0.3*128)))
button = pygame.transform.scale(pygame.image.load(button_path),(int(0.3*254),int(0.3*300)))
plunger = pygame.transform.scale(pygame.image.load(plunger_path),(20,60))
