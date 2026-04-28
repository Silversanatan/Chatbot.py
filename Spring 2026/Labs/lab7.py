# Lab 7 starter code
# Node class
class Node:
    def __init__(self, value):
        self._value = value
        self._inner_list = LinkedList()
        self._next = None
    
    def value(self):
        return self._value

    def get_inner_list(self):
        return self._inner_list
    
    def next(self):
        return self._next

    def __str__(self): 
       if self._next is None:
           ending = ""
       else:
           ending = " -> "
       if self._inner_list.is_empty():
           return str(self._value) + " [empty llist] " + ending
       else:
           # This calls the __str__ of the inner LinkedList object
           return str(self._value) + " [" + str(self._inner_list) + "] " + ending

        
# Linked list class
class LinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    # add a node to the head of the list (Prepend)
    def add(self, node):
        node._next = self._head
        self._head = node

    def __str__(self):
        string = 'List -> '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        return string


def main():
    # create the outer list
    my_ll = LinkedList()

    # create a node (Step 1/2 logic)
    n = Node(4)
    # add a node to n's inner list
    n.get_inner_list().add(Node(2))
    # add n to the outer list
    my_ll.add(n)
    print(f"After Step 2:\n{my_ll}\n")

    # create another node
    n = Node(8)
    # add a node to n's inner list
    n.get_inner_list().add(Node(3))
    # add n to the outer list
    my_ll.add(n)
    print(f"After adding Node 8:\n{my_ll}\n")

    
    # Step 4 (a): create another node n with value 7
    n = Node(7)
    
    # Step 4 (b): add a node to its inner list with value 5
    n.get_inner_list().add(Node(5))

    # Step 4 (c): add n to the outer list
    my_ll.add(n)

    print(f"Final List (Step 4d):\n{my_ll}")


main()