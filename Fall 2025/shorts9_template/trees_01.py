class BinarySearchTree:
    def __init__(self):
        self._value = None
        self._left = None
        self._right = None
    
    def add(self, value):
        if self._value is None:
            self._value = value
            self._left = BinarySearchTree()
            self._right = BinarySearchTree()
        elif value < self._value:
            self._left.add(value)
        elif value > self._value:
            self._right.add(value)
    
    
    def find(self, value):
        if self._value is None:
            return None
        
        if self._value == value:
            return self
        
        if value < self._value:
            return self._left.find(value)
        
        if value > self._value:
            return self._right.find(value)
        
    
    def __str__(self):
        if self._value is None:
            return "None"
        else:
            return "({:d} {} {})".format(self._value, str(self._left), str(self._right))