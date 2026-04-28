"""
File: battleship.py
Author: Rajat Tawari
Course: CSC 120, Spring 2026
Purpose: This program simulates part of the Battleship game. It reads a file
    containing ship placements and another file containing guesses, then
    processes the guesses to determine hits, misses, and when ships are sunk.
"""


class GridPos:
    """Represents a single position on the Battleship grid.

    Each position stores its coordinates, the ship occupying it (if any),
    and whether it has been guessed before.
    """

    def __init__(self, x, y):
        """Initialize a grid position.

        Parameters: x and y are integers representing coordinates (0–9).

        Returns: None
        """
        self._x = x
        self._y = y
        self._ship = None
        self._guessed = False

    def __str__(self):
        return "(" + str(self._x) + "," + str(self._y) + ")"


class Ship:
    """Represents a ship placed on the board.

    A ship has a type, size, list of positions it occupies, and tracks
    how many of its positions are not yet hit.
    """

    def __init__(self, kind, size):
        """Initialize a ship.

        Parameters: kind is a character representing ship type,
                    size is the length of the ship.

        Returns: None
        """
        self._kind = kind
        self._size = size
        self._positions = []
        self._left = size

    def __str__(self):
        return self._kind


class Board:
    """Represents the game board.

    The board contains a 10x10 grid of GridPos objects and a list of ships.
    It supports adding ships and processing guesses.
    """

    def __init__(self):
        """Initialize the board with empty grid and no ships.

        Returns: None
        """
        self._grid = []

        # create 10x10 grid of GridPos objects
        for i in range(10):
            row = []
            for j in range(10):
                row.append(GridPos(i, j))
            self._grid.append(row)

        self._ships = []

    def add_ship(self, kind, x1, y1, x2, y2, line):
        """Add a ship to the board based on given coordinates.

        Parameters: kind is the ship type,
                    x1, y1 and x2, y2 are endpoints of the ship,
                    line is the original input line for error messages.

        Returns: True if the ship is successfully added, False otherwise.
        """
        sizes = {'A':5,'B':4,'S':3,'D':3,'P':2}

        # check valid ship type
        if kind not in sizes:
            print("ERROR: fleet composition incorrect")
            return False

        # check bounds
        if x1<0 or x1>9 or y1<0 or y1>9 or x2<0 or x2>9 or y2<0 or y2>9:
            print("ERROR: ship out-of-bounds: " + line)
            return False

        # check orientation
        if x1!=x2 and y1!=y2:
            print("ERROR: ship not horizontal or vertical: " + line)
            return False

        ship = Ship(kind, sizes[kind])
        cells = []

        # collect positions of the ship
        if x1 == x2:
            start = min(y1,y2)
            end = max(y1,y2)
            for y in range(start, end+1):
                # check overlap
                if self._grid[x1][y]._ship != None:
                    print("ERROR: overlapping ship: " + line)
                    return False
                cells.append(self._grid[x1][y])
        else:
            start = min(x1,x2)
            end = max(x1,x2)
            for x in range(start, end+1):
                # check overlap
                if self._grid[x][y1]._ship != None:
                    print("ERROR: overlapping ship: " + line)
                    return False
                cells.append(self._grid[x][y1])

        # check correct size
        if len(cells) != sizes[kind]:
            print("ERROR: incorrect ship size: " + line)
            return False

        # assign ship to positions
        for c in cells:
            c._ship = ship
            ship._positions.append(c)

        self._ships.append(ship)
        return True

    def guess(self, x, y):
        """Process a guess at position (x, y).

        Parameters: x and y are integers representing coordinates.

        Returns: True if all ships are sunk, False otherwise.
        """
        # check bounds
        if x<0 or x>9 or y<0 or y>9:
            print("illegal guess")
            return False

        pos = self._grid[x][y]

        # miss case
        if pos._ship == None:
            if pos._guessed:
                print("miss (again)")
            else:
                print("miss")
            pos._guessed = True
            return False

        ship = pos._ship

        # repeated hit
        if pos._guessed:
            print("hit (again)")
            return False

        # new hit
        pos._guessed = True
        ship._left -= 1

        # check if ship is sunk
        if ship._left == 0:
            print(ship._kind + " sunk")
            all_sunk = True

            # check if all ships are sunk
            for s in self._ships:
                if s._left > 0:
                    all_sunk = False

            if all_sunk:
                print("all ships sunk: game over")
                return True
        else:
            print("hit")

        return False


def main():
    """Main function that runs the Battleship simulation.

    Reads placement and guess files, sets up the board,
    and processes all guesses.

    Returns: None
    """
    board = Board()

    placement_file = input()
    f = open(placement_file)
    lines = f.readlines()
    f.close()

    # check number of ships
    if len(lines) != 5:
        print("ERROR: fleet composition incorrect")
        return

    seen = set()

    for line in lines:
        parts = line.split()

        # check correct format
        if len(parts) != 5:
            print("ERROR: fleet composition incorrect")
            return

        kind = parts[0]

        # check duplicate ship types
        if kind in seen:
            print("ERROR: fleet composition incorrect")
            return
        seen.add(kind)

        x1 = int(parts[1])
        y1 = int(parts[2])
        x2 = int(parts[3])
        y2 = int(parts[4])

        ok = board.add_ship(kind, x1, y1, x2, y2, line.strip())

        # stop if error
        if not ok:
            return

    guess_file = input()
    f = open(guess_file)

    for line in f:
        parts = line.split()

        if len(parts) != 2:
            continue

        x = int(parts[0])
        y = int(parts[1])

        done = board.guess(x, y)

        # stop if game over
        if done:
            return

    f.close()
main()