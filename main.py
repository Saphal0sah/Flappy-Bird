import random # for generating Random numbers
import sys # sys.exit to exit the program
import pygame
from pygame.locals import *# basic pygame imports

#Global Variable for the game

FPS = 32
SCREENWIDTH = 289
SCREENHEIGNT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGNT))
GROUNDY = SCREENHEIGNT * 0.8
GAME_SPRITES ={}
GAME_SOUNDS = {}
PLAYER = 'Gallery/images/bird.png'
BACKGROUND ='Gallery/images/background.png'
PIPE = 'Gallery/images/pipe.png'


if __name__ == '__main__':
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by saphal')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Gallery/images/0.png').convert_alpha(),
        pygame.image.load('Gallery/images/1.png').convert_alpha(),
        pygame.image.load('Gallery/images/2.png').convert_alpha(),
        pygame.image.load('Gallery/images/3.png').convert_alpha(),
        pygame.image.load('Gallery/images/4.png').convert_alpha(),
        pygame.image.load('Gallery/images/5.png').convert_alpha(),
        pygame.image.load('Gallery/images/6.png').convert_alpha(),
        pygame.image.load('Gallery/images/7.png').convert_alpha(),
        pygame.image.load('Gallery/images/8.png').convert_alpha(),
        pygame.image.load('Gallery/images/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] =pygame.image.load('Gallery/images/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('Gallery/images/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
    )

    #Game Sounds

    GAME_SOUNDS['die'] = pygame.mixer.Sound('Gallery/sounds/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Gallery/sounds/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Gallery/sounds/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Gallery/sounds/swoosh.wav')
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Gallery/sounds/wing.wav')



GAME_SPRITES['background'] =pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player'] =pygame.image.load(PLAYER).convert_alpha()


while True:
    welcomeScreen()
    mainGame()




