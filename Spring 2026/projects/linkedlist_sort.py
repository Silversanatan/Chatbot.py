"""
    File: linkedlist_sort.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program reads a series of integers from a file and
        populates a custom LinkedList. It then sorts the nodes in 
        descending order by moving nodes between lists rather than 
        swapping values.
"""

class Node:
    """Represents a single node in a linked list structure."""

    def __init__(self, value):
        """Initializes a node with a numeric value and no successor.

        Parameters: value is the integer to be stored in the node.
        """
        # Store the integer value and initialize the next pointer to null
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        """Returns the numeric value stored in the node."""
        # Simple getter for the internal value attribute
        return self._value
    
    def next(self):
        """Returns the next node in the sequence."""
        # Simple getter for the next node pointer
        return self._next

class LinkedList:
    """A class representing a linked list of Node objects.

    It provides methods for adding, removing, and inserting nodes, 
    as well as a custom sorting algorithm that rearranges node pointers.
    """

    def __init__(self):
        """Initializes an empty linked list with a null head."""
        # Start the list with a None head to indicate it is empty
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        """Sorts the linked list in descending order.

        This method follows a specific insertion sort algorithm where nodes 
        are removed from the original list and inserted into a new list
        one by one based on their value.
        """
        if self._head == None or self._head.next() == None:
            return

        sorted_list_head = None
        
        # Process every node until the original list is empty
        while self._head != None:
            # Extract the front node from the current list
            node_to_move = self.remove()
            
            # If new list is empty or current value belongs at the head
            if sorted_list_head == None or \
                node_to_move.value() >= sorted_list_head.value():
                node_to_move._next = sorted_list_head
                sorted_list_head = node_to_move
            else:
                # Iterate through the sorted list to find the insertion point
                search_node = sorted_list_head
                while search_node.next() != None and \
                    search_node.next().value() > node_to_move.value():
                    search_node = search_node.next()
                
                # Rewire pointers to place the node in the middle or end
                node_to_move._next = search_node._next
                search_node._next = node_to_move
        
        # Point the original list head to the newly constructed sorted list
        self._head = sorted_list_head
    
    # add a node to the head of the list
    def add(self, node):
        """Adds a node to the very beginning of the list."""
        # Set new node's next to the current head
        node._next = self._head
        # Move the head pointer to the new node
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        """Removes the head node and returns it.

        Returns: The Node object previously at the head of the list.
        """
        assert self._head != None
        _node = self._head
        # Move the head to the second node in the list
        self._head = _node._next
        # Detach the removed node from the list completely
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        """Inserts node2 immediately following node1.

        Parameters: 
            node1: The node already in the list to follow.
            node2: The new node to be inserted.
        """
        # Connect the new node to node1's successor
        node2._next = node1._next
        # Redirect node1 to point to the new node
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        # Traverse every node and append its string representation
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

def main():
    file_name = input()
    
    my_file = open(file_name, 'r')
    content = my_file.read()
    my_file.close()
    
    words = content.split()
    
    ll = LinkedList()
    
    index = len(words) - 1
    while index >= 0:
        val = int(words[index])
        new_node = Node(val)
        ll.add(new_node)
        index = index - 1
        
    ll.sort()
    print(ll)

main()