"""
    File: writer_bot.py
    Author: Rajat Tawari
    Course: CSc 120, Fall 2025
    Purpose: This program generates random text based on a source
        file using a Markov chain algorithm. It builds a model
        of n-word prefixes and their possible suffixes, then uses
        this model to generate new text of a specified length.
"""

from random import randint, seed

# Seed for the random number generator for reproducible output
SEED = 8

# A special string to represent the start/end of text
NONWORD = " "

def read_file_and_build_words(filename, n):
    """
    Reads the specified file and processes its content into a single
    list of words. The list is prefixed with 'n' NONWORDs to
    bootstrap the prefix model.
    
    Parameters:
        filename (str): The name of the source text file to read.
        n (int): The size of the prefix (number of NONWORDs to add).
    
    Returns:
        list[str]: A list of all words from the file, prefixed by
                   n NONWORDs.
    """
    all_words = []
    # Add n NONWORDs to the beginning of the list
    for i in range(n):
        all_words.append(NONWORD)

    # Open, read, and close the file
    file_obj = open(filename, 'r')
    file_contents = file_obj.read()
    file_obj.close()

    words_from_file = file_contents.split()
    
    # Append the file's words to the NONWORD list
    for word in words_from_file:
        all_words.append(word)

    return all_words

def build_markov_model(all_words, n):
    """
    Builds the Markov chain model from the list of words. The model
    is a dictionary where keys are n-word prefix tuples and
    values are lists of all possible suffixes.
    
    Parameters:
        all_words (list[str]): The complete list of words, including
                               initial NONWORDs.
        n (int): The size of the prefix to use for keys.
    
    Returns:
        dict: The Markov model, mapping (tuple) -> list[str]
    """
    model = {}
    # Iterate through the words, stopping n words before the end
    for i in range(len(all_words) - n):
        # Create the n-word prefix (as a list)
        prefix_list = all_words[i : i + n]
        prefix = tuple(prefix_list)
        suffix = all_words[i + n]

        if prefix not in model:
            # If this is a new prefix, start a new list for its suffixes
            model[prefix] = [suffix]
        else:
            # If prefix exists, append the suffix (maintains multiplicity)
            model[prefix].append(suffix)
    
    return model

def generate_text(model, n, num_words):
    """
    Generates a list of random words based on the Markov model.
    It starts with a prefix of n NONWORDs and generates
    'num_words' of text.
    
    Parameters:
        model (dict): The Markov model from build_markov_model.
        n (int): The prefix size.
        num_words (int): The number of words to generate.
    
    Returns:
        list[str]: A list of the generated words.
    """
    # Seed the generator for consistent random choices
    seed(SEED)
    output_list = []
    
    # Create the initial prefix, which is n NONWORDs
    start_prefix_list = []
    for i in range(n):
        start_prefix_list.append(NONWORD)
    current_prefix = tuple(start_prefix_list)

    # Loop to generate the specified number of words
    for i in range(num_words):
        # Stop if the chain breaks (prefix not in model)
        if current_prefix not in model:
            break
        
        # Get the list of possible suffixes for the current prefix
        suffix_list = model[current_prefix]
        
        next_word = ""
        # Choose the next word
        if len(suffix_list) == 1:
            # If only one choice, pick it (no random call)
            next_word = suffix_list[0]
        else:
            # If multiple choices, pick one randomly by index
            index = randint(0, len(suffix_list) - 1)
            next_word = suffix_list[index]
        
        # Add the chosen word to our output
        output_list.append(next_word)
        
        # Build the next prefix by "shifting"
        next_prefix_list = []
        for j in range(1, n):
            next_prefix_list.append(current_prefix[j])
        next_prefix_list.append(next_word)
        current_prefix = tuple(next_prefix_list)

    return output_list

def print_output(output_list):
    """
    Prints the list of generated words, 10 words per line.
    Any remaining words are printed on a final line.
    
    Parameters:
        output_list (list[str]): The list of words to print.
    """
    count = 0
    line_str = ""
    # Iterate through all generated words
    for word in output_list:
        # Add word and a space to the current line string
        line_str = line_str + word + " "
        count = count + 1
        
        # If we reach 10 words, print the line and reset
        if count == 10:
            print(line_str.strip())
            line_str = ""
            count = 0
    
    # After the loop, print any remaining words
    if count > 0:
        print(line_str.strip())

def main():
    """
    Main function to drive the program. It gets user input,
    then calls helper functions to read the file, build the model,
    generate the text, and print the final output.
    """
    # Get input (no prompts as per specification)
    sfile = input()
    n_str = input()
    num_words_str = input()

    # Convert string inputs to integers
    n = int(n_str)
    num_words = int(num_words_str)

    # Execute the program steps
    all_words = read_file_and_build_words(sfile, n)
    model = build_markov_model(all_words, n)
    output_list = generate_text(model, n, num_words)
    print_output(output_list)

main()