# sudoku/game.py

import pygame
import random

# Initialize Pygame modules
pygame.init()

# Define constants
WIDTH, HEIGHT = 540, 540
ROWS, COLS = 9, 9
CELL_SIZE = WIDTH // COLS
FONT = pygame.font.SysFont('Arial', 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
BLUE = (0, 0, 255)

def draw_grid(screen, grid):
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if grid[row][col] != 0:
                text = FONT.render(str(grid[row][col]), True, BLACK)
                screen.blit(text, (col * CELL_SIZE + 15, row * CELL_SIZE + 5))

def generate_random_grid():
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for _ in range(20):  # Randomly place 20 numbers
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if grid[row][col] == 0 and is_valid_move(grid, num, (row, col)):
            grid[row][col] = num
    return grid

def is_valid_move(grid, num, pos):
    for i in range(COLS):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(ROWS):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True
