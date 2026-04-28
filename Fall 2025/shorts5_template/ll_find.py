## DON'T EDIT ANY CODE OTHER THAN THAT OF THE sum() METHOD YOU WRITE.
class LinkedList:
    def __init__(self):
        self._head = None
    
    def sum(self):
        current_sum = 0
        current_node = self._head
        while current_node is not None:
            current_sum += current_node.value()
            current_node = current_node.next()
        return current_sum

    def find(self, item):
        current_node = self._head
        while current_node is not None:
            if current_node.value() == item:
                return True
            current_node = current_node.next()
        return False
    
    def add(self, node):
        node._next = self._head
        self._head = node
        
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    
    def __str__(self):
        string = 'LList -> '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        return string

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        if self._next == None:
            reference = "-> None"
        else:
            reference = "-> "
        return str(self._value) + reference
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next