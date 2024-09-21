def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in this document")

    for key, value in sorted(chars_dict.items()):
        if key.isalpha():
            print(f"the {key} Character was found {value} times")
    print("--- End Report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
