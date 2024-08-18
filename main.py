# main.py

import pygame
from sudoku.game import generate_random_grid, draw_grid
from sudoku.solver import solve

def main():
    # Initialize Pygame
    pygame.init()

    screen = pygame.display.set_mode((540, 540))
    pygame.display.set_caption("Sudoku Solver")

    grid = generate_random_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        solve(screen, grid)
        pygame.time.delay(5000)  # Wait 5 seconds before closing the window
        running = False

    pygame.quit()

if __name__ == "__main__":
    main()
