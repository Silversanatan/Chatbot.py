class LinkedList:
    def __init__(self):
        self._head = None

    def add(self,new):
        new._next = self._head
        self._head = new
        
    def print_elements(self):
        current = self._head
        while current != None:
            print(str(current._value))
            current = current._next

    # ICA-14 prob 3: Define incr(self) to increment each element by 1
    def incr(self):
        current = self._head
        while current != None:
            current._value += 1
            current = current._next

    # ICA-14 prob 4: Define replace(self, val1, val2)
    def replace(self, val1, val2):
        current = self._head
        while current != None:
            if current._value == val1:
                current._value = val2
            current = current._next

    # ICA-14 prob 5: Define add_to_end(self, new)
    def add_to_end(self, new):
        current = self._head
        prev = None
        while current != None:
            prev = current
            current = current._next
        
        if prev == None:
            self._head = new
        else:
            prev._next = new

    # ICA-14 prob 6: Define remove_first() (Challenge)
    def remove_first(self):
        if self._head == None:
            return None
        
        removed_node = self._head
        self._head = self._head._next
        removed_node._next = None
        return removed_node

    def __str__(self):
        string = 'LList -> '
        current = self._head
        while current != None:
            string += str(current)
            current = current._next
        return string
        

class Node:
    def __init__(self,value):
        self._value = value
        self._next = None

    def __str__(self):
        if self._next == None:
            nxt = "None"
        else:
            nxt = "->"
        return " |" + str(self._value) + "|:" + nxt


def main():
    # ICA-14 prob 2,a thru d.
    # a) make a linked list called my_ll and add three elements that are ints
    my_ll = LinkedList()
    my_ll.add(Node(12))
    my_ll.add(Node(7))
    my_ll.add(Node(80))

    # b) use the method print_elements() to print out linked list
    print("--- Problem 2b: print_elements ---")
    my_ll.print_elements()

    # c) now use print() to print your linked list
    print("\n--- Problem 2c: print(my_ll) ---")
    print(my_ll)
 
    # d) take a pic of the output (Instructions for student) [cite: 37]

    # ICA-14 prob 3
    # a) call incr() on your linked list
    my_ll.incr()

    # b) use print() to print the list and see the changes 
    print("\n--- Problem 3b: After incr() ---")
    print(my_ll)

    # ICA-14 prob 4
    # a) call replace() on your linked list
    my_ll.replace(81, 99)

    # b) use print() to print the list and take a pic
    print("\n--- Problem 4b: After replace(81, 99) ---")
    print(my_ll)

    # ICA-14 prob 5
    # a) create a new node n and call add_to_end()
    n = Node(40)
    my_ll.add_to_end(n)

    # b) use print() to print the linked list and take a pic
    print("\n--- Problem 5b: After add_to_end(40) ---")
    print(my_ll)
   
    # ICA-14 prob 6 
    # a) call remove_first() on your linked list
    print("\n--- Problem 6: remove_first() ---")
    removed = my_ll.remove_first()
    if removed:
        print(f"Removed node value: {removed._value}")

    # b) use print() to show how the linked list changed
    print("List after removal:")
    print(my_ll)
   
    # additional tests for remove_first()
    print("\n--- More tests for remove_first() ---")
    empty_ll = LinkedList()
    print(f"Empty list removal: {empty_ll.remove_first()}")
    
    one_el_ll = LinkedList()
    one_el_ll.add(Node(100))
    one_el_ll.remove_first()
    print(f"One element list after removal: {one_el_ll}")
    
main()