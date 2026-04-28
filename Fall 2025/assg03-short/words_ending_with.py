def words_ending_with(wordlist, tail):
    result = []
    for word in wordlist:
        if word.endswith(tail):
            result.append(word)
    return result