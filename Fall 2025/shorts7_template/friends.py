"""
    File: friends.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program reads a file containing pairs of names representing
        friendships. It builds a network of Person objects, each maintaining
        their own LinkedList of friends. The program then asks for two names
        and prints their mutual friends, if any.
"""

from linked_list import *


class Person:
    """Represents a person and their list of friends.

       Each Person object has a name and a LinkedList containing
       the names of all their friends.
    """
    def __init__(self, name):
        """Initialize a person with a given name and an empty friend list.

        Parameters:
            name - a string representing the person's name
        """
        self._name = name
        self._friends = LinkedList()

    def get_name(self):
        """Return the person's name."""
        return self._name

    def get_friends(self):
        """Return the LinkedList of the person's friends."""
        return self._friends

    def add_friend(self, friend_name):
        """Add a friend to this person's friend list."""
        self._friends.add_unordered(friend_name)


def find_person(main_list, name):
    """Locate a Person object by name within the given linked list.

    Parameters:
        main_list - a LinkedList containing Person objects
        name - the name of the person to search for

    Returns:
        The Person object if found; otherwise, None.
    """
    current = main_list.get_head()
    # Loop through each node in the list
    while current is not None:
        person_obj = current.get_value()
        # Check if the person’s name matches the target
        if person_obj.get_name() == name:
            return person_obj
        current = current.get_next()
    return None


def process_friendship(people_list, name_a, name_b):
    """Ensure both people exist and are friends with each other.

    Parameters:
        people_list - LinkedList of Person objects
        name_a, name_b - names of two friends in the input file
    """
    # Find or create person A
    person_a = find_person(people_list, name_a)
    if person_a is None:
        person_a = Person(name_a)
        people_list.add_unordered(person_a)

    # Find or create person B
    person_b = find_person(people_list, name_b)
    if person_b is None:
        person_b = Person(name_b)
        people_list.add_unordered(person_b)

    # Add both friends if not already present

    friends_a = person_a.get_friends()
    friends_b = person_b.get_friends()

    if not friends_a.contains(name_b):
        person_a.add_friend(name_b)
    
    if not friends_b.contains(name_a):
        person_b.add_friend(name_a)


def build_network(filename):
    """Build the network of people and friendships from the input file.

    Parameters:
        filename - name of the file containing friendship pairs

    Returns:
        A LinkedList of Person objects representing the network.
    """
    people_list = LinkedList()
    try:
        file_handle = open(filename, 'r')
        # Read file line-by-line and process friendships
        line = file_handle.readline()
        while line != '':
            names = line.strip().split()
            # Ensure each line has exactly two names
            if len(names) == 2:
                name_a, name_b = names
                process_friendship(people_list, name_a, name_b)
            line = file_handle.readline()
        file_handle.close()
    except FileNotFoundError:
        print("Error: File not found.")
        
    return people_list


def get_mutual_friends(person1, person2):
    """Compute and return the mutual friends between two people.

    Parameters:
        person1, person2 - Person objects whose mutual friends are needed

    Returns:
        A LinkedList containing the names of mutual friends.
    """
    mutual_friends = LinkedList()
    
    # Access friends list via getters
    friends1 = person1.get_friends()
    friends2 = person2.get_friends()
    
    friend_node = friends1.get_head()

    # Loop through all of person1’s friends
    while friend_node is not None:
        friend_name = friend_node.get_value()
        # Check if this friend is also in person2’s list
        if friends2.contains(friend_name):
            mutual_friends.add_alpha(friend_name)
        friend_node = friend_node.get_next()

    return mutual_friends


def print_mutual_friends(mutual_friends):
    """Print all mutual friends in alphabetical order.

    Parameters:
        mutual_friends - a LinkedList of mutual friend names
    """
    if not mutual_friends.is_empty():  # Only print if mutual friends exist
        print("Friends in common:")
        current = mutual_friends.get_head()
        # Traverse through each mutual friend
        while current is not None:
            print(current.get_value())
            current = current.get_next()


def main():
    filename = input('Input file: ')
    people_list = build_network(filename)

    # Prompt for two names
    name1 = input('Name 1: ').strip()
    name2 = input('Name 2: ').strip()

    # Check if both people exist in the network
    person1 = find_person(people_list, name1)
    if person1 is None:
        print("ERROR: Unknown person " + name1)
        return

    person2 = find_person(people_list, name2)
    if person2 is None:
        print("ERROR: Unknown person " + name2)
        return

    # Find and print mutual friends
    mutual_friends = get_mutual_friends(person1, person2)
    print_mutual_friends(mutual_friends)


main()