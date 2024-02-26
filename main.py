def main():
    book_path = "books/frankenstein.txt"
    get_book_report(book_path)


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letter_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


def convert_dict_to_list(dict):
    letter_dict_list = []
    for char in dict:
        if char.isalpha():
            letter_dict = {}
            letter_dict["letter"] = char
            letter_dict["count"] = dict[char]
            letter_dict_list.append(letter_dict)
    return letter_dict_list


def sort_on(dict):
    return dict["count"]


def get_book_report(path):
    text = get_book_text(path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count_dicts = convert_dict_to_list(letter_count)
    letter_count_dicts.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    for d in letter_count_dicts:
        char = d["letter"]
        count = d["count"]
        print(f"The {char} character was found {count} times")

    print("--- End report ---")


main()
