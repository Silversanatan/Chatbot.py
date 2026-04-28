''' 
    File: dates.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program manages a database of dates
    and their associated events.
    It reads a file containing operations to insert ('I') or retrieve ('R')
    events. The program handles various date formats by converting them
    to a standardized canonical representation.
'''

# Map month names to numbers
MONTH_LOOKUP = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def get_canonical(date_str):
    """
    Standardizes a date string to the yyyy-m-d format.
    """
    if "/" in date_str:
        # mm/dd/yyyy format
        bits = date_str.split("/")
        m, d, y = bits[0], bits[1], bits[2]
    elif "-" in date_str:
        # yyyy-mm-dd format
        bits = date_str.split("-")
        y, m, d = bits[0], bits[1], bits[2]
    else:
        # MonthName dd yyyy format
        bits = date_str.split()
        m = MONTH_LOOKUP[bits[0]]
        d = bits[1]
        y = bits[2]
    
    # int() removes leading zeros from strings
    return "{:d}-{:d}-{:d}".format(int(y), int(m), int(d))

class Date:
    def __init__(self, date_string, event):
        # Using ._ for internal class attributes
        self._date_id = date_string
        self._event_list = [event]

    def add_event(self, event):
        """Appends a new event to the internal list."""
        self._event_list.append(event)

    def get_canonical(self):
        """Returns the canonical date string."""
        return self._date_id

    def get_events(self):
        """Returns the internal list of events."""
        return self._event_list

    def __len__(self):
        """Returns the number of events for this date."""
        return len(self._event_list)

    def __str__(self):
        return self._date_id

class DateSet:
    def __init__(self):
        # Using ._ for internal dictionary
        self._all_records = {}

    def add_date(self, d_str, e_str):
        """Adds a date or appends to an existing Date object."""
        if d_str in self._all_records:
            self._all_records[d_str].add_event(e_str)
        else:
            new_entry = Date(d_str, e_str)
            self._all_records[d_str] = new_entry

    def get_records(self):
        """Returns the dictionary of Date objects."""
        return self._all_records

    def __len__(self):
        """Returns the number of unique dates stored."""
        return len(self._all_records)

def run_i_op(calendar, text):
    """Parses the 'I' operation text."""
    # Split only at the first colon to preserve colons in event names
    parts = text.split(":", 1)
    date_part = parts[0].strip()
    event_part = parts[1].strip()
    
    canon = get_canonical(date_part)
    calendar.add_date(canon, event_part)

def run_r_op(calendar, text):
    """Parses the 'R' operation text."""
    canon = get_canonical(text)
    records = calendar.get_records()
    
    if canon in records:
        date_obj = records[canon]
        events = date_obj.get_events()
        # Use .sort() to modify the list in place
        events.sort()
        for e in events:
            print("{}: {}".format(canon, e))

def run_p_op(calendar):
    """Parses the 'P' operation to print everything sorted."""
    records = calendar.get_records()
    date_keys = list(records.keys())
    # Sort the dates first
    date_keys.sort()
    
    for d in date_keys:
        date_obj = records[d]
        events = date_obj.get_events()
        # Sort the events for that specific date
        events.sort()
        for e in events:
            print("{}: {}".format(d, e))

def manual_clean(line):
    """
    Cleans leading '#' characters and spaces without using lstrip.
    """
    line = line.strip()
    # Check the first character in a loop to remove all '#'
    while len(line) > 0 and line[0] == "#":
        line = line[1:].strip()
    return line

def process_calendar_file(filename):
    """Main processing loop for the file input."""
    my_calendar = DateSet()
    infile = open(filename, "r")
    
    for line in infile:
        clean_line = manual_clean(line)
        
        # Skip lines that become empty after cleaning
        if clean_line == "":
            continue
            
        op_code = clean_line[0]
        remaining = clean_line[1:].strip()
        
        if op_code == "I":
            run_i_op(my_calendar, remaining)
        elif op_code == "R":
            run_r_op(my_calendar, remaining)
        elif op_code == "P":
            run_p_op(my_calendar)
        else:
            print("Error - Illegal operation.")
            
    infile.close()

def main():
    """Entry point for the program."""
    file_to_open = input()
    process_calendar_file(file_to_open)
main()