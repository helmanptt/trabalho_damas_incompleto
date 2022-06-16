from .constants import *
import pygame

PADDING = 10
BORDER = 2

king = False
x = 0
y = 0

# função criada por Helman para não usar classe
#def piece_chars():

def calc_pos(col):
    x = SQUARE_SIZE * col + SQUARE_SIZE // 2
    y = SQUARE_SIZE * col + SQUARE_SIZE // 2

def make_king():
    king = True

def draw(win, color, x, y):
    radius = SQUARE_SIZE//2 - PADDING
    pygame.draw.circle(win, color, (x, y), radius)
    if king:
        win.blit(CROWN, (x - CROWN.get_width()//2, y - CROWN.get_height()//2))

#def move(row, col):

