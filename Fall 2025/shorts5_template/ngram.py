def ngram(arglist, startpos, length):
    if length < 0:
        return []

    endpos = startpos + length
    result = arglist[startpos:endpos]

    if len(result) == length:
        return result
    else:
        return []