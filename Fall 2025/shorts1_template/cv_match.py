def cv_match(sentence, pattern):
    words = sentence.split()
    matching_words = []
    for word in words:
        word_pattern = ""
        for letter in word.lower():
            if letter in "aeiou":
                word_pattern += "v"
            else:
                word_pattern += "c"
        if word_pattern == pattern:
            matching_words.append(word)
    return matching_words