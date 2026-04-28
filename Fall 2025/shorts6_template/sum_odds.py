def sum_odds(alist):
    if len(alist)==0:
        return 0
    
    first_element = alist[0]
    rest_of_list = alist[1:]
    
    if first_element % 2 != 0:
        return first_element + sum_odds(rest_of_list)
    else:
        return sum_odds(rest_of_list)