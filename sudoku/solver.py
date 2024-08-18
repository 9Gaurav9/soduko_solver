# # sudoku/solver.py

# import pygame
# from sudoku.game import draw_grid

# def is_valid_move(grid, num, pos):
#     row, col = pos
#     for i in range(9):
#         if grid[row][i] == num and i != col:
#             return False
#     for i in range(9):
#         if grid[i][col] == num and i != row:
#             return False
#     box_x = col // 3
#     box_y = row // 3
#     for i in range(box_y * 3, box_y * 3 + 3):
#         for j in range(box_x * 3, box_x * 3 + 3):
#             if grid[i][j] == num and (i, j) != pos:
#                 return False
#     return True

# def draw_screen(screen, grid):
#     screen.fill((255, 255, 255))
#     draw_grid(screen, grid)
#     pygame.display.update()

# def solve(screen, grid):
#     for row in range(9):
#         for col in range(9):
#             if grid[row][col] == 0:
#                 for num in range(1, 10):
#                     if is_valid_move(grid, num, (row, col)):
#                         grid[row][col] = num
#                         draw_screen(screen, grid)s
#                         pygame.time.delay(2)  # Delay for visualization
#                         solve(screen, grid)
#                         grid[row][col] = 0
#                 return
#     draw_screen(screen, grid)

''' '''
# sudoku/solver.py

import pygame
from sudoku.game import draw_grid, is_valid_move

def draw_screen(screen, grid):
    screen.fill((255, 255, 255))
    draw_grid(screen, grid)
    pygame.display.update()

def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def solve(screen, grid):
    empty_pos = find_empty(grid)
    if not empty_pos:
        return True  # Solution found
    
    row, col = empty_pos

    for num in range(1, 10):
        if is_valid_move(grid, num, (row, col)):
            grid[row][col] = num
            draw_screen(screen, grid)
            pygame.time.delay(2)  # Shorter delay for faster solving

            if solve(screen, grid):  # Recursively attempt to solve the rest
                return True

            grid[row][col] = 0  # Backtrack

    return False  # Trigger backtracking
