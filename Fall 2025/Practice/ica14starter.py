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

    # define this
    def incr(self):
        pass

    # define this
    def replace(self, val1, val2):
        pass

    # define this
    def add_to_end(self, new):
        pass

    # define this
    def remove_first(self):
        pass

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

    # Problem 3: Increments each element's value by 1
    def incr(self):
        current = self._head
        while current is not None:
            current._value += 1
            current = current._next

    # Problem 4: Replaces all occurrences of val1 with val2
    def replace(self, val1, val2):
        current = self._head
        while current is not None:
            if current._value == val1:
                current._value = val2
            current = current._next

    # Problem 5: Adds a new node to the end of the list
    def add_to_end(self, new):
        if self._head is None:
            self._head = new
        else:
            current = self._head
            while current._next is not None:
                current = current._next
            current._next = new

    # Problem 6: Removes the first node and returns it
    def remove_first(self):
        if self._head is None:
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
    # Problem 2: Create and print a list
    print("--- Problem 2: Initial List ---")
    my_ll = LinkedList()
    my_ll.add(Node(10))
    my_ll.add(Node(20))
    my_ll.add(Node(30))

    # b) Use print_elements()
    print("Output from print_elements():")
    my_ll.print_elements()
    
    # c) Use print()
    print("\nOutput from print(my_ll):")
    print(my_ll)

    # Problem 3: Increment all elements
    print("\n--- Problem 3: After incr() ---")
    my_ll.incr()
    print(my_ll)

    # Problem 4: Replace an element
    print("\n--- Problem 4: After replace(21, 99) ---")
    my_ll.replace(21, 99)
    print(my_ll)

    # Problem 5: Add a node to the end
    print("\n--- Problem 5: After add_to_end(Node(5)) ---")
    n = Node(5)
    my_ll.add_to_end(n)
    print(my_ll)
   
    # Problem 6: Remove the first element
    print("\n--- Problem 6: After remove_first() ---")
    removed = my_ll.remove_first()
    print(f"Removed node:{removed}")
    print(f"List state: {my_ll}")
   
    print("\n--- More tests for remove_first() ---")
    
    list_one = LinkedList()
    list_one.add(Node(100))
    print(f"\nList with one element before: {list_one}")
    list_one.remove_first()
    print(f"List with one element after:  {list_one}")

    list_empty = LinkedList()
    print(f"\nEmpty list before: {list_empty}")
    list_empty.remove_first()
    print(f"Empty list after:  {list_empty}")
    
main()