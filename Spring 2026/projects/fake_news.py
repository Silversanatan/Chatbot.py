"""
    File: fake_news.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program reads a CSV file containing titles, cleans the text 
        by removing punctuation, and counts the frequency of words with more 
        than two characters using a custom LinkedList.
"""
import csv
import string

class Node:
    """
    This class represents a single node in a linked list.
    It stores a word and its frequency count.
    """
    def __init__(self, word):
        """
        Initializes a Node with a word and sets its count to 1.
        
        Parameters: word is a string.
        """
        # Store the word and initialize frequency count to one
        self._word = word
        self._count = 1
        # Pointer to the next node in the linked list
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
        self._count += 1

    def __str__(self):
        return "{} : {}".format(self._word, self._count)

class LinkedList:
    """
    This class represents a singly linked list of Node objects.
    It provides methods to update counts, remove from head, and sort.
    """
    def __init__(self):
        """Initializes the list with an empty head."""
        # Initialize the head of the list to None
        self._head = None

    def is_empty(self):
        return self._head is None

    def head(self):
        return self._head

    def update_count(self, word):
        """
        Increments the count of a word if it exists, or adds a new Node.
        
        Parameters: word is a string.
        """
        # Start searching for the word from the head of the list
        current = self._head
        while current is not None:
            # If word is found, increment its count and exit function
            if current.word() == word:
                current.incr()
                return
            current = current.next()
        
        # If word is not found, create a new node and add to the front
        new_node = Node(word)
        new_node.set_next(self._head)
        self._head = new_node

    def rm_from_hd(self):
        """
        Removes and returns the node at the head of the list.
        
        Returns: The removed Node object.
        """
        # Check if the list is empty before attempting removal
        if self.is_empty():
            return None
        # Disconnect the head node and update the head pointer
        head_node = self._head
        self._head = self._head.next()
        head_node.set_next(None)
        return head_node
    
    def insert_after(self, node1, node2):
        """
        Inserts node2 into the list after node1.
        
        Parameters: node1 is the reference node, node2 is the new node.
        """
        # Connect node2 to the rest of the list following node1
        node2.set_next(node1.next())
        # Link node1 directly to node2
        node1.set_next(node2)

    def sort(self):
        """
        Sorts the linked list in descending order by count using
        insertion sort.
        """
        # Do nothing if the list has fewer than two elements
        if self._head is None or self._head.next() is None:
            return

        # Create a temporary list to hold sorted nodes
        sorted_ll = LinkedList()
            
        while not self.is_empty():
            # Extract a node from the current list to place in sorted list
            node_to_insert = self.rm_from_hd()
            current = sorted_ll.head()
            prev= None
                
            # Traverse sorted list to find the correct insertion point
            while current is not None and current.count() \
                >= node_to_insert.count():
                prev =current
                current = current.next()
                
            # Insert at the head or after the identified previous node
            if prev is None:
                node_to_insert.set_next(sorted_ll.head())
                sorted_ll._head =node_to_insert
            else:
                sorted_ll.insert_after(prev, node_to_insert)
            
        # Point the original head to the newly sorted structure
        self._head= sorted_ll.head()
    
    def get_nth_highest_count(self, n):
        """
        Returns the count value of the node at index n.
        
        Parameters: n is an integer index.
        Returns: An integer count.
        """
        # Start traversal from the head node
        current =self._head
        index=0
        while current is not None:
            # Return count once the target index n is reached
            if index == n:
                return current.count()
            current =current.next()
            index+=1
        # Return zero if the index is beyond list length
        return 0
    
    def print_upto_count(self, n):
        """
        Prints all nodes that have a count greater than or equal to n.
        
        Parameters: n is the threshold count.
        """
        # Iterate through every node in the list
        current = self._head
        while current is not None:
            # Print node string representation if count meets threshold
            if current.count()>=n:
                print(current)
            current = current.next()

    def __len__(self):
        # Initialize counter to track number of nodes
        count=0
        current =self._head
        while current is not None:
            # Increment counter for every node found
            count+=1
            current =current.next()
        return count

    def __str__(self):
        # Initialize an empty string to accumulate results
        res= ""
        current =self._head
        while current is not None:
            # Append each node's string and a newline to the result
            res += str(current) + "\n"
            current= current.next()
        return res

def get_cleaned_word_list(title):
    """
    Replaces punctuation with spaces and returns a list of words.
    
    Parameters: title is a string.
    Returns: A list of strings.
    """
    # Create an empty string to build the cleaned version
    new_title = ""
    for char in title:
        # Swap punctuation for whitespace to separate words
        if char in string.punctuation:
            new_title += " "
        else:
            new_title += char
    # Split the cleaned string into a list of words
    return new_title.split()

def main():
    filename = input()
    my_list = LinkedList()

    # Open the file and parse contents using the csv module
    infile = open(filename, 'r')
    reader = csv.reader(infile)
    for row in reader:
        if len(row) > 0:
            # Skip rows marked as comments with a hash symbol
            if not row[0].startswith('#'):
                title_text = row[4]
                words = get_cleaned_word_list(title_text)
                for w in words:
                    clean_w = w.lower()
                    # Process words that are longer than two characters
                    if len(clean_w) > 2:
                        my_list.update_count(clean_w)
    infile.close()
    # Organize the collected words by frequency
    my_list.sort()

    # Determine threshold n from user input or default to three
    val = input()
    if val.isdigit():
        n = int(val)
    else:
        n = 3
    # Ensure n is non-negative before proceeding
    if n < 0:
        n = 3
    # Calculate count threshold and print matching nodes
    k = my_list.get_nth_highest_count(n)
    my_list.print_upto_count(k)
main()