def words_beginning_with(wordlist, head):
    result = []
    for word in wordlist:
        if word.startswith(head):
            result.append(word)
    return result