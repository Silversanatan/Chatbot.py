"""
    File: huffman.py
    Author: Rajat Tawari
    Course: CSc 120, Fall 2025
    Purpose: This program reconstructs a Huffman decoding tree from its
        preorder and inorder traversals. It then uses this tree
        to decode an encoded bit sequence. The program outputs the
        postorder traversal of the tree and the final decoded message.
"""

class PrefixCodeHuffmanTree:
    """
    This class represents a single node within the Huffman decoding tree.
    
    It stores an integer value and references to its left and right children.
    The class is constructed with a value, and its primary method,
    find_value_in_tree, is used for testing and validation.
    """

    def __init__(self, val):
        """
        Initializes a new tree node.
        
        Parameters:
            val (int): The integer value to be stored in this node.
        """
        self._val = val
        self._left = None
        self._right = None

    def find_value_in_tree(self, value):
        """
        Recursively searches the subtree starting at this node for a
        given value.
        
        Parameters:
            value (int): The integer value to search for in the tree.
        
        Returns:
            PrefixCodeHuffmanTree: The node containing the value if found,
                                   or None if the value is not in this subtree.
        """
        # Base case: The current node holds the value
        if self._val == value:
            return self

        # Recursive step: Search the left subtree
        if self._left is not None:
            found_node = self._left.find_value_in_tree(value)
            if found_node is not None:
                return found_node

        # Recursive step: Search the right subtree
        if self._right is not None:
            found_node = self._right.find_value_in_tree(value)
            if found_node is not None:
                return found_node
        
        # Base case: The value was not found in this subtree
        return None

def build_tree(preorder, inorder):
    """
    Recursively constructs the Huffman tree from its preorder and
    inorder traversal lists.
    
    Parameters:
        preorder (list[int]): A list of integer values from a preorder
                              traversal.
        inorder (list[int]): A list of integer values from an inorder
                             traversal.
    
    Returns:
        PrefixCodeHuffmanTree: The root node of the fully constructed tree,
                               or None if the input lists are empty.
    """
    # Base case: An empty tree cannot be built from empty lists.
    if len(preorder) == 0 or len(inorder) == 0:
        return None

    # The first value in a preorder traversal is always the root.
    root_val = preorder[0]
    root_node = PrefixCodeHuffmanTree(root_val)

    # Find the position of the root value in the inorder list.
    root_index = -1
    i = 0
    while i < len(inorder) and root_index == -1:
        if inorder[i] == root_val:
            root_index = i
        i = i + 1

    # Slice the traversal lists into parts for the left and right subtrees
    inorder_left = inorder[0:root_index]
    inorder_right = inorder[root_index + 1:]

    left_subtree_size = len(inorder_left)
    preorder_left = preorder[1 : 1 + left_subtree_size]
    preorder_right = preorder[1 + left_subtree_size :]

    # Recursively call build_tree to construct the left and right children
    root_node._left = build_tree(preorder_left, inorder_left)
    root_node._right = build_tree(preorder_right, inorder_right)

    return root_node

def get_postorder(root):
    """
    Performs a postorder traversal (Left, Right, Root) of the tree
    and returns a list of the node values.
    
    Parameters:
        root (PrefixCodeHuffmanTree): The root node of the tree to traverse.
    
    Returns:
        list[int]: A list of integer values in postorder.
    """
    # Base case: An empty node (None) contributes no values.
    if root is None:
        return []

    # Recursive step: Get values from left and right subtrees
    left_list = get_postorder(root._left)
    right_list = get_postorder(root._right)
    
    # Combine lists: Left + Right + Root
    return left_list + right_list + [root._val]

def decode_sequence(root, encoded_str):
    """
    Decodes the given bit sequence string using the provided Huffman tree.
    This function traverses the tree iteratively based on the '0' (left)
    and '1' (right) bits in the string.
    
    Parameters:
        root (PrefixCodeHuffmanTree): The root of the decoding tree.
        encoded_str (str): A string containing '0's and '1's.
    
    Returns:
        str: The decoded sequence, formed by concatenating the values
             of the leaf nodes reached.
    """
    decoded_output = ""
    current_node = root

    i = 0
    # Iterate through the encoded string bit by bit
    while i < len(encoded_str) and current_node is not None:
        bit = encoded_str[i]
        
        # '0' means go left, '1' means go right
        if bit == '0':
            current_node = current_node._left
        else:
            current_node = current_node._right
        
        # If we landed on a valid node
        if current_node is not None:
            # Check if it is a leaf node (no children)
            if current_node._left is None and current_node._right is None:
                decoded_output = decoded_output + str(current_node._val)
                current_node = root
        
        i = i + 1
    
    return decoded_output

def clean_line(line, is_encoded):
    """
    Cleans a raw line from the input file. It strips whitespace and
    specified punctuation. For traversal lines, it splits the string
    and converts it to a list of integers.
    
    Parameters:
        line (str): The raw line read from the file.
        is_encoded (bool): True if the line is the encoded bit string,
                           False if it is a traversal line.
    
    Returns:
        list[int] or str: A list of integers for traversal lines, or
                          a cleaned string for the encoded line.
    """
    punctuation = "?!.,"
    cleaned = line.strip().strip(punctuation)

    if is_encoded:
        # Encoded line is just a string
        return cleaned
    else:
        # Traversal lines must be split and converted to int
        parts = cleaned.split()
        int_list = []
        for part in parts:
            int_list.append(int(part))
        return int_list

def main():
    """
    Main function to drive the program. It handles file I/O,
    calls functions to build the tree, get the postorder traversal,
    and decode the sequence, then prints the required output.
    """
    filename = input('Input file: ')
    
    # Open, read, and close the file
    file_obj = open(filename, 'r')
    
    preorder_line = file_obj.readline()
    inorder_line = file_obj.readline()
    encoded_line = file_obj.readline()
    
    file_obj.close()

    # Process the raw lines
    preorder_list = clean_line(preorder_line, False)
    inorder_list = clean_line(inorder_line, False)
    encoded_str = clean_line(encoded_line, True)

    # Build the tree from the traversals
    tree_root = build_tree(preorder_list, inorder_list)

    # Get the postorder traversal
    postorder_list = get_postorder(tree_root)
    
    # Convert list of ints to a space-separated string for printing
    postorder_str_list = []
    for val in postorder_list:
        postorder_str_list.append(str(val))
    print(" ".join(postorder_str_list))

    # Decode the sequence using the tree
    decoded_str = decode_sequence(tree_root, encoded_str)
    print(decoded_str)

main()