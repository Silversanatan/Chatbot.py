def display_helper(slist):
    if not slist:
        return
    print(slist[0])
    display_helper(slist[1:])

def display(slist):
    if not slist:
        return
    
    border_length = len(max(slist, key=len))
    border = '-' * border_length
    
    print(border)
    display_helper(slist)
    print(border)
display(["   *   ","  ***  "," ***** ","*******"])