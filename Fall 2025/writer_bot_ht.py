"""
    File: writer_bot_ht.py
    Author: Rajat Tawari
    Course: CSc 120, Fall 2025
    Purpose: This program generates random text based on a source
        file using a Markov chain algorithm stored in a Hash Table.
"""

import sys
from random import randint, seed

# Seed for random number generator
SEED = 8
# Special character for start/end
NONWORD = '@'

class Hashtable:
    """
    Hash Table using linear probing.
    """
    def __init__(self, size):
        self._pairs = [None] * size
        self._size = size

    def _hash(self, key):
        p = 0
        # Iterate over each char in key
        for c in key:
            p = 31 * p + ord(c)
        # Return index modulo table size
        return p % self._size

    def put(self, key, value):
        index = self._hash(key)
        # Loop until empty slot or key found
        while self._pairs[index] is not None:
            # Check if current key matches
            if self._pairs[index][0] == key:
                self._pairs[index][1] = value
                return
            index = (index - 1) % self._size
        # Insert key and value pair
        self._pairs[index] = [key, value]

    def get(self, key):
        index = self._hash(key)
        start_index = index
        # Loop while slot is not empty
        while self._pairs[index] is not None:
            # Return value if key matches
            if self._pairs[index][0] == key:
                return self._pairs[index][1]
            index = (index - 1) % self._size
            # Check if we circled back to start
            if index == start_index:
                return None
        # Return None if key not found
        return None

    def __contains__(self, key):
        found = self.get(key)
        return found is not None

    def __str__(self):
        result = str(self._pairs)
        return result

def read_file_and_build_words(filename, n):
    all_words = []
    # Add n NONWORDs to start of list
    for i in range(n):
        all_words.append(NONWORD)
    file_obj = open(filename, 'r')
    file_contents = file_obj.read()
    file_obj.close()
    words_file = file_contents.split()
    for word in words_file:
        all_words.append(word)
    # Return the complete list of words
    return all_words

def build_markov_model(all_words, n, size):
    ht = Hashtable(size)
    # Iterate through words to build keys
    for i in range(len(all_words) - n):
        prefix_list = all_words[i : i + n]
        prefix_str = ""
        # Build string key from prefix list
        for j in range(len(prefix_list)):
            prefix_str += prefix_list[j]
            # Add space between words
            if j < len(prefix_list) - 1:
                prefix_str += " "
        suffix = all_words[i + n]
        # Check if prefix is new
        if prefix_str not in ht:
            ht.put(prefix_str, [suffix])
        else:
            current_suffixes = ht.get(prefix_str)
            current_suffixes.append(suffix)
    # Return the populated model
    return ht

def generate_text(model, n, num_words):
    seed(SEED)
    output_list = []
    current_prefix_list = []
    for i in range(n):
        # Append nonword to prefix list
        current_prefix_list.append(NONWORD)
    # Loop to generate specified words
    for i in range(num_words):
        current_prefix_str = ""
        # Convert prefix list to string key
        for j in range(len(current_prefix_list)):
            current_prefix_str += current_prefix_list[j]
            # Add space between words
            if j < len(current_prefix_list) - 1:
                current_prefix_str += " "
        # Stop if prefix not in model
        if current_prefix_str not in model:
            break
        suffix_list = model.get(current_prefix_str)
        next_word = ""
        # Check if only one suffix exists
        if len(suffix_list) == 1:
            next_word = suffix_list[0]
        else:
            # Pick random index for suffix
            index = randint(0, len(suffix_list) - 1)
            next_word = suffix_list[index]
        output_list.append(next_word)
        next_prefix_list = []
        # Shift prefix window by one
        for j in range(1, n):
            next_prefix_list.append(current_prefix_list[j])
        next_prefix_list.append(next_word)
        current_prefix_list = next_prefix_list
    return output_list

def print_output(output_list):
    count = 0
    line_str = ""
    # Iterate through generated words
    for word in output_list:
        line_str = line_str + word + " "
        count +=1
        # Check if line length reached 10
        if count == 10:
            print(line_str.strip())
            line_str = ""
            count = 0
    # Check for remaining words
    if count > 0:
        print(line_str.strip())

def main():
    sfile = input()
    size_str = input()
    n_str = input()
    num_words_str = input()
    size = int(size_str)
    n = int(n_str)
    num_words = int(num_words_str)
    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)
    all_words = read_file_and_build_words(sfile, n)
    model = build_markov_model(all_words, n, size)
    output_list = generate_text(model, n, num_words)
    print_output(output_list)
main()