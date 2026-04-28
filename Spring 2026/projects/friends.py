"""
    File: friends.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program reads a file of friend pairs to build a social 
        network using linked lists. It then prompts the user for two names 
        and calculates their common friends by comparing their friend lists.
"""

from linked_list import *


def find_node(my_list, target_name):
    """Searches a linked list for a node with a specific name.
  
    Parameters: 
        my_list is the LinkedList to search through.
        target_name is the string name of the person to find.
  
    Returns: The Node containing the target_name, or None if not found.
    """
    curr = my_list.get_head()
    while curr is not None:
        if curr.get_value() == target_name:
            return curr
        curr = curr.get_next()
    return None


def build_network(file_name):
    """Reads a file to build a linked list of people and their friends.
  
    Assumes the file contains pairs of strings separated by whitespace, 
    representing a bidirectional friendship between two people.

    Parameters: file_name is a string representing the path to the text file.
  
    Returns: A LinkedList containing all individuals and their friend networks.
    """
    infile = open(file_name, 'r')
    name_list = LinkedList()

    for line in infile:
        parts = line.split()
        if len(parts) == 2:
            n1 = parts[0]
            n2 = parts[1]

            # Ensure the first person exists in the network
            node1 = find_node(name_list, n1)
            if node1 is None:
                name_list.add_unordered(n1)
                node1 = name_list.get_head()
                node1.set_friends(LinkedList())

            # Ensure the second person exists in the network
            node2 = find_node(name_list, n2)
            if node2 is None:
                name_list.add_unordered(n2)
                node2 = name_list.get_head()
                node2.set_friends(LinkedList())

            # Establish the bidirectional friendship
            if not node1.get_friends().contains(n2):
                node1.get_friends().add_unordered(n2)
            if not node2.get_friends().contains(n1):
                node2.get_friends().add_unordered(n1)
    
    infile.close()
    return name_list


def get_common_friends(node1, node2):
    """Finds the intersection of friends between two individuals.
  
    Parameters: 
        node1 is the Node representing the first person.
        node2 is the Node representing the second person.
  
    Returns: A sorted LinkedList containing the names of their common friends.
    """
    common_list = LinkedList()
    
    curr1 = node1.get_friends().get_head()
    # Iterate through all of person 1's friends
    while curr1 is not None:
        curr2 = node2.get_friends().get_head()
        # Compare current friend against all of person 2's friends
        while curr2 is not None:
            if curr1.get_value() == curr2.get_value():
                common_list.add_unordered(curr1.get_value())
            curr2 = curr2.get_next()
        curr1 = curr1.get_next()

    common_list.sort()
    return common_list


def print_common_friends(common_list):
    """Prints the names of the common friends from a linked list.
  
    Parameters: common_list is a LinkedList containing common friend names.
  
    Returns: None
    """
    if not common_list.is_empty():
        print("Friends in common:")
        curr = common_list.get_head()
        while curr is not None:
            print(curr.get_value())
            curr = curr.get_next()


def main():
    """Main execution function to handle user input and run the network logic.
  
    Parameters: None
  
    Returns: None
    """
    file_name = input('Input file: ')
    name_list = build_network(file_name)

    p1 = input('Name 1: ').strip()
    p2 = input('Name 2: ').strip()

    person1_node = find_node(name_list, p1)
    if person1_node is None:
        print("ERROR: Unknown person " + p1)
        return

    person2_node = find_node(name_list, p2)
    if person2_node is None:
        print("ERROR: Unknown person " + p2)
        return

    common_list = get_common_friends(person1_node, person2_node)
    print_common_friends(common_list)


main()