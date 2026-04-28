"""
    File: word_search.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program performs a word search on a grid of letters. 
        It reads a list of valid words and a letter grid from user-specified 
        files, then searches the grid horizontally, vertically, and 
        diagonally for matches. Found words are printed in alphabetical order.
"""

def get_word_list():
    """Reads a list of words from a file provided by the user.

    Returns: A list of strings, where each string is a lowercase word 
        from the file.
    """
    list_filename = input()
    word_list = []
    file = open(list_filename, 'r')
    for line in file:
        word_list.append(line.strip().lower())
    file.close()
    return word_list

def read_letters_files():
    """Reads a grid of letters from a file provided by the user.

    Returns: A 2D list (list of lists) representing the grid of letters.
    """
    grid_fname = input()
    grid = []
    file = open(grid_fname, 'r')
    for line in file:
        row = line.strip().split()
        if len(row) > 0:
            grid.append(row)
    file.close()
    return grid

def line_search(line, word_list, found_words):
    """Searches a single sequence of letters for words in the word list.

    Parameters:
        line: A list of characters representing a row, column, or diagonal.
        word_list: A list of valid words to search for.
        found_words: A list of words already identified in the grid.

    Note: Updates the found_words list in-place if a match is found.
    """
    for start in range(len(line)):
        for end in range(start + 3, len(line) + 1):
            substring = "".join(line[start:end]).lower()
            if substring in word_list and substring not in found_words:
                found_words.append(substring)

def find_words(grid, word_list):
    """Orchestrates the search across rows, columns, and diagonals.

    Parameters:
        grid: The 2D list of letters to be searched.
        word_list: The list of valid words to look for.

    Returns: A list of all unique words found within the grid.
    """
    found_words = []
    if not grid:
        return found_words

    grid_size = len(grid)
    # Horizontal and Reverse Horizontal search
    for row in grid:
        line_search(row, word_list, found_words)
        line_search(row[::-1], word_list, found_words)
        
    # Vertical and Reverse Vertical search
    for col_index in range(grid_size):
        column = []
        for row_index in range(grid_size):
            column.append(grid[row_index][col_index])
        line_search(column, word_list, found_words)
        line_search(column[::-1], word_list, found_words)
        
    # Diagonal search (top-left to bottom-right, upper triangle)
    for start_col in range(grid_size):
        diagonal = []
        row, col = 0, start_col
        while row < grid_size and col < grid_size:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        line_search(diagonal, word_list, found_words)
        
    # Diagonal search (top-left to bottom-right, lower triangle)
    for start_row in range(1, grid_size):
        diagonal = []
        row, col = start_row, 0
        while row < grid_size and col < grid_size:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        line_search(diagonal, word_list, found_words)
    return found_words

def print_words(words):
    """Sorts and prints the list of found words.

    Parameters: words is a list of strings found during the search.
    """
    words.sort()
    for word in words:
        print(word)

def main():
    """Main execution function to handle file input, processing, and output."""
    word_list = get_word_list()
    letters_grid = read_letters_files()
    if not letters_grid:
        return
    all_words_found = find_words(letters_grid, word_list)
    print_words(all_words_found)

main()