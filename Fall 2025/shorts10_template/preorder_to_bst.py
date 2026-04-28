def preorder_to_bst(preorder):
    if not preorder:
        return None
    
    root = BinarySearchTree(preorder[0])
    
    idx = 1
    while idx < len(preorder) and preorder[idx] < preorder[0]:
        idx += 1
        
    root._left = preorder_to_bst(preorder[1:idx])
    root._right = preorder_to_bst(preorder[idx:])
    
    return root

    

"""DO NOT MODIFY ANYTHING BELOW THIS LINE"""
class BinarySearchTree:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def __str__(self):
        if self == None:
            return 'None'
        else:
            return "({:d} {} {})".format(self._value
                , str(self._left), str(self._right))

def test01():
    tree = preorder_to_bst([3])
    return str(tree)

def test02():
    tree = preorder_to_bst([3, 2, 5])
    return str(tree)

def test03():
    tree = preorder_to_bst([8, 5, 11, 9, 14])
    return str(tree)

def test04():
    tree = preorder_to_bst([24, 11, 5, 7, 30, 28, 41])
    return str(tree)
