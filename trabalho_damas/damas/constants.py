import pygame
import os

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
DARK_BROWN = (43, 29, 20)
LIGHT_BROWN = (208, 187, 148)

CROWN = pygame.transform.scale(pygame.image.load('crown-png-free-download-676533.png'), (44, 25))