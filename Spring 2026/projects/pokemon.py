"""
    File: pokemon.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2026
    Purpose: This program processes a Pokemon file containing information 
        about Pokemon types and their properties. It calculates the average 
        values for each type's properties and then responds to a set of queries
        about the Pokemon properties. It answers the queries by printing the 
        Pokemon type that have the highest average value for that property.
"""
def read_data(filename):
    """
    Reads Pokemon data from the specified CSV file.
    Args:
        filename: The name of the CSV file to read.
    Returns:
        A two-level dictionary where the first key is the Pokemon's 'Type 1'
        and the second key is the Pokemon's name. The value is another
        dictionary containing the Pokemon's stats.
    """
    database = {}
    file_handle = open(filename, 'r')
    for line in file_handle:
        line = line.strip()
        # Check if the line is not a comment/header before parsing

        if line and line[0] != '#':
            parts = line.split(',')
            # Extract data based on column positions
            name = parts[1]
            type1 = parts[2]
            # Convert raw string parts into integers for math processing
            total = int(parts[4])
            hp = int(parts[5])
            attack = int(parts[6])
            defense = int(parts[7])
            sp_attack = int(parts[8])
            sp_defense = int(parts[9])
            speed = int(parts[10])
            # Create a dictionary for the current Pokemon's stats
            stats = {
                'Total': total,
                'HP': hp,
                'Attack': attack,
                'Defense': defense,
                'SpecialAttack': sp_attack,
                'SpecialDefense': sp_defense,
                'Speed': speed
            }
            # Add the Pokemon to the main database, organized by Type 1
            if type1 not in database:
                database[type1] = {}
            database[type1][name] = stats
    file_handle.close()
    return database

def calculate_avg(database):
    """
    Calculates the average stats for each Pokemon type.
    Args:
        database: A two-level dictionary of Pokemon data.
    Returns:
        A dictionary where keys are Pokemon types and values are dictionaries
        containing the average value for each stat.
    """
    type_avg = {}
    stat_keys = ['Total', 'HP', 'Attack', 'Defense', 
                 'SpecialAttack', 'SpecialDefense', 'Speed']
    for p_type, pokemons in database.items():
        # Initialize a dictionary to hold the sum of stats for the current type
        stat_sums = {}
        for key in stat_keys:
            stat_sums[key] = 0
        num_pokemons = len(pokemons)
        # Sum up the stats for all Pokemon of the current type
        for name, stats in pokemons.items():
            for stat_name, stat_value in stats.items():
                stat_sums[stat_name] += stat_value
        # Calculate and store the averages
        type_avg[p_type] = {}
        for stat_name, total_sum in stat_sums.items():
            average = 0
            if num_pokemons > 0:
                average = total_sum / num_pokemons
            type_avg[p_type][stat_name] = average
    return type_avg

def find_max_avg(type_avg):
    """
    Finds the maximum average value for each stat across all Pokemon types.
    Args:
        type_avg: A dictionary of average stats for each type.
    Returns:
        A dictionary where keys are stat names and values are the highest
        average found for that stat.
    """
    max_stats = {}
    stat_keys = ['Total', 'HP', 'Attack', 'Defense',
                 'SpecialAttack', 'SpecialDefense', 'Speed']
    # Initialize max values to 0.0
    for key in stat_keys:
        max_stats[key] = 0.0
    # Iterate through each type's averages to find the maximum for each stat
    for p_type, averages in type_avg.items():
        for stat_name, avg_value in averages.items():
            if avg_value > max_stats[stat_name]:
                max_stats[stat_name] = avg_value   
    return max_stats

def process_queries(type_avg, max_stats):
    """
    Repeatedly prompts the user for queries and prints the results.
    Args:
        type_avg: A dictionary containing average stats for each type.
        max_stats: A dictionary containing the maximum average for each stat.
    """
    # Map user-friendly query strings to the formal stat names
    query_map = {
        'total': 'Total',
        'hp': 'HP',
        'attack': 'Attack',
        'defense': 'Defense',
        'specialattack': 'SpecialAttack',
        'specialdefense': 'SpecialDefense',
        'speed': 'Speed'
    }
    while True:
        query = input()
        if query == "":
            break  # Exit loop if the user enters an empty line
        processed_query = query.lower()
        if processed_query in query_map:
            stat_name = query_map[processed_query]
            max_average = max_stats[stat_name]
            # Find all types that have this maximum average
            result_types = []
            for p_type, averages in type_avg.items():
                if averages[stat_name] == max_average:
                    result_types.append(p_type)
            # Sort the resulting types alphabetically before printing
            result_types.sort()
            for p_type in result_types:
                print("{}: {}".format(p_type, max_average))

def main():
    filename = input()
    pokemon_data = read_data(filename)
    if pokemon_data:
        averages_by_type = calculate_avg(pokemon_data)
        max_average_stats = find_max_avg(averages_by_type)
        process_queries(averages_by_type, max_average_stats)
main()