def main():
    path = "books/frankenstein.txt"
    book = []
    book = get_book(path)
    count = get_words(book)
    character_count = {}
    character_count = count_characters(book)
    print (character_count)

def get_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_words(book):
    words = book.split()
    count = len(words)
    return count

def count_characters(book):
    character_count = {}
    lowered_book = book.lower()
    for letter in lowered_book:
        if letter in character_count:
            x = character_count.get(letter) +1
            character_count.update({letter : x})
        else:
            character_count[letter] = 1
    return character_count


        


main()