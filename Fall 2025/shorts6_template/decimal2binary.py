class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []
    
    def __str__(self):
        return str(self._items)

def decimal2binary(n):
    s = Stack()
    
    if n == 0:
        return "0"

    while n > 0:
        remainder = n % 2
        s.push(remainder)
        n = n // 2
    
    binary_string = ""
    while not s.is_empty():
        binary_string += str(s.pop())
        
    return binary_string