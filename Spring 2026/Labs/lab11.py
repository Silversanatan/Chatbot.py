'''
Lab 11 Starter Code
___________________

'''

'''
Node and Linked classes for Problem 4 - hashing
'''
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + " ->  "
    
    def value(self):
        return self._value
    
    def set_value(self, value):
        self._value = value

    def set_next(self, node):
        self._next = node
    
    def next(self):
        return self._next

    def str(self):
        return str(self._value) + " ->  "
        
class LinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def get_head(self):
        return self._head

    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node

    def __str__(self):
        string = 'LL -> '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        #string += ']'
        return string

'''
Hashtable class for Problem 4

'''
class Hashtable:
    def __init__(self, capacity):
        self._pairs = [None] * capacity 
        self._size = capacity

    def _hash(self, key):
        return key % 7


    def put(self, key):
        index = self._hash(key)

        if self._pairs[index] is None:
            self._pairs[index] = LinkedList()

        new_node = Node(key)

        self._pairs[index].add(new_node)
        
        print(f"Key {key} hashed to index {index}.")
        print("The linked list for this slot is:", self._pairs[index])

def main():

    ht = Hashtable(7)
    ht.put(8)
    ht.put(24)
    ht.put(19)
    ht.put(17)
    ht.put(26)

main()