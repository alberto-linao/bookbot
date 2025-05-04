import sys

from stats import create_report, get_num_characters, get_num_words

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path: str):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def book_text_to_array(file_content: str):
    return file_content.split()


book_address = sys.argv[1]
text = get_book_text(book_address)
arr = book_text_to_array(text)
num_words = get_num_words(arr)
num_characters = get_num_characters(text)
create_report(text, book_address, num_words, num_characters)
