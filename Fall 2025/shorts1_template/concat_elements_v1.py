def concat_elements_v1(slist, startpos, stoppos):
    result=""
    if startpos < 0:
        startpos = 0
    if stoppos >= len(slist):
        stoppos = len(slist) - 1
    if startpos > stoppos:
        return ""
    for i in range(startpos, stoppos + 1):
        result += slist[i]
        
    return result