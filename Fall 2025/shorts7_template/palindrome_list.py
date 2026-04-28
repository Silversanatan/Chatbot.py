def palindrome_list(arglist):
    if arglist == []:
        return True
    return (arglist[0] == arglist[-1]) and palindrome_list(arglist[1:-1])