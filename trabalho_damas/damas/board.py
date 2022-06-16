import pygame
from .constants import *

board = []
white_left = black_left = 12
white_kings = black_kings = 0

def draw_squares(win):
    win.fill(DARK_BROWN)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, LIGHT_BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def move(piece, row, col):
    board[piece.row][piece.col], board[row][col] = board[row][col], board[piece.row][piece.col]
    piece.move(row, col)

    if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                white_kings += 1
            else:
                black_kings += 1

def get_piece(row, col):
        return board[row][col]

def create_board():
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            if col % 2 == ((row + 1) % 2):
                if row < 3:
                    board[row].append((row, col, WHITE))
                elif row > 4:
                    board[row].append((row, col, BLACK))
                else:
                    board[row].append(0)
            else:
                board[row].append(0)

def draw_evrt(win):
    draw_squares(win)
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != 0:
                piece.draw(win)