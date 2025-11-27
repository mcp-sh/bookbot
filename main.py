from stats import count_words, get_sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def print_report(book):
    text = get_book_text(book)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    count_words(text)
    print("--------- Character Count -------")
    char_count = get_sorted_dict(text)
    for char in char_count:
        if char["char"].isalpha() == True:
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    


def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1] 
        print_report(filepath)
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()