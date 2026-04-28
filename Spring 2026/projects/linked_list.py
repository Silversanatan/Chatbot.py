"""
    File: linked_list.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This file defines the Node and LinkedList classes to be used in 
        building and manipulating linked data structures. It provides the 
        foundational objects for constructing a social network.
"""

class Node:
    """This class represents a node in a singly linked list.

       It stores a data value (such as a person's name), a reference to the 
       next node in the sequence, and a reference to another LinkedList that 
       represents this node's friends. It is constructed with a data value.
    """
    def __init__(self, data):
        """Initializes a Node with the given data and empty references.
      
        Parameters: data is the value to be stored in the node.
      
        Returns: None
        """
        self._val = data
        self._next = None
        self._friends = None

    def get_value(self):
        return self._val

    def set_value(self, data):
        self._val = data

    def get_next(self):
        return self._next

    def set_next(self, target_node):
        self._next = target_node

    def get_friends(self):
        return self._friends

    def set_friends(self, friends_list):
        self._friends = friends_list


class LinkedList:
    """This class represents a singly linked list.

       It contains methods for adding elements alphabetically or unordered, 
       sorting the list, and checking for the presence of specific data. It 
       is constructed as an empty list with a None head pointer.
    """
    def __init__(self):
        """Initializes an empty LinkedList with the head pointing to None.
      
        Parameters: None
      
        Returns: None
        """
        self._head = None

    def get_head(self):
        return self._head

    def add_alpha(self, data):
        """Inserts a new node into the linked list in alphabetical order.
      
        Parameters: data is the value to be added to the list.
      
        Returns: None
        """
        n_node = Node(data)
        front = self.get_head()

        # Insert at the head if the list is empty or data comes first
        if front is None or n_node.get_value() <= front.get_value():
            n_node.set_next(front)
            self._head = n_node
        else:
            curr = front
            # Traverse to find the correct alphabetical insertion point
            while curr.get_next() is not None and \
                  n_node.get_value() > curr.get_next().get_value():
                curr = curr.get_next()
            
            # Insert the new node between curr and curr's next node
            n_node.set_next(curr.get_next())
            curr.set_next(n_node)
    
    def add_unordered(self, data):
        """Adds a new node to the front of the linked list.
      
        Parameters: data is the value to be added to the list.
      
        Returns: None
        """
        n_node = Node(data)
        n_node.set_next(self.get_head())
        self._head = n_node
    
    def sort(self):
        """Sorts the linked list in ascending order using bubble sort.
      
        Parameters: None
      
        Returns: None
        """
        front = self.get_head()
        # An empty or single-element list is already sorted
        if front is None or front.get_next() is None:
            return

        did_swap = True
        while did_swap:
            did_swap = False
            curr = front
            # Traverse and swap adjacent node values if out of order
            while curr.get_next() is not None:
                following = curr.get_next()
                if curr.get_value() > following.get_value():
                    # Swap values without modifying the node pointers
                    backup_val = curr.get_value()
                    curr.set_value(following.get_value())
                    following.set_value(backup_val)
                    did_swap = True
                curr = curr.get_next()

    def contains(self, data):
        """Checks if the linked list contains a node with the specified data.
      
        Parameters: data is the target value being searched for.
      
        Returns: True if the data is found, False otherwise.
        """
        curr = self.get_head()
        while curr is not None:
            if curr.get_value() == data:
                return True
            curr = curr.get_next()
        return False
    
    def is_empty(self):
        """Checks if the linked list has no elements.
      
        Parameters: None
      
        Returns: True if the list is empty, False otherwise.
        """
        return self._head is None