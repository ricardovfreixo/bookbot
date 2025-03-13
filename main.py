import sys
from stats import count_words, count_characters, sort_dict


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_list = sort_dict(count_characters(book_text))
    for char in char_list:
        key = list(char.keys())[0]
        if key.isalpha():
            print(f"{key}: {char[key]}")



main()
