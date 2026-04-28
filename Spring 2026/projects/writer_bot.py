"""
    File: writer_bot.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program reads a text file and builds a Markov chain 
        table based on a prefix of length 'n'. It then uses this table 
        to generate a specified number of words of random text and 
        outputs the result in a formatted grid.
"""

import random

SEED = 8
NONWORD = " "


def read_words(filename):
    """Reads all whitespace-separated words from a file into a list.

    Parameters: filename is a string representing the path to the file.

    Returns: A list of strings containing every word in the file.
    """
    f = open(filename, "r")
    words = []

    for line in f:
        # Split each line into individual words based on whitespace
        parts = line.split()
        for w in parts:
            words.append(w)

    f.close()
    return words


def build_table(words, n):
    """Constructs a dictionary mapping prefixes to lists of suffixes.

    Parameters: 
        words: a list of strings to process.
        n: an integer representing the size of the prefix.

    Returns: A dictionary where keys are n-length tuples and values 
             are lists of words that follow that prefix.
    """
    table = {}

    # Initialize the starting prefix with 'n' empty strings (NONWORD)
    prefix = []
    i = 0
    while i < n:
        prefix.append(NONWORD)
        i = i + 1

    # Convert to tuple because dictionary keys must be immutable
    prefix = tuple(prefix)

    for w in words:
        # Map current prefix to the word that follows it
        if prefix in table:
            table[prefix].append(w)
        else:
            table[prefix] = [w]

        # Slide the window: remove the first word, add the current word
        temp = list(prefix)
        temp.pop(0)
        temp.append(w)
        prefix = tuple(temp)

    return table


def generate_text(table, n, total):
    """Generates a list of random words based on the Markov table.

    Parameters:
        table: the dictionary of prefixes and suffixes.
        n: the length of the prefix.
        total: the total number of words to generate.

    Returns: A list of generated strings.
    """
    result = []

    # Reset prefix to the initial state (all NONWORD) to start generation
    prefix = []
    i = 0
    while i < n:
        prefix.append(NONWORD)
        i = i + 1

    prefix = tuple(prefix)

    count = 0
    while count < total:
        # If the prefix doesn't exist in our table, we can't generate more
        if prefix not in table:
            break

        suffixes = table[prefix]

        # Choose the next word: if multiple options exist, pick one randomly
        if len(suffixes) == 1:
            next_word = suffixes[0]
        else:
            r = random.randint(0, len(suffixes) - 1)
            next_word = suffixes[r]

        result.append(next_word)

        # Shift the prefix window to prepare for the next word generation
        temp = list(prefix)
        temp.pop(0)
        temp.append(next_word)
        prefix = tuple(temp)

        count = count + 1

    return result


def print_output(result):
    """Prints the generated word list in rows of 10 words.

    Parameters: result is a list of strings to be printed.

    Returns: None
    """
    i = 0
    while i < len(result):
        line = []
        j = 0
        # Build a temporary list of 10 words (or fewer if at the end)
        while j < 10 and i < len(result):
            line.append(result[i])
            i = i + 1
            j = j + 1
        # Join words with a space and print the completed line
        print(" ".join(line))


def main():
    random.seed(SEED)

    filename = input()
    n = int(input())
    total = int(input())

    words = read_words(filename)
    table = build_table(words, n)
    result = generate_text(table, n, total)

    print_output(result)
main()