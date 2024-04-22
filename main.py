def book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_letter_dict(text)
    letter_sort_list = letter_dict_to_sort_list(letter_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for i in letter_sort_list:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")


def sort_on(d):
    return d["num"]


def letter_dict_to_sort_list(num_letter_dict):
    sort_list = []
    for ch in num_letter_dict:
        sort_list.append({"char": ch, "num": num_letter_dict[ch]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


def get_letter_dict(text):
    letter = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter:
            letter[lowered] += 1
        else:
            letter[lowered] = 1
    return letter


main()