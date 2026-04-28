"""
File: street.py
Author: Rajat Tawari
Course: CSc 120, Fall 2025
Purpose: This program reads a single-line specification of a city street
    and produces a simple ASCII rendering of it. The program is
    written entirely using recursion, with no loops.
"""
def repeat_char(char, count):
    """
    Recursively creates a string by repeating 'char' 'count' times.
    
    char: The character to repeat.
    count: The number of times to repeat the character.
    Returns: A string of 'char' repeated 'count' times.
    """
    if count <= 0:
        # Base case: If count is 0 or less, return an empty string.
        return ""
    else:
        # Recursive step: Add one 'char' and call the function for 'count - 1'.
        return char + repeat_char(char, count - 1)


def build_trash_string(width, pattern, index):
    """
    Recursively builds the trash string for an empty lot.
    
    width: The total width of the lot.
    pattern: The trash pattern string (e.g., "__~").
    index: The current character position being built (starts at 0).
    Returns: The complete trash string for the lot.
    """
    if index == width:
        # Base case: If the current index reaches the total width, stop.
        return ""
    else:
        pattern_char = pattern[index % len(pattern)]
        
        # Replace underscore with a space, as per specification.
        if pattern_char == '_':
            actual_char = ' '
        else:
            actual_char = pattern_char
        return actual_char + build_trash_string(width, pattern, index + 1)


def recursive_join(string_list):
    """
    Recursively concatenates a list of strings into a single string.
    Replicates the functionality of ''.join(string_list).
    
    string_list: A list of strings to join.
    Returns: A single string combining all strings in the list.
    """
    if not string_list:
        # Base case: If the list is empty, return an empty string.
        return ""
    else:
        return string_list[0] + recursive_join(string_list[1:])


def get_row_strings(element_list, h):
    """
    Recursively collects the string representation for each element
    in the list at a specific height 'h'.
    
    element_list: The list of street element objects (Building, Park, etc.).
    h: The current height (row) being drawn.
    Returns: A list of strings, where each string is one element's
             representation at that height.
    """
    if not element_list:
        # Base case: If the list of elements is empty, return an empty list.
        return []
    else:
        # Get the string for the first element at height 'h'.
        row_str = element_list[0].at_height(h)
        return [row_str] + get_row_strings(element_list[1:], h)


def get_total_width(element_list):
    """
    Recursively calculates the total width of all elements in the list.
    
    element_list: The list of street element objects.
    Returns: The integer sum of all element widths.
    """
    if not element_list:
        # Base case: An empty list has a total width of 0.
        return 0
    else:
        return element_list[0].get_width() + get_total_width(element_list[1:])


def find_max_height(element_list):
    """
    Recursively finds the maximum height among all elements in the list.
    
    element_list: The list of street element objects.
    Returns: The integer height of the tallest element.
    """
    if not element_list:
        # Base case: An empty list has a max height of 0.
        return 0
    if len(element_list) == 1:
        return element_list[0].get_height()
    else:
        height1 = element_list[0].get_height()
        # Recursive step: Find the max height of the rest of the list.
        height_rest = find_max_height(element_list[1:])
        # Return the max of the two (max(a, b) is allowed).
        return max(height1, height_rest)


def parse_elements(spec_list):
    """
    Recursively processes a list of specification strings (e.g., "b:5,7,x")
    and returns a list of corresponding class objects.
    
    spec_list: A list of specification strings from the user input.
    Returns: A list of initialized element objects.
    """
    if not spec_list:
        # Base case: If the spec list is empty, return an empty list.
        return []
    else:
        # Process the first specification string.
        spec = spec_list[0]
        parts = spec.split(':')
        kind = parts[0]
        args_str = parts[1]
        args = args_str.split(',')
        
        element = None
        # Create the appropriate object based on the 'kind' (b, p, or e).
        if kind == 'b':
            width = int(args[0])
            height = int(args[1])
            brick = args[2]
            element = Building(width, height, brick)
        elif kind == 'p':
            width = int(args[0])
            foliage = args[1]
            element = Park(width, foliage)
        elif kind == 'e':
            width = int(args[0])
            trash = args[1]
            element = EmptyLot(width, trash)
        
        # Only add the element if it was successfully created.
        if element:
            return [element] + parse_elements(spec_list[1:])
        else:
            return parse_elements(spec_list[1:])


