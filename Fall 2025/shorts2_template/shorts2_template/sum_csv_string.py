def sum_csv_string(csv_string):
    number_strings = csv_string.split(',')
    total_sum = 0
    for num_str in number_strings:
        total_sum += int(num_str)  
    return total_sum