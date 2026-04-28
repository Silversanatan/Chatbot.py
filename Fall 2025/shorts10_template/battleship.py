"""
File: battleship.py
Author: Rajat Tawari
Course: CSC 120, Fall 2025
Purpose: This program simulates the logic for the Battleship board game.
    It reads a ship placement file to initialize Player 1's board, validating
    for specific errors. It then reads a file of Player 2's guesses and
    reports hits, misses, and sunk ships until the game ends.
"""

import sys


class GridPos:
    """Represents a single position on the game board.

    This class maintains the state of a specific (x, y) coordinate,
    tracking whether a ship is present and if the position has been guessed.
    """

    def __init__(self, x, y):
        """Initialize a new grid position.

        Parameters:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
        """
        self._x = x
        self._y = y
        self._ship = None
        self._guessed = False

    def __str__(self):
        if self._ship is None:
            return "Empty"
        return self._ship.kind


class Ship:
    """Represents a ship in the game.

    This class stores the ship's type, its occupied positions, and
    tracks its health (hits remaining) to determine when it is sunk.
    """

    def __init__(self, kind, x1, y1, x2, y2):
        """Initialize a new ship.

        Parameters:
            kind (str): The abbreviation of the ship type (e.g., 'A', 'B').
            x1, y1 (int): Coordinates of the start of the ship.
            x2, y2 (int): Coordinates of the end of the ship.
        """
        self._kind = kind
        self._positions = []
        self._sizes = {'A': 5, 'B': 4, 'S': 3, 'D': 3, 'P': 2}
        self._size = self._sizes[kind]
        self._hits_remaining = 0

    def __str__(self):
        return self._kind


class Board:
    """Represents the game board.

    This class manages the 10x10 grid of GridPos objects and the collection
    of ships placed on the board. It handles processing guesses and checking
    game state.
    """

    def __init__(self):
        """Initialize the 10x10 game board and an empty ship list."""
        self._grid = []
        for x in range(10):
            row = []
            for y in range(10):
                row.append(GridPos(x, y))
            self._grid.append(row)
        self._ships = []

    def __str__(self):
        return "Board Object"

    def process_guess(self, x, y):
        """Update the board state based on a player's guess.

        Parameters:
            x (int): The x-coordinate of the guess.
            y (int): The y-coordinate of the guess.
        """
        # Validate that the coordinates are within the 10x10 grid boundaries
        if not (0 <= x <= 9 and 0 <= y <= 9):
            print("illegal guess")
            return

        pos = self._grid[x][y]
        # Check the grid position to see if a ship is present or absent
        if pos._ship is None:
            self._handle_miss(pos)
        else:
            self._handle_hit(pos)

    def _handle_miss(self, pos):
        """Helper method to handle output for a miss.

        Parameters:
            pos (GridPos): The position object being guessed.
        """
        # Check if this specific empty spot has been guessed previously
        if pos._guessed:
            print("miss (again)")
        else:
            # Mark the position as guessed if it's the first time
            print("miss")
            pos._guessed = True

    def _handle_hit(self, pos):
        """Helper method to handle logic and output for a hit.

        Parameters:
            pos (GridPos): The position object being guessed.
        """
        # If the position was already guessed, report it immediately
        if pos._guessed:
            print("hit (again)")
        else:
            pos._guessed = True
            # Decrement the ship's health counter and check if it sank
            pos._ship._hits_remaining -= 1
            if pos._ship._hits_remaining == 0:
                print("{} sunk".format(pos._ship._kind))
                self._check_game_over()
            else:
                print("hit")

    def _check_game_over(self):
        """Check if all ships have been sunk and exit if true."""
        all_sunk = True
        # Iterate through all ships to see if any are still afloat
        for ship in self._ships:
            if ship._hits_remaining > 0:
                all_sunk = False

        # If no ships have health remaining, terminate the program successfully
        if all_sunk:
            print("all ships sunk: game over")
            sys.exit(0)


