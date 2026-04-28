def separate_author_title(line):
    colon_index = line.find(":")
    author = line[:colon_index]
    title = line[colon_index + 1:].strip()
    return author, title