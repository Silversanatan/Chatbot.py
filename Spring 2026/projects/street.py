"""
File: street.py
Author: Rajat Tawari
Course: CSC 120, Spring 2026
Purpose: This program reads a single-line specification of a city street
    and produces a simple ASCII rendering of it. The program is
    written entirely using recursion to handle the layout, parsing,
    and drawing of buildings, parks, and empty lots.
"""

def repeat_char(char, count):
    """Recursively creates a string by repeating a character.

    Parameters:
        char: The character string to repeat.
        count: An integer representing how many times to repeat it.

    Returns: A string consisting of the character repeated 'count' times.
    """
    if count <= 0:
        return ""
    else:
        return char + repeat_char(char, count - 1)


def build_trash_string(width, pattern, index):
    """Recursively builds the trash string for an empty lot.

    Parameters:
        width: The integer total width of the lot to fill.
        pattern: The string pattern to repeat.
        index: The current integer position in the width being filled.

    Returns: A string of trash characters scaled to the width.
    """
    if index == width:
        return ""
    else:
        pattern_char = pattern[index % len(pattern)]
        # Replace underscore with a space per specification
        if pattern_char == '_':
            actual_char = ' '
        else:
            actual_char = pattern_char
        return actual_char + build_trash_string(width, pattern, index + 1)


def recursive_join(string_list):
    """Recursively concatenates a list of strings.

    Parameters:
        string_list: A list of strings to be joined.

    Returns: A single concatenated string.
    """
    if not string_list:
        return ""
    else:
        return string_list[0] + recursive_join(string_list[1:])


def get_row_strings(element_list, h):
    """Recursively collects strings for each element at a specific height.

    Parameters:
        element_list: A list of Building, Park, or EmptyLot objects.
        h: The integer height (row) currently being rendered.

    Returns: A list of strings representing each element at height 'h'.
    """
    if not element_list:
        return []
    else:
        row_str = element_list[0].at_height(h)
        return [row_str] + get_row_strings(element_list[1:], h)


def get_total_width(element_list):
    """Recursively calculates the total width of the street.

    Parameters:
        element_list: A list of street element objects.

    Returns: An integer representing the sum of all element widths.
    """
    if not element_list:
        return 0
    else:
        return element_list[0].get_width() + get_total_width(element_list[1:])


def find_max_height(element_list):
    """Recursively finds the maximum height among all street elements.

    Parameters:
        element_list: A list of street element objects.

    Returns: An integer representing the height of the tallest element.
    """
    if not element_list:
        return 0
    if len(element_list) == 1:
        return element_list[0].get_height()
    else:
        height1 = element_list[0].get_height()
        height_rest = find_max_height(element_list[1:])
        return max(height1, height_rest)


def parse_elements(spec_list):
    """Recursively converts specification strings into element objects.

    Parameters:
        spec_list: A list of strings (e.g., ["b:5,7,x"]).

    Returns: A list of initialized Building, Park, or EmptyLot objects.
    """
    if not spec_list:
        return []
    else:
        spec = spec_list[0]
        parts = spec.split(':')
        kind = parts[0]
        args = parts[1].split(',')
        
        element = None
        if kind == 'b':
            element = Building(int(args[0]), int(args[1]), args[2])
        elif kind == 'p':
            element = Park(int(args[0]), args[1])
        elif kind == 'e':
            element = EmptyLot(int(args[0]), args[1])
        
        if element:
            return [element] + parse_elements(spec_list[1:])
        else:
            return parse_elements(spec_list[1:])


def print_street(elements, current_height, total_width, max_elem_height):
    """Recursively prints the street row by row from top to bottom.

    Parameters:
        elements: List of street objects.
        current_height: The integer row currently being printed.
        total_width: Total integer width of the street.
        max_elem_height: Height of the tallest element for padding logic.
    """
    if current_height == 0:
        return
    else:
        if current_height == max_elem_height + 1:
            row_str = repeat_char(' ', total_width)
        else:
            string_list = get_row_strings(elements, current_height)
            row_str = recursive_join(string_list)
        
        print('|' + row_str + '|')
        # Move down to the next row
        print_street(elements, current_height - 1,\
             total_width, max_elem_height)


class Building:
    """Represents a building with a specific width, height, and brick type.

    The class provides methods to retrieve dimensions and generate the
    visual string representation of the building at any given height.
    """
    def __init__(self, width, height, brick):
        """Initializes the Building with dimensions and material.

        Parameters:
            width: Integer width of the building.
            height: Integer height of the building.
            brick: Single character used for the building walls.
        """
        self._width = width
        self._height = height
        self._brick = brick
    
    def get_height(self):
        """Returns the integer height of the building."""
        return self._height
    
    def get_width(self):
        """Returns the integer width of the building."""
        return self._width
    
    def at_height(self, h):
        """Returns the building string at a specific height.

        Parameters: h is the integer height to check.

        Returns: A string of bricks if h is within height, otherwise spaces.
        """
        if h > self._height:
            return repeat_char(' ', self._width)
        else:
            return repeat_char(self._brick, self._width)


class Park:
    """Represents a park containing a single centered tree.

    The class handles the geometry of the tree (foliage and trunk) 
    within a specified width. Parks always have a fixed height of 5.
    """
    def __init__(self, width, foliage):
        """Initializes the Park with a width and foliage type.

        Parameters:
            width: Integer width of the park.
            foliage: Single character for the tree leaves.
        """
        self._width = width
        self._foliage = foliage
        self._height = 5 
    
    def get_height(self):
        """Returns the integer height of the park."""
        return self._height
    
    def get_width(self):
        """Returns the integer width of the park."""
        return self._width
    
    def at_height(self, h):
        """Generates the centered tree layers or trunk at height 'h'.

        Parameters: h is the integer height level.

        Returns: A string representing the park slice at that height.
        """
        if h > 5:
            return repeat_char(' ', self._width)
    
        # Logic to center the 5-character wide tree pattern
        padding_left = (self._width - 5) // 2
        padding_right = self._width - 5 - padding_left
    
        if h == 5:
            tree_part = repeat_char(' ', 2) + self._foliage +\
                  repeat_char(' ', 2)
        elif h == 4:
            tree_part = ' ' + repeat_char(self._foliage, 3) + ' '
        elif h == 3:
            tree_part = repeat_char(self._foliage, 5)
        elif h == 2 or h == 1:
            tree_part = repeat_char(' ', 2) + '|' + repeat_char(' ', 2)
        else:
            return repeat_char(' ', self._width)
    
        return repeat_char(' ', padding_left) + tree_part +\
              repeat_char(' ', padding_right)


class EmptyLot:
    """Represents an empty lot that contains a repeating trash pattern.

    The lot has a fixed height of 1. Above the ground level, it is 
    represented by empty spaces.
    """
    def __init__(self, width, trash):
        """Initializes the EmptyLot with width and a trash pattern.

        Parameters:
            width: Integer width of the lot.
            trash: String pattern of trash found in the lot.
        """
        self._width = width
        self._trash = trash
        self._height = 1
    
    def get_height(self):
        """Returns the integer height of the lot."""
        return self._height
    
    def get_width(self):
        """Returns the integer width of the lot."""
        return self._width
    
    def at_height(self, h):
        """Returns trash pattern at ground level, otherwise spaces.

        Parameters: h is the integer height level.

        Returns: A string for the lot at height 'h'.
        """
        if h > 1:
            return repeat_char(' ', self._width)
        else:
            return build_trash_string(self._width, self._trash, 0)


def main():
    spec_line = input("Street: ")
    if not spec_line.strip():
        return
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