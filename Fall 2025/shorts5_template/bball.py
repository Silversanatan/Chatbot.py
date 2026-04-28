"""
    File: bball.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program analyzes a file of NCAA women's basketball
        data. It reads team names, conferences, wins, and losses;
        calculates the win ratio for each team and the average win
        ratio for each conference; and finally identifies and prints
        the conference(s) with the highest average win ratio.
"""
class Team:
    """This class represents a single basketball team and its season data.

       The class stores the team's name, its conference, and its calculated
       win ratio. It is constructed by parsing a single line of text from
       the input data file. The primary methods provide access to these
       attributes.
    """
    def __init__(self, line):
        """Initializes a Team object by parsing a formatted string.

           This method extracts the team name, conference, wins, and losses
           from a single line of text. It then calculates and stores the
           team's win ratio.

           Parameters:
               line: A string containing the team's data, e.g.,
                     "Team Name (Conference) Wins Losses".
        """
        last_open_paren = line.rfind('(')
        last_close_paren = line.rfind(')')

        self._name = line[:last_open_paren].strip()
        self._conference = line[last_open_paren + 1:last_close_paren].strip()

        win_loss_str = line[last_close_paren + 1:].strip()
        parts = win_loss_str.split()
        wins = int(parts[0])
        losses = int(parts[1])

        total_games = wins + losses
        if total_games == 0:
            self._win_ratio = 0.0
        else:
            self._win_ratio = wins / total_games

    def name(self):
        return self._name

    def conf(self):
        return self._conference

    def win_ratio(self):
        return self._win_ratio

    def __str__(self):
        return "{} : {}".format(self.name(), self.win_ratio())
    
class Conference:
    """This class represents a conference as a collection of teams.

       It stores the conference's name and a list of all the Team objects
       that belong to it. The primary methods allow for adding teams and
       calculating the conference's average win ratio. It is constructed
       with just the conference name.
    """
    def __init__(self,conf_name):
        """Initializes a Conference object with a name.

           The list of teams for the conference is initialized to be empty.

           Parameters:
               conf_name: A string representing the name of the conference.
        """
        self._name = conf_name
        self._teams = []
    def __contains__(self,team):
        """Checks if a team is in this conference by name.

           Parameters:
               team: A Team object to check for.
           Returns: True if a team with the same name is in the
               conference, False otherwise.
        """
        is_present = False
        for t in self._teams:
            if t.name() == team.name():
                is_present = True
        return is_present
    def name(self):
        return self._name
    def add(self,team):
        """Adds a team to the conference's list of teams.

           Parameters:
               team: The Team object to add to this conference.
           Returns: None.
        """
        self._teams.append(team)
    def win_ratio_avg(self):
        """Calculates the average win ratio for the conference.

           This is computed by summing the win ratios of all teams in the
           conference and dividing by the number of teams.

           Returns: A float representing the average win ratio. Returns 0.0
               if the conference has no teams.
        """
        total_ratios = 0.0
        for team in self._teams:
            total_ratios += team.win_ratio()
        if len(self._teams) == 0:
            return 0.0
        else:
            return total_ratios / len(self._teams)
    def __str__(self):
        return "{} : {}".format(self.name(), self.win_ratio_avg())
    
class ConferenceSet:
    """This class represents a collection of all Conference objects.

       It acts as a container for all conferences in a season. Its main
       purpose is to organize teams into their respective conferences and
       to identify which conference(s) had the best performance. It is
       constructed as an empty set.
    """
    def __init__(self):
        """Initializes an empty collection of conferences."""
        self._conferences = {}
    def add(self, team):
        """Adds a team to the appropriate conference.

           If a conference for the team does not yet exist in the
           collection, it is created automatically.

           Parameters:
               team: The Team object to be added.
           Returns: None.
        """
        conf_name = team.conf()
        if conf_name not in self._conferences:
            new_conference = Conference(conf_name)
            self._conferences[conf_name] = new_conference
        self._conferences[conf_name].add(team)
    def best(self):
        """Finds the conference(s) with the highest average win ratio.

           This method iterates through all conferences to find the maximum
           average win ratio and returns a list of all Conference objects
           that meet that maximum. This handles cases where there is a tie.

           Returns: A list of Conference objects.
        """
        best_conferences = []
        max_avg = -1.0
        for conf in self._conferences.values():
            current_avg = conf.win_ratio_avg()
            if current_avg > max_avg:
                max_avg = current_avg
                best_conferences = [conf]
            elif current_avg == max_avg:
                best_conferences.append(conf)
        return best_conferences


def main():
    filename = input()
    data_file = open(filename, 'r')
    all_conferences = ConferenceSet()
    for line in data_file:
        line = line.strip()
        if line != "" and not line.startswith("#"):
            team = Team(line)
            all_conferences.add(team)
    data_file.close()
    best_list = all_conferences.best()
    best_conf_map = {}
    best_names = []
    for conf in best_list:
        conf_name = conf.name()
        best_conf_map[conf_name] = conf
        best_names.append(conf_name)
    best_names.sort()
    for name in best_names:
        conference_object = best_conf_map[name]
        print("{} : {}".format(conference_object.name(),\
                               conference_object.win_ratio_avg()))
main()