def check_fleet_composition(lines):
    """Verify that the input file contains exactly one of each ship type.

    Parameters:
        lines (list): List of strings from the placement file.
    """
    required_ships = ['A', 'B', 'S', 'D', 'P']
    found_ships = []

    # Extract the ship abbreviations from the input lines
    for line in lines:
        parts = line.split()
        if len(parts) > 0:
            found_ships.append(parts[0])

    # Sort both lists to compare the actual fleet against the required set
    found_ships.sort()
    required_ships.sort()

    if found_ships != required_ships:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)


def get_ship_coordinates(x1, y1, x2, y2):
    """Generate a list of (x,y) tuples covered by a ship.

    Parameters:
        x1, y1, x2, y2 (int): The start and end coordinates.

    Returns:
        list: A list of (x, y) tuples.
    """
    coords = []
    # Determine the range of coordinates for a vertical ship placement
    if x1 == x2:
        start = min(y1, y2)
        end = max(y1, y2)
        for y in range(start, end + 1):
            coords.append((x1, y))
    # Determine the range of coordinates for a horizontal ship placement
    else:
        start = min(x1, x2)
        end = max(x1, x2)
        for x in range(start, end + 1):
            coords.append((x, y1))
    return coords


def process_single_ship_placement(board, line):
    """Parse, validate, and place a single ship from a text line.

    Parameters:
        board (Board): The game board object.
        line (str): A single line from the placement file.
    """
    parts = line.split()
    kind = parts[0]
    x1, y1, x2, y2 = int(parts[1]), int(parts[2]),\
        int(parts[3]), int(parts[4])

    # Check error 2: Validate ship is within the 0-9 grid range
    if not (0 <= x1 <= 9 and 0 <= y1 <= 9 and 0 <= x2 <= 9 and 0 <= y2 <= 9):
        print("ERROR: ship out-of-bounds: " + line.strip())
        sys.exit(0)

    # Check error 3: Validate alignment (must be horizontal or vertical)
    if x1 != x2 and y1 != y2:
        print("ERROR: ship not horizontal or vertical: " + line.strip())
        sys.exit(0)

    coords = get_ship_coordinates(x1, y1, x2, y2)

    # Check error 4: Check for Overlap with existing ships
    for cx, cy in coords:
        if board._grid[cx][cy]._ship is not None:
            print("ERROR: overlapping ship: " + line.strip())
            sys.exit(0)

    # Check error 5: Verify the calculated length matches ship type
    ship_obj = Ship(kind, x1, y1, x2, y2)
    if len(coords) != ship_obj._size:
        print("ERROR: incorrect ship size: " + line.strip())
        sys.exit(0)

    # Final placement: update grid references and ship list
    ship_obj._hits_remaining = len(coords)
    for cx, cy in coords:
        board._grid[cx][cy]._ship = ship_obj
        ship_obj._positions.append(board._grid[cx][cy])
    board._ships.append(ship_obj)


def validate_and_place_ships(board, lines):
    """Orchestrate the validation and placement of all ships.

    Parameters:
        board (Board): The game board object.
        lines (list): The raw lines read from the placement file.
    """
    # First, ensure the file contains exactly one of each required ship
    check_fleet_composition(lines)

    # Iterate through each line to parse and place the individual ships
    for line in lines:
        process_single_ship_placement(board, line)


def main():
    """Main entry point for the Battleship program.

    Reads filenames for placement and guesses, initializes the board,
    and processes the game loop.
    """
    # Read the filenames for configuration from standard input
    placement_file = input()
    guess_file = input()

    board = Board()

    # Explicitly open the placement file to read ship configuration
    f_place = open(placement_file, 'r')
    place_lines = f_place.readlines()
    f_place.close()

    validate_and_place_ships(board, place_lines)

    # Open the guess file and process each line as a coordinate pair
    f_guess = open(guess_file, 'r')
    guess_lines = f_guess.readlines()
    f_guess.close()

    for line in guess_lines:
        parts = line.split()
        if len(parts) == 2:
            gx = int(parts[0])
            gy = int(parts[1])
            board.process_guess(gx, gy)

main()