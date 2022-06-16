import pygame
from damas.constants import *
from damas.board import *
from damas.piece import * 
#from minimax.algorithm import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Damas - Projeto Pygame")

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                
        draw_evrt(WIN)
        pygame.display.update()

    pygame.quit()

# A função "main()" só é executada diretamente por esse arquivo
if __name__ == "__main__":
    main()