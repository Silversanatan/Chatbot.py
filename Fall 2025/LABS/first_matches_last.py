def first_matches_last(slist):
    if not slist:
        return []
    first_string = slist[0]
    rest_of_list = slist[1:]
    filtered_rest = first_matches_last(rest_of_list)
    if len(first_string) > 0 and first_string[0] == first_string[-1]:
        return [first_string] + filtered_rest
    else:
        return filtered_rest
    
def main():
    print(first_matches_last(["abba","nope","kook","hello","bob"]))
main()