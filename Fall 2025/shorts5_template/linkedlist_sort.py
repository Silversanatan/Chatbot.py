"""
    File: linkedlist_sort.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program reads a line of integers from a file,
        creates a singly linked list from those numbers, sorts the
        list in descending order by moving the nodes, and then
        prints the final sorted list to the console.
"""
class LinkedList:
    """This class represents a singly linked list of Node objects.

       The class provides the primary methods for manipulating the list,
       including adding, removing, inserting, and sorting nodes. The sort
       method is a key feature, which rearranges nodes into descending
       order based on their value. The list is constructed as an empty
       list, and nodes are typically added to the head.
    """
    def __init__(self):
        """Initializes an empty LinkedList object.

           The head of the list is set to None, indicating that the
           list contains no nodes upon creation.
        """
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        """Sorts the list's nodes in descending order of their values.

           This method implements an insertion sort algorithm specifically
           for a linked list. It iterates through the original list,
           moving each node one by one into a new, separate list that is
           kept sorted. After all nodes have been moved, the head of the
           original list is updated to point to the head of the new sorted
           list. The nodes themselves are moved, not just their values.

           Parameters: None. This method modifies the list in place.
           Returns: None.
        """
        sorted_head = None
        # 'current' will traverse the original, unsorted list
        current = self._head

        while current is not None:
            # Store the next node to visit before we change current's pointers
            next_to_visit = current.next()

            # Case 1: Sorted list is empty or 'current' is the new max value.
            if sorted_head is None or sorted_head.value() <= current.value():
                current._next = sorted_head
                sorted_head = current
            else:
                # Case 2:Traverse the sorted list to find the insertion point.
                sorted_current = sorted_head
                while (sorted_current.next() is not None and
                       sorted_current.next().value() > current.value()):
                    sorted_current = sorted_current.next()
                
                # Insert 'current' after 'sorted_current'
                current._next = sorted_current.next()
                sorted_current._next = current

            # Move to the next node in the original list
            current = next_to_visit
        
        # The original list is now dismantled.
        self._head = sorted_head
    
    
    # add a node to the head of the list
    def add(self, node):
        """Adds a node to the head of the list.

           Parameters:
               node: A Node object to be added to the list.
           Returns: None.
        """
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        """Removes a node from the head of the list and returns it.

           Assumptions: The list is not empty when this method is called.

           Parameters: None.
           Returns: The Node object that was removed from the head.
        """
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        """Inserts node2 immediately after node1 in the list.

           Assumptions: node1 is a valid node that exists within the list.

           Parameters:
               node1: The Node object after which node2 will be inserted.
               node2: The Node object to be inserted.
           Returns: None.
        """
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    """This class represents a single node in a singly linked list.

       Each node contains a numeric value and a reference (pointer) to the
       next node in the sequence. It is constructed with a given value.
    """
    def __init__(self, value):
        """Initializes a Node object with a given value.

           The node's `_next` pointer is initialized to None, indicating
           it does not yet point to another node.

           Parameters:
               value: The value to be stored in this node.
        """
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next

def main():
    filename = input()
    data_file = open(filename, 'r')
    line = data_file.read().strip()
    data_file.close()

    values = line.split()

    ll = LinkedList()
    for val_str in values:
        if val_str:
            node = Node(int(val_str))
            ll.add(node)
    ll.sort()
    print(ll)
main()