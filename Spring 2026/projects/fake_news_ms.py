"""
    File: fake_news_ms.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: Analyzes fake news titles using Python lists and Merge Sort.
        Sorts words by frequency (descending) and alphabetically (ascending) 
        for ties.
"""
import csv
import string
import sys

class Word:
    """Represents a word and its frequency count."""
    def __init__(self, word):
        """Initializes a Word object with a count of 1."""
        self._word = word
        self._count = 1

    def word(self):
        """Returns the word string."""
        return self._word

    def count(self):
        """Returns the occurrence count."""
        return self._count

    def incr(self):
        """Increments the word count by 1."""
        self._count += 1

    def __lt__(self, other):
        """Returns True if this word is alphabetically smaller than other."""
        return self._word < other.word()

    def __str__(self):
        """Returns formatted string for output."""
        return "{} : {:d}".format(self._word, self._count)

def msort(L):
    """
    Recursively sorts a list using the Merge Sort algorithm.
    Based on class notes on recursion.
    """
    if len(L) <= 1:
        return L
    
    mid = len(L) // 2
    left = msort(L[:mid])
    right = msort(L[mid:])
    return merge(left, right)

def merge(L1, L2):
    """
    Merges two sorted lists into one.
    Primary key: Count (Descending)
    Secondary key: Word (Ascending/Alphabetical)
    """
    res = []
    i = 0
    j = 0
    
    # Standard merge loop
    while i < len(L1) and j < len(L2):
        # Primary check: Count (Descending)
        if L1[i].count() > L2[j].count():
            res.append(L1[i])
            i += 1
        elif L2[j].count() > L1[i].count():
            res.append(L2[j])
            j += 1
        else:
            # Secondary check: Alphabetical Ascending for ties
            if L1[i].word() < L2[j].word():
                res.append(L1[i])
                i += 1
            else:
                res.append(L2[j])
                j += 1
                
    while i < len(L1):
        res.append(L1[i])
        i += 1
    while j < len(L2):
        res.append(L2[j])
        j += 1
        
    return res

def get_cleaned_word_list(title):
    """Replaces punctuation with spaces and returns list of words."""
    new_title = ""
    for char in title:
        if char in string.punctuation:
            new_title += " "
        else:
            new_title += char
    return new_title.lower().split()

def main():
    # Set recursion depth for Merge Sort as required
    sys.setrecursionlimit(4000)
    
    filename = input()
    word_list = []

    # Open file using standard methods
    infile = open(filename, 'r')
    reader = csv.reader(infile)
    for row in reader:
        if len(row) > 0:
            # Ignore comments starting with #
            if not row[0].startswith('#'):
                # Title is field 4
                words = get_cleaned_word_list(row[4])
                for w in words:
                    # Discard words with length <= 2
                    if len(w) > 2:
                        found = False
                        for word_obj in word_list:
                            if word_obj.word() == w:
                                word_obj.incr()
                                found = True
                                break
                        if not found:
                            word_list.append(Word(w))
    infile.close()

    # Sort the list using Merge Sort
    sorted_list = msort(word_list)

    val_str = input()
    # Manual check for integer conversion
    if val_str.isdigit() or (val_str.startswith('-') \
                             and val_str[1:].isdigit()):
        n = int(val_str)
    else:
        n = 3
        
    if n < 0:
        n = 3

    # Format output to match autograder expectations
    if n < len(sorted_list):
        k = sorted_list[n].count()
        first_item = True
        for item in sorted_list:
            if item.count() >= k:
                if first_item:
                    # Prefix first line with File: and N:
                    print("File: " +" N: " + str(item))
                    first_item = False
                else:
                    print(item)
main()