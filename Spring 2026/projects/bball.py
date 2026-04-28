"""
    File: bball.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program reads a file containing NCAA women's basketball
        team data, organizes teams into conferences, and calculates win
        ratios. It identifies and prints the conference(s) with the
        highest average win ratio in alphabetical order.
"""

class Team:
    """Represents a basketball team with its name, conference, and stats.

    The class extracts team data from a formatted string and calculates
    the win ratio. It is constructed using a single line from the input file.
    """

    def __init__(self, line):
        """Initializes a Team object by parsing a line of text.

        Parameters: line is a string containing the team name, conference
            in parentheses, and win/loss numbers.
        """
        # Find parentheses from the right to handle names
        last_paren_close = line.rfind(')')
        last_paren_open = line.rfind('(')
        
        self._team_conf = line[last_paren_open + 1 : last_paren_close]
        
        # Split the remaining string to isolate the win and loss integers
        data_after_conf = line[last_paren_close + 1 :].split()
        self._wins = int(data_after_conf[0])
        self._losses = int(data_after_conf[1])
        
        self._team_name = line[:last_paren_open].strip()

    def name(self):
        """Returns the name of the team."""
        # Simple getter for the stored team name attribute
        return self._team_name

    def conf(self):
        """Returns the name of the conference the team belongs to."""
        # Returns the conference string extracted during initialization
        return self._team_conf

    def win_ratio(self):
        """Calculates the fraction of games won by the team.

        Returns: A float representing wins / total games. Returns 0.0
            if no games were played.
        """
        # Sum wins and losses to find the denominator
        total = self._wins + self._losses
        if total == 0:
            return 0.0
        # Calculate ratio as a float fraction
        return self._wins / total

    def __str__(self):
        return "{} : {}".format(self._team_name, self.win_ratio())


class Conference:
    """Represents a sports conference containing multiple Team objects.

    This class maintains a list of teams and provides functionality to
    calculate the aggregate average win ratio for the entire group.
    """

    def __init__(self, conf_name):
        """Initializes a Conference object with a name and empty team list.

        Parameters: conf_name is the string name of the conference.
        """
        # Store the conference name for identification
        self._name_str = conf_name
        # Initialize an empty list to store Team objects
        self._team_list = []

    def __contains__(self, team_obj):
        # Checks if a specific team object exists within this conference
        return team_obj in self._team_list

    def name(self):
        """Returns the name of the conference."""
        # Simple getter for the conference name string
        return self._name_str

    def add(self, team_obj):
        """Adds a Team object to the conference's collection.

        Parameters: team_obj is an instance of the Team class.
        """
        # Append the team to the internal list of conference members
        self._team_list.append(team_obj)

    def win_ratio_avg(self):
        """Computes the average win ratio for all teams in the conference.

        Returns: A float representing the sum of win ratios divided by 
            the number of teams.
        """
        total_ratios = 0
        # Accumulate the win ratio of every team in the conference
        for team in self._team_list:
            total_ratios = total_ratios + team.win_ratio()
        # Perform division once at the end as required by the prompt
        return total_ratios / len(self._team_list)

    def __str__(self):
        return "{} : {}".format(self._name_str, self.win_ratio_avg())


class ConferenceSet:
    """A collection that manages multiple Conference objects.

    It handles the distribution of Team objects into their respective
    conferences and determines which conferences have the best performance.
    """

    def __init__(self):
        """Initializes an empty collection of conferences."""
        # A list that will hold individual Conference class instances
        self._all_conferences = []

    def add(self, team_obj):
        """Assigns a team to the correct conference, creating it if needed.

        Parameters: team_obj is the Team instance to be categorized.
        """
        target = None
        # Look through existing conferences for a matching name
        for current_conf in self._all_conferences:
            if current_conf.name() == team_obj.conf():
                target = current_conf
                break
        
        # Create and store a new conference if no match was found
        if target == None:
            target = Conference(team_obj.conf())
            self._all_conferences.append(target)
            
        target.add(team_obj)

    def best(self):
        """Finds the conference(s) with the highest average win ratio.

        Returns: A list of Conference objects tied for the highest average,
            sorted alphabetically by name.
        """
        if len(self._all_conferences) == 0:
            return []
            
        highest_score = -1.0
        # First pass: find the maximum average win ratio value
        for conf in self._all_conferences:
            current_avg = conf.win_ratio_avg()
            if current_avg > highest_score:
                highest_score = current_avg
        
        winners = []
        # Second pass: collect all conferences that tie for that max value
        for conf in self._all_conferences:
            if conf.win_ratio_avg() == highest_score:
                winners.append(conf)
        
        winner_names = []
        # Extract names for alphabetical sorting
        for conf in winners:
            winner_names.append(conf.name())
        winner_names.sort()

        final_list = []
        # Re-associate sorted names with their original objects
        for name in winner_names:
            for conf in winners:
                if conf.name() == name:
                    final_list.append(conf)
                    break
                    
        return final_list


def main():
    file_name = input()
    
    my_file = open(file_name, 'r')
    master_set = ConferenceSet()

    for line in my_file:
        line = line.strip()
        # Skip empty lines and comments
        if line == "" or line.startswith('#'):
            continue
        
        new_team = Team(line)
        master_set.add(new_team)
    
    my_file.close()

    top_list = master_set.best()
    for conf in top_list:
        print("{} : {}".format(conf.name(), conf.win_ratio_avg()))

main()