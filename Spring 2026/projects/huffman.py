"""
    File: huffman.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program reconstructs a Huffman tree using its preorder 
        and inorder traversal sequences. Once the tree is built, it 
        calculates the postorder traversal and decodes a given binary 
        string based on the tree structure.
"""

class PrefixCodeHuffmanTree:
    """This class represents a node within a Huffman binary tree.

       The class stores a value and references to its left and right 
       child nodes. It includes a recursive method to locate a specific 
       node within the tree based on its value.
    """

    def __init__(self, val):
        """Initializes a tree node with a value and empty children."""
        self.val = val
        self.left = None
        self.right = None

    def find_value_in_tree(self, value):
        """Recursively searches for a node with the specified value.

        Parameters: value is the data to search for in the tree.

        Returns: The node object if found, otherwise None.
        """
        if self.val == value:
            return self

        # Search the left subtree first
        if self.left is not None:
            x = self.left.find_value_in_tree(value)
            if x is not None:
                return x

        # If not in left, search the right subtree
        if self.right is not None:
            x = self.right.find_value_in_tree(value)
            if x is not None:
                return x

        return None


def build(pre, ino):
    """Reconstructs a binary tree from preorder and inorder lists.

    Parameters: 
        pre: a list of integers (preorder traversal).
        ino: a list of integers (inorder traversal).

    Returns: The root node of the reconstructed PrefixCodeHuffmanTree.
    """
    if len(pre) == 0:
        return None

    # The first element in preorder is always the root of the (sub)tree
    root_val = pre[0]
    root = PrefixCodeHuffmanTree(root_val)

    # Locate the root in the inorder list to split left/right subtrees
    i = 0
    while i < len(ino):
        if ino[i] == root_val:
            break
        i = i + 1

    # Split inorder list into left and right subtrees
    left_in = ino[:i]
    right_in = ino[i+1:]

    # Slice preorder list to match the sizes of the inorder subtrees
    left_pre = pre[1:1+len(left_in)]
    right_pre = pre[1+len(left_in):]

    # Recursively build the child nodes
    root.left = build(left_pre, left_in)
    root.right = build(right_pre, right_in)

    return root


def postorder(node):
    """Generates a postorder traversal of the tree.

    Parameters: node is the root of the tree/subtree to traverse.

    Returns: A list of values in postorder (Left, Right, Root).
    """
    if node is None:
        return []

    left = postorder(node.left)
    right = postorder(node.right)

    return left + right + [node.val]


def decode(root, code):
    """Decodes a binary string into values using the Huffman tree.

    Parameters:
        root: the root node of the Huffman tree.
        code: a string of '0's and '1's.

    Returns: A string of the decoded values found at the leaf nodes.
    """
    result = ""
    curr = root

    i = 0
    while i < len(code):
        # Traverse left for '0', right for '1'
        if code[i] == '0':
            curr = curr.left
        else:
            curr = curr.right

        if curr is not None:
            # If a leaf node is reached, record the value and reset to root
            if curr.left is None and curr.right is None:
                result = result + str(curr.val)
                curr = root
        else:
            # Safety reset if traversal falls off the tree
            curr = root

        i = i + 1

    return result


def main():
    file = input("Input file: ")
    f = open(file, "r")

    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    f.close()

    pre = []
    for x in line1.split():
        pre.append(int(x))

    ino = []
    for x in line2.split():
        ino.append(int(x))

    code = line3.strip()

    root = build(pre, ino)
    post = postorder(root)

    out = []
    for x in post:
        out.append(str(x))

    print(" ".join(out))
    print(decode(root, code))
main()