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



def is_balanced(symbols):
    s = Stack()
    for symbol in symbols:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                top = s.pop()
                if not (top == '(' and symbol == ')' or \
                        top == '{' and symbol == '}' or \
                        top == '[' and symbol == ']'):
                    return False
    return s.is_empty()