# Lab 4 - exercise on using a class

class BookData:
    def __init__(self, author, title, rating):
        self._author = author
        self._title = title
        self._rating = rating

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_rating(self):
        return self._rating

    def __str__(self):
        return self._title + " - " + self._author + " - " + str(self._rating)

def process_input(filename):
    books = {}
    f = open(filename, "r")
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 3:
            title, author, rating = parts
            books[title] = BookData(author, title, int(rating))
    f.close()
    return books

def main():
    filename = input("Enter filename: ")
    
    book_dict = process_input(filename)
    print("\nDictionary contents:")
    for title, book in book_dict.items():
        print(str(title) + ":" + str(book))

    prompt = ''
    while prompt != 'done':
        title = input("Book title: ")
        if title in book_dict:
            print("Rating is", book_dict[title].get_rating())
        else:
            print("There is no information on that book.")

        prompt = input('Enter "done" if finished: ')
 
main()