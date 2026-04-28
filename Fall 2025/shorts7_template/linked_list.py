"""
    File: linked_list.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This module defines a singly linked list structure used to store
        and manage data elements. It includes the Node and LinkedList classes.
        The LinkedList class supports inserting elements, sorting,
        checking membership, and verifying if the list is empty.
"""

class Node:
    """Represents a single node in a singly linked list.

       Each node stores a value and a reference to the next node.
       Nodes are used internally by the LinkedList class.
    """
    def __init__(self, val):
        """Initialize a node with a value and a next pointer set to None.

        Parameters:
            val - the value to be stored in this node
        """
        self._val = val
        self._next = None

    def get_value(self):
        """Return the value stored in the node."""
        return self._val

    def set_value(self, val):
        """Set the value stored in the node."""
        self._val = val

    def get_next(self):
        """Return the reference to the next node."""
        return self._next

    def set_next(self, node):
        """Set the reference to the next node."""
        self._next = node


class LinkedList:
    """Represents a singly linked list data structure.

       The list supports alphabetical insertion, unordered insertion,
       sorting, searching for elements, and checking whether the list is empty.
    """
    def __init__(self):
        """Initialize an empty linked list with no head node."""
        self._head = None

    def get_head(self):
        """Return the head node of the list."""
        return self._head

    def add_alpha(self, val):
        """Insert a new value into the list in alphabetical order.

        Parameters:
            val - the value to be inserted into the list

        Returns: None
        """
        new_node = Node(val)
        head = self.get_head()

        # If list is empty or new value comes before current head
        if head is None or new_node.get_value() <= head.get_value():
            new_node.set_next(head)
            self._head = new_node
        else:
            current = head
            # Traverse until correct position is found
            while current.get_next() is not None and \
                  new_node.get_value() > current.get_next().get_value():
                current = current.get_next()
            
            # Insert new node in the proper place
            new_node.set_next(current.get_next())
            current.set_next(new_node)
    
    def add_unordered(self, val):
        """Insert a new value at the beginning of the list.

        Parameters:
            val - the value to be inserted into the list

        Returns: None
        """
        new_node = Node(val)
        new_node.set_next(self.get_head())
        self._head = new_node
    
    def sort(self):
        """Sort the elements of the linked list in ascending order.
           (Implemented using Bubble Sort for Linked List)
        """
        head = self.get_head()
        if head is None or head.get_next() is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = head
            while current.get_next() is not None:
                next_node = current.get_next()
                if current.get_value() > next_node.get_value():
                    # Swap values
                    temp = current.get_value()
                    current.set_value(next_node.get_value())
                    next_node.set_value(temp)
                    swapped = True
                current = current.get_next()

    def contains(self, val):
        """Check whether the list contains the given value.

        Parameters:
            val - the value to search for

        Returns:
            True if the value is found; False otherwise
        """
        current = self.get_head()
        while current is not None:
            if current.get_value() == val:
                return True
            current = current.get_next()
        return False
    
    def is_empty(self):
        """Determine if the list is empty.

        Returns:
            True if there are no nodes in the list; False otherwise
        """
        return self._head is None