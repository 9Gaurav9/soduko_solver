from setuptools import setup, find_packages

setup(
    name="sudoku_solver",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    entry_points={
        "console_scripts": [
            "sudoku_solver=main:main",
        ],
    },
    author="Gaurav Upadhyay",
    description="A 9x9 Sudoku game with AI solving and visualization using Pygame.",
    url="https://github.com/yourusername/sudoku_solver",
)
