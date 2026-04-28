def canonicalize_date(date_str):
    month_map = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    year, month, day = None, None, None
    if '-' in date_str:
        parts = date_str.split('-')
        year, month, day = parts[0], parts[1], parts[2]
    elif '/' in date_str:
        parts = date_str.split('/')
        month, day, year = parts[0], parts[1], parts[2]
    elif ' ' in date_str:
        parts = date_str.split()
        month_name, day, year = parts[0], parts[1], parts[2]
        month = month_map[month_name]
    return "{}-{}-{}".format(int(year), int(month), int(day))