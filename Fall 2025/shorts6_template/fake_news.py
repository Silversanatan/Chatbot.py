"""
    File: fake_news.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program reads a CSV file of news article data, processes
        the titles to count the frequency of significant words, and
        identifies the most common words. The word counts are stored
        and manipulated using a linked list data structure.
"""
import csv
import string

class Node:
    """Represents a single element in a linked list for storing word counts.

       This class holds a word, its frequency count, and a reference to the
       next Node in the list. It is constructed with a word string, which
       initializes its count to 1.
    """
    def __init__(self, word):
        """Initializes a Node object with a word and a default count of 1.

           Parameters: word is the string to be stored in the node.
        """
        self._word = word
        self._count = 1
        self._next = None

    def word(self):
        return self._word

    def count(self):
        return self._count

    def next(self):
        return self._next

    def set_next(self, target):
        self._next = target

    def incr(self):
        """Increments the node's internal count by 1."""
        self._count += 1

    def __str__(self):
        return "({}: {})".format(self._word, self._count)

    def __repr__(self):
        return self.__str__()


class LinkedList:
    """Represents a linked list to manage a collection of Node objects.

       This class manages a sequence of word-count nodes. Its primary methods
       allow for updating word counts, sorting the list by count in
       descending order, and retrieving nodes based on their position.
       It is constructed as an empty list.
    """
    def __init__(self):
        """Initializes an empty LinkedList by setting the head to None."""
        self._head = None

    def is_empty(self):
        return self._head is None

    def head(self):
        return self._head

    def update_count(self, word):
        """Updates the count for a word; adds it if it's not in the list.

           Parameters: word is a string whose count needs to be updated. If
               the word exists, its count is incremented. If not, a new
               node for the word is added to the front of the list.
        """
        current = self._head
        while current is not None:
            if current.word() == word:
                current.incr()
                return
            current = current.next()

        # Add a new node to the head if the word was not found.
        new_node = Node(word)
        new_node.set_next(self._head)
        self._head = new_node

    def sort(self):
        """Sorts the linked list in descending order based on node counts.

           This method uses an insertion sort algorithm to rebuild the list
           in sorted order.
           Note: This method is based on the sorting algorithm provided
           in CSc 120 class materials.
        """
        sorted_head = None
        current = self._head
        while current is not None:
            next_node = current.next()
            if sorted_head is None or sorted_head.count() <= current.count():
                current.set_next(sorted_head)
                sorted_head = current
            else:
                # Find the correct position in the new sorted list.
                search_ptr = sorted_head
                while (search_ptr.next() is not None and
                       search_ptr.next().count() > current.count()):
                    search_ptr = search_ptr.next()
                current.set_next(search_ptr.next())
                search_ptr.set_next(current)
            current = next_node
        self._head = sorted_head

    def get_nth_highest_count(self, n):
        """Finds the count of the node at the nth position in the list.

           Parameters: n is the zero-based index of the desired node.

           Returns: An integer representing the count of the node at
               position n. Returns 0 if n is out of bounds.
        """
        if self.is_empty():
            return 0
        current = self._head
        i = 0
        while current is not None and i < n:
            current = current.next()
            i += 1
        if current is not None:
            return current.count()
        else:
            return 0  # Index n was beyond the end of the list.

    def print_upto_count(self, k):
        """Prints all nodes with a count greater than or equal to k.

           Assumes the list has been sorted in descending order by count.
           Parameters: k is the minimum integer count for a node to be
               printed.
        """
        current = self._head
        while current is not None and current.count() >= k:
            print("{} : {:d}".format(current.word(), current.count()))
            current = current.next()

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = []
        current = self._head
        while current is not None:
            result.append(str(current))
            current = current.next()
        return " -> ".join(result)

def process_title(title_string):
    """Cleans a title string to produce a list of standardized words.

       This function replaces all punctuation with spaces, splits the title
       into words, filters out any words with 2 or fewer characters, and
       converts all remaining words to lowercase.

       Parameters: title_string is the raw string of the article title.

       Returns: A list of cleaned and standardized word strings.
    """
    processed_str = ""
    for char in title_string:
        # Replace punctuation with a space to handle cases like "word,word".
        if char in string.punctuation:
            processed_str += " "
        else:
            processed_str += char
    words = processed_str.split()
    cleaned_list = []
    for word in words:
        if len(word) > 2:
            cleaned_list.append(word.lower())
    return cleaned_list

def main():
    """Drives the program for reading and analyzing fake news titles."""
    word_counts = LinkedList()
    filename = input()
    file_obj = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(file_obj)

    for row in reader:
        # A row is valid if it's not empty and not a comment.
        is_valid_row = len(row) > 0
        if is_valid_row:
            first_char = row[0][0]
            if first_char != "#" and first_char != "!":
                title = row[4]
                cleaned_words = process_title(title)
                for word in cleaned_words:
                    word_counts.update_count(word)

    file_obj.close()
    word_counts.sort()
    n_str = input()
    n = int(n_str)
    if n < 0:
        n = 3  # A default value for negative input as per spec.
    k = word_counts.get_nth_highest_count(n)
    word_counts.print_upto_count(k)
main()