def concat_elements_v2(slist, startpos, stoppos):
    if startpos < 0:
        startpos = 0
    if startpos > stoppos:
        return ""
    return "".join(slist[startpos:stoppos + 1])