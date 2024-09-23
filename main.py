def main():
    path = "books/frankenstein.txt"
    book = []
    book = get_book(path)
    count = get_words(book)
    character_count = {}
    character_count = count_characters(book)
    sorted_count = sorting_letter(character_count)
    finished = present_numbers(count, sorted_count, path)
    print(f"{finished}")

def sort_on(dict):
    return dict["num"]

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
        if letter.isalpha() == True:
            if letter in character_count:
                x = character_count.get(letter) +1
                character_count.update({letter : x})
            else:
                character_count[letter] = 1
    return character_count

def sorting_letter(character_count):
    list_of_letters = []
    for letter in character_count:
        ramsa = {}
        count = 0
        count = character_count[letter]
        ramsa["letter"] = letter
        ramsa["num"] = count
        list_of_letters.append(ramsa)
    list_of_letters.sort(reverse=True, key=sort_on)
    return list_of_letters
        
def present_numbers(words, sorted_count, path):
    bokstav = ""
    num = 0
    ramsa = {}
    print(f"--- Begin report of {path} ---")
    print(f"{words} words were found in the document")
    for i in range(0, len(sorted_count)):
        ramsa = sorted_count[i]
        bokstav = ramsa["letter"]
        num = ramsa["num"]
        print(f"the letter {bokstav} was counted {num} times!")
    print("--- End report ---")
    return("o7")

main()