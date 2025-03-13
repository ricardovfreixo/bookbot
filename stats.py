from collections import Counter


def count_words(text_string):
    words = text_string.split()
    return len(words)


def count_characters(text_string):
    return dict(Counter(text_string.lower()))


def sort_dict(char_dict):
    char_list = [{key: value} for key, value in char_dict.items()]

    # Sort by the value of the inner dictionary
    char_list.sort(key=lambda d: list(d.values())[0], reverse=True)
    return char_list
