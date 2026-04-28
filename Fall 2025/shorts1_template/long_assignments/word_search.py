"""
    File: word_search.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program finds legal words in a grid of letters. It reads
        a list of valid words and a letter grid from two separate files.
        It then searches for words horizontally, vertically, and diagonally
        (top-left to bottom-right), and prints the found words in
        alphabetical order.
"""

def get_word_list():
    """Reads a list of words from a file specified by user input.

    The function reads a filename, opens that file, and reads each line
    into a list of words. The words are converted to lowercase to ensure
    case-insensitive matching later on.

    Returns:
        A list of strings, where each string is a word from the file.
    note:
        This function does not handle file-not-found errors and the program
        will stop if the specified file does not exist.
    """
    word_list_filename = input()
    word_list = []
    file = open(word_list_filename, 'r')
    for line in file:
        word_list.append(line.strip().lower())
    file.close()
    return word_list

def read_letters_grid():
    """Reads a grid of letters from a file specified by user input.

    The user provides a filename for a grid of letters. The function reads
    this file, where each line represents a row of the grid. Letters on
    each line are expected to be separated by whitespace.

    Returns:
        A list of lists, representing the 2D grid of letters.
    note:
        This function does not handle file-not-found errors and the program
        will stop if the specified file does not exist.
    """
    grid_filename = input()
    grid = []
    file = open(grid_filename, 'r')
    for line in file:
        # Split the line by whitespace to create the row of letters.
        row = line.strip().split()
        if len(row) > 0:  # Ensure the row is not empty before appending
            grid.append(row)
    file.close()
    return grid

def find_words(grid, word_list):
    """Searches the grid for legal words in all specified directions.

    This function orchestrates the search for words horizontally (both
    directions), vertically (both directions), and diagonally (top-left
    to bottom-right). It compiles a list of all unique legal words found.

    Parameters:
        grid: A list of lists representing the letter grid.
        word_list: A list of valid words to search for.

    Returns:
        A list of all unique legal words found in the grid.
    """
    found_words = []
    if not grid:
        return found_words

    grid_size = len(grid)
    # Horizontal Search (Left-to-Right and Right-to-Left)
    for row in grid:
        search_line(row, word_list, found_words)
        search_line(row[::-1], word_list, found_words)
    # Vertical Search (Top-to-Bottom and Bottom-to-Top)
    for col_index in range(grid_size):
        column = []
        for row_index in range(grid_size):
            column.append(grid[row_index][col_index])
        search_line(column, word_list, found_words)
        search_line(column[::-1], word_list, found_words)
    # Diagonal Search (Top-Left to Bottom-Right)
    # Diagonals starting from the top row
    for start_col in range(grid_size):
        diagonal = []
        row, col = 0, start_col
        while row < grid_size and col < grid_size:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        search_line(diagonal, word_list, found_words)
    # Diagonals starting from the first column (excluding top-left corner)
    for start_row in range(1, grid_size):
        diagonal = []
        row, col = start_row, 0
        while row < grid_size and col < grid_size:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        search_line(diagonal, word_list, found_words)
    return found_words

def search_line(line, word_list, found_words):
    """Searches a single list of characters for legal words.

    This helper function iterates through a given line (a list of characters)
    to find all possible substrings of length 3 or more. It checks if these
    substrings are in the word_list and adds them to the found_words list
    if they are not already present.

    Parameters:
        line: A list of characters to search through.
        word_list: A list of valid words.
        found_words: A list to accumulate the unique words that are found.
    """
    for start in range(len(line)):
        # A legal word must be at least 3 letters long.
        for end in range(start + 3, len(line) + 1):
            substring = "".join(line[start:end]).lower()
            if substring in word_list and substring not in found_words:
                found_words.append(substring)

def print_words(words):
    """Sorts and prints a list of words, one per line.

    The function first sorts the list of words alphabetically and then
    prints each word on a new line.

    Parameters:
        words: A list of strings to be printed.
    """
    words.sort()
    for word in words:
        print(word)

def main():
    word_list = get_word_list()
    letters_grid = read_letters_grid()
    if not letters_grid:
        return
    all_words_found = find_words(letters_grid, word_list)
    print_words(all_words_found)
main()