"""
    File: word_grid.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program generates a grid of random lowercase letters.
        It takes a grid size and a random seed as input, creates the grid,
        and then prints it to the console with specific formatting.
"""
import random

def init():
    """Reads the grid size and a seed value from user input.

    This function reads two lines of input. The first is converted to an
    integer to be used as the grid size. The second is used as a string
    to seed the random number generator, ensuring a reproducible sequence
    of random letters.

    Returns:
        An integer representing the size (width and height) of the grid.
    """
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size

def make_grid(grid_size):
    """Creates a 2D list of randomly generated lowercase letters.

    A grid is constructed as a list of lists. The function iterates to
    create each row and, for each row, iterates to create each column,
    populating the grid with random lowercase letters.

    Parameters:
        grid_size: An integer specifying the width and height of the grid.

    Returns:
        A list of lists, where each inner list represents a row in the
        grid of random characters.
    """
    grid = []
    # The ASCII value for 'a' is 97 and for 'z' is 122.
    # These are used as the range for the random integer generation.
    min_char = ord('a')
    max_char = ord('z')
    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            # Generate a random number and convert it to
            # its character equivalent.
            random_num = random.randint(min_char, max_char)
            letter = chr(random_num)
            row.append(letter)
        grid.append(row)
    return grid

def print_grid(grid):
    """Prints the grid of letters one row per line.

    Each letter in a row is separated by a comma, except for the last
    letter, which is followed by a newline character.

    Parameters:
        grid: A list of lists containing the characters to be printed.
    """
    for row in grid:
        # Iterate through all but the last letter in the row to
        #  print with a comma
        for i in range(len(row) - 1):
            print(row[i], end=',')
        # Print the last letter of the row, followed by a newline.
        print(row[-1])

def main():
    grid_size = init()
    grid = make_grid(grid_size)
    print_grid(grid)
main()