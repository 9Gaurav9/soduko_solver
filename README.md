# AI-Powered Sudoku Solver with Visualization Using Pygame

This project implements a Sudoku solver using AI-based backtracking algorithms, providing a real-time visual representation of the solving process. The game is built using Pygame, a popular Python library for creating games.

## Features

- **9x9 Sudoku Grid**: A standard Sudoku grid is generated, with numbers randomly placed at the start.
- **AI Solver**: The backtracking algorithm efficiently solves the Sudoku puzzle.
- **Real-Time Visualization**: Watch as the AI fills in the grid step by step.
- **Customizable Speed**: The delay between each move can be adjusted for faster or slower visualization.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/9Gaurav9/sudoku_solver.git
   cd sudoku_solver
   ```

2. **Install the required dependencies:**

   Make sure you have Python installed, then run:

   ```bash
   pip install pygame
   ```

3. **Run the Sudoku Solver:**

   ```bash
   python main.py
   ```

## How It Works

- **Random Grid Generation**: At the start, a partially filled Sudoku grid is generated with 20 randomly placed numbers.
- **AI Solver**: The solver uses a backtracking algorithm that places numbers in the grid and checks for validity based on Sudoku rules. If it encounters an invalid state, it backtracks and tries another number.
- **Visualization**: Pygame is used to draw the grid and the numbers, with a delay to show the AI's progress as it solves the puzzle.

## Project Structure

- `main.py`: The main entry point of the program.
- `sudoku/game.py`: Contains functions to generate the Sudoku grid, draw it, and validate moves.
- `sudoku/solver.py`: Contains the backtracking algorithm to solve the Sudoku puzzle.

## Customization

- **Adjusting Speed**: You can modify the delay in the `solve` function in `sudoku/solver.py` to speed up or slow down the visualization.
- **Grid Complexity**: Change the number of randomly placed numbers in `generate_random_grid` in `sudoku/game.py` to increase or decrease the initial difficulty.

## Future Enhancements

- **User Interface**: Add an option for users to input their own Sudoku puzzles.
- **Difficulty Levels**: Implement different levels of difficulty by controlling the number of pre-filled cells and the complexity of the generated puzzles.
- **Hint System**: Add a feature that provides hints to the user for solving the puzzle manually.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request to propose changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Pygame**: For providing an easy-to-use framework for creating the game interface.
- **Python**: For being a versatile and powerful programming language.
- **Sudoku Algorithms**: Inspired by various Sudoku solving techniques available in the public domain.


