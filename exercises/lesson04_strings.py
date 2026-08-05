from collections import defaultdict


def first_character(text):
    return text[0]


def last_character(text):
    return text[-1]


def reverse_text(text):
    return text[::-1]


def split_words(text):
    return text.split(" ")


def join_words(words):
    return ", ".join(words)


def title_case(text):
    return text.title()


def replace_word(text, old, new):
    return text.replace(old, new)


def starts_with(text, prefix):
    return text.startswith(prefix)


def format_greeting(name, language):
    return f"Hello {name}, welcome to {language}."


def normalize_whitespace(text):
    return " ".join(text.split())


def reverse_words(text):
    return " ".join(text.split()[::-1])


def is_palindrome(text):
    processed_text = "".join(text.lower().split())
    return processed_text == processed_text[::-1]


def count_words(text):
    return len(text.split())


def longest_word(text):
    return max(text.split(), key=lambda item: len(item))


def acronym(text):
    return "".join(word[0].upper() for word in text.split())


def extract_domain(email):
    return email.split("@", 1)[1]


def remove_prefix(text, prefix):
    if not text.startswith(prefix):
        return text

    return text[len(prefix) :]


def word_frequency(text):
    frequencies = defaultdict(int)

    for word in text.split():
        frequencies[word.lower()] += 1

    return frequencies
