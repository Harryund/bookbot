def main():
    path = "books/frankenstein.txt"
    book = []
    book = get_book(path)
    count = get_words(book)
    print (count)

def get_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_words(book):
    words = book.split()
    count = len(words)
    return count


main()