def count_words(text):
    words = text.split()
    word_count = len(words)
    print(f"Found {word_count} total words")

def count_chars(text):
    chars = set()
    for c in text :
        chars.add(c.lower())
    # print("Set:", chars)    
    char_count = dict.fromkeys(chars, 0)
    for c in text :
        char_count[c.lower()] += 1
    # print("Number of Chars:", len(text))
    # print("Unique Chars", char_count)
    return char_count

def sort_on(items):
    return items["num"]

def get_sorted_dict(text):
    char_dict = count_chars(text)
    # print("Dict", char_dict)
    list_of_letters = []
    for letter in char_dict:
        # print(dict[letter])
        list_of_letters.append(
        { 
            "char" : letter,
            "num" : char_dict[letter]
          }
        )
    list_of_letters.sort(reverse=True, key=sort_on)
    # print("List of Letters, Sorted:", list_of_letters)
    return list_of_letters