"""
    File: writer_bot_ht.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: Builds a Markov chain using a custom hash table
    to generate random text.
"""

import random
import sys

SEED = 8
NONWORD = "@"

class Hashtable:
    """Custom hash table using linear probing to map prefixes to suffixes."""
    
    def __init__(self, size):
        """Initializes the table.
        Parameters: size is an int for table capacity.
        Returns: None
        """
        # Set max capacity
        self._size = size
        # Init empty pair list
        self._pairs = [None] * size

    def _hash(self, key):
        """Hashes a string using Horner's rule.
        Parameters: key is a string to hash.
        Returns: An int index.
        """
        p = 0
        # Accumulate hash value
        for c in key:
            p = 31 * p + ord(c)
        # Keep index within bounds
        return p % self._size

    def put(self, key, value):
        """Inserts a key-value pair.
        Parameters: key is a string, value is a list of suffixes.
        Returns: None
        """
        idx = self._hash(key)
        # Track starting index
        start = idx
        
        while self._pairs[idx] is not None:
            if self._pairs[idx][0] == key:
                self._pairs[idx][1] = value
                return
            
            # Probe left on collision
            idx = (idx - 1) % self._size
            if idx == start:
                return 
                
        self._pairs[idx] = [key, value]

    def get(self, key):
        """Retrieves a value by key.
        Parameters: key is a string to find.
        Returns: List of suffixes or None.
        """
        idx = self._hash(key)
        # Track starting index
        start = idx
        
        while self._pairs[idx] is not None:
            # Linear probe for match
            if self._pairs[idx][0] == key:
                return self._pairs[idx][1]
            idx = (idx - 1) % self._size
            if idx == start:
                return None
                
        return None

    def __contains__(self, key):
        """Checks if key exists.
        Parameters: key is a string.
        Returns: True if found, False otherwise.
        """
        # Fetch value
        ans = self.get(key)
        
        # Return presence
        if ans is not None:
            return True
        return False

    def __str__(self):
        """Returns string representation."""
        return str(self._pairs)


def read_words(filename):
    """Reads words from a file.
    Parameters: filename is a string.
    Returns: List of strings.
    """
    # Open file for reading
    f = open(filename, "r")
    words = []

    for line in f:
        parts = line.split()
        for w in parts:
            # Extract individual words
            words.append(w)

    f.close()
    return words


def build_table(words, n, m):
    """Maps prefixes to suffixes in a hash table.
    Parameters: words is a list, n is prefix size, m is table size.
    Returns: Populated Hashtable.
    """
    table = Hashtable(m)
    
    # Init prefix list
    pref_list = []
    i = 0
    while i < n:
        pref_list.append(NONWORD)
        i = i + 1

    pref_str = " ".join(pref_list)

    for w in words:
        if pref_str in table:
            val = table.get(pref_str)
            val.append(w)
        else:
            table.put(pref_str, [w])

        # Slide prefix window
        pref_list.pop(0)
        pref_list.append(w)
        pref_str = " ".join(pref_list)

    return table


def generate_text(table, n, total):
    """Generates random text from the table.
    Parameters: table is a Hashtable, n is prefix size, total is word count.
    Returns: List of generated words.
    """
    res = []

    pref_list = []
    i = 0
    while i < n:
        pref_list.append(NONWORD)
        i = i + 1

    pref_str = " ".join(pref_list)

    count = 0
    while count < total:
        if not (pref_str in table):
            break

        sufs = table.get(pref_str)

        # Pick random suffix
        if len(sufs) == 1:
            nxt = sufs[0]
        else:
            r = random.randint(0, len(sufs) - 1)
            nxt = sufs[r]

        res.append(nxt)

        # Update prefix
        pref_list.pop(0)
        pref_list.append(nxt)
        pref_str = " ".join(pref_list)

        count = count + 1

    return res


def print_text(res):
    """Prints words in rows of 10.
    Parameters: res is a list of strings.
    Returns: None
    """
    i = 0
    while i < len(res):
        line = []
        j = 0
        # Chunk into groups of 10
        while j < 10 and i < len(res):
            line.append(res[i])
            i = i + 1
            j = j + 1
        
        # Print formatted line
        print(" ".join(line))


def main():
    random.seed(SEED)

    filename = input()
    m = int(input())
    n = int(input())
    total = int(input())

    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    
    if total < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    words = read_words(filename)
    table = build_table(words, n, m)
    res = generate_text(table, n, total)

    print_text(res)

main()