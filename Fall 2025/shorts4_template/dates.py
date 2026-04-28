''' 
    File: dates.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program manages a database of dates
    and their associated events.
    It reads a file containing operations to insert ('I') or retrieve ('R')
    events. The program handles various date formats by converting them
    to a standardized canonical representation.
'''
# A dictionary to map three-letter month abbreviations to month numbers.
MONTHS = {
    'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4',
    'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
    'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

def convert_to_canonical(date_string):
    """
    Converts a date string from various formats to a canonical
    'yyyy-m-d' format.

    This function supports three input formats:
    1. yyyy-mm-dd
    2. mm/dd/yyyy
    3. MonthName dd yyyy (e.g., 'Mar 07 1997')

    Args:
        date_string (str): The date string in one of the supported formats.

    Returns:
        str: The canonical representation of the date, with no leading zeros
             in the month or day (e.g., '1997-3-7').
    """
    yyyy, mm, dd = '', '', ''

    if '/' in date_string:
        # Handles the 'mm/dd/yyyy' format.
        parts = date_string.split('/')
        mm, dd, yyyy = parts[0], parts[1], parts[2]
    elif '-' in date_string:
        # Handles the 'yyyy-mm-dd' format.
        parts = date_string.split('-')
        yyyy, mm, dd = parts[0], parts[1], parts[2]
    else:
        # Handles the 'MonthName dd yyyy' format.
        parts = date_string.split()
        month_name, dd, yyyy = parts[0], parts[1], parts[2]
        mm = MONTHS[month_name]

    # Creates the string by converting parts to integers and back to strings
    canonical_date = "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
    return canonical_date


class Date:
    """
    Represents a single date and stores a collection of events for that date.
    """
    def __init__(self, date_str, event):
        """
        Initializes a Date object with its canonical
        representation and an initial event.

        Args:
            date_str (str): The canonical string representation of the date.
            event (str): The first event string for this date.
        """
        self._canonical_rep = date_str
        self._events = [event]

    def get_canonical(self):
        """Returns the canonical string representation of the date."""
        return self._canonical_rep

    def get_events(self):
        """Returns the list of events associated with this date."""
        return self._events

    def add_event(self, event):
        """
        Adds a new event to this date's list of events.

        Args:
            event (str): The event string to add.
        """
        self._events.append(event)

    def __str__(self):
        """Returns the string representation of the Date object."""
        return self._canonical_rep


class DateSet:
    """
    Represents a collection of Date objects, serving as a database for events.
    """
    def __init__(self):
        """Initializes an empty DateSet 
        using a dictionary to store Date objects."""
        self._dates_dict = {}

    def add_date(self, date_str, event):
        """
        Adds an event for a specific date to the collection.

        If the date does not exist in the collection, a new Date object is
        created and added. If the date already exists, the event is added to
        the existing Date object's list of events.

        Args:
            date_str (str): The canonical string representation of the date.
            event (str): The event string to add.
        """
        if date_str in self._dates_dict:
            self._dates_dict[date_str].add_event(event)
        else:
            new_date = Date(date_str, event)
            self._dates_dict[date_str] = new_date

    def get_date(self, date_str):
        """
        Retrieves a Date object from the collection based
        on its canonical string.

        Args:
            date_str (str): The canonical string representation of the date.

        Returns:
            Date: The Date object if it exists in the collection,
            otherwise None.
        """
        if date_str in self._dates_dict:
            return self._dates_dict[date_str]
        return None

    def __str__(self):
        """Returns a string representation of all dates in the DateSet."""
        return str(list(self._dates_dict.keys()))


def process_operations(filename):
    """
    Reads an input file line by line, parsing and processing each operation.

    Args:
        filename (str): The name of the input file to process.
    """
    calendar = DateSet()
    
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        # Process the line only if it is not empty.
        if line:
            op_type = line[0]
            rest_of_line = line[1:].strip()
            if op_type == 'I':
                # separate the date from the event.
                parts = rest_of_line.split(':', 1)
                date_part = parts[0].strip()
                event_part = parts[1].strip()
                canonical = convert_to_canonical(date_part)
                calendar.add_date(canonical, event_part)
            elif op_type == 'R':
                # For Retrieve operations
                date_part = rest_of_line
                canonical = convert_to_canonical(date_part)
                date_obj = calendar.get_date(canonical)
                if date_obj is not None:
                    events_list = date_obj.get_events()
                    events_list.sort()
                    for event in events_list:
                        print("{}: {}".format(canonical, event))
            else:
                # Handle any lines that do not start with 'I' or 'R'.
                print("Error - Illegal operation.")
    file.close()


def main():
    """
    The main function to drive the program. It prompts the user for a
    filename and then initiates the processing of the file.
    """
    filename = input()
    process_operations(filename)
main()