def print_street(elements, current_height, total_width, max_elem_height):
    """
    Recursively prints the street, row by row, from top to bottom.
    
    elements: The list of all street element objects.
    current_height: The row we are currently printing.
    total_width: The total width of the street, for padding.
    max_elem_height: The height of the tallest element.
    """
    if current_height == 0:
        # Base case: Stop when we've printed all rows.
        return
    else:
        row_str = ""
        # Check if this is the top padding row.
        if current_height == max_elem_height + 1:
            row_str = repeat_char(' ', total_width)
        else:
            string_list = get_row_strings(elements, current_height)
            row_str = recursive_join(string_list)
        
        # Print the row enclosed in border pipes.
        print('|' + row_str + '|')
        
        # Recursive step: Call the function for the next row down.
        print_street(elements, current_height - 1,\
                     total_width, max_elem_height)

class Building:
    """Represents a building on the street."""
    
    def __init__(self, width, height, brick):
        """Initializes a Building object."""
        self._width = width
        self._height = height
        self._brick = brick
    
    def get_height(self):
        """Returns the height of the building."""
        return self._height
    
    def get_width(self):
        """Returns the width of the building."""
        return self._width
    
    def at_height(self, h):
        """
        Returns the string representation of the
        building at a specific height 'h'.
        """
        if h > self._height:
            # If 'h' is above the building, return spaces.
            return repeat_char(' ', self._width)
        else:
            # If 'h' is within the building height, return bricks.
            return repeat_char(self._brick, self._width)


class Park:
    """Represents a park on the street."""
    
    def __init__(self, width, foliage):
        """Initializes a Park object. Height is always 5."""
        self._width = width
        self._foliage = foliage
        self._height = 5  # Parks always have a height of 5.
    
    def get_height(self):
        """Returns the height of the park."""
        return self._height
    
    def get_width(self):
        """Returns the width of the park."""
        return self._width
    
    def at_height(self, h):
        """
        Returns the string representation of the park at specific height 'h'.
        This includes the centered tree.
        """
        if h > 5:
            return repeat_char(' ', self._width)
    
        # Calculate side padding to center the 5-wide tree.
        padding_left = (self._width - 5) // 2
        # Calculate remaining padding for the right side.
        padding_right = self._width - 5 - padding_left
    
        # Build the 5-wide tree part based on the height 'h'.
        if h == 5:
            tree_part = repeat_char(' ', 2) + self._foliage +\
                repeat_char(' ', 2)
        elif h == 4:
            tree_part = ' ' + repeat_char(self._foliage, 3) + ' '
        elif h == 3:
            tree_part = repeat_char(self._foliage, 5)
        elif h == 2:
            tree_part = repeat_char(' ', 2) + '|' + repeat_char(' ', 2)
        elif h == 1:
            tree_part = repeat_char(' ', 2) + '|' + repeat_char(' ', 2)
        else:
            # Any other height (like 0) should just be spaces.
            return repeat_char(' ', self._width)
    
        # Return the centered tree part.
        return repeat_char(' ', padding_left) +\
              tree_part + repeat_char(' ', padding_right)

class EmptyLot:
    """Represents an empty lot on the street."""
    
    def __init__(self, width, trash):
        """Initializes an EmptyLot object. Height is always 1."""
        self._width = width
        self._trash = trash
        self._height = 1  # Empty lots always have a height of 1.
    
    def get_height(self):
        """Returns the height of the empty lot."""
        return self._height
    
    def get_width(self):
        """Returns the width of the empty lot."""
        return self._width
    
    def at_height(self, h):
        """
        Returns the string representation of the empty lot at height 'h'.
        """
        if h > 1:
            # If 'h' is above the lot, return spaces.
            return repeat_char(' ', self._width)
        else:
            # At height 1 (ground level), return the trash string.
            return build_trash_string(self._width, self._trash, 0)

def main():
    """
    Main function to run the street renderer.
    """
    spec_line = input("Street: ")
    spec_list = spec_line.split()
    elements = parse_elements(spec_list)
    max_elem_height = find_max_height(elements)
    total_width = get_total_width(elements)
    drawing_height = max_elem_height + 1
    border = '+' + repeat_char('-', total_width) + '+'
    print(border)
    
    print_street(elements, drawing_height, total_width, max_elem_height)
    
    print(border)

main()