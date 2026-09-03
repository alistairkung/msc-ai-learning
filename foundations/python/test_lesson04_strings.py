from lesson04_strings import (
    acronym,
    count_words,
    extract_domain,
    first_character,
    format_greeting,
    is_palindrome,
    join_words,
    last_character,
    longest_word,
    normalize_whitespace,
    remove_prefix,
    replace_word,
    reverse_text,
    reverse_words,
    split_words,
    starts_with,
    title_case,
    word_frequency,
)


def test_first_character():
    assert first_character("Python") == "P"


def test_last_character():
    assert last_character("Python") == "n"


def test_reverse_text():
    assert reverse_text("Python") == "nohtyP"


def test_split_words():
    assert split_words("Python Ruby Java") == [
        "Python",
        "Ruby",
        "Java",
    ]


def test_join_words():
    words = ["Python", "Ruby", "Java"]

    assert join_words(words) == "Python, Ruby, Java"


def test_title_case():
    assert title_case("artificial intelligence engineering") == (
        "Artificial Intelligence Engineering"
    )


def test_replace_word():
    text = "I am learning Ruby"

    assert replace_word(text, "Ruby", "Python") == "I am learning Python"


def test_starts_with():
    assert starts_with("machine learning", "machine") is True
    assert starts_with("machine learning", "learning") is False


def test_format_greeting():
    assert format_greeting("Alistair", "Python") == (
        "Hello Alistair, welcome to Python."
    )


def test_normalize_whitespace():
    assert (
        normalize_whitespace("   Python     is   very    readable   ")
        == "Python is very readable"
    )


def test_reverse_words():
    assert reverse_words("Python is fun") == "fun is Python"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("python") is False


def test_is_palindrome_ignores_case():
    assert is_palindrome("RaceCar") is True


def test_is_palindrome_ignores_spaces():
    assert is_palindrome("never odd or even") is True


def test_count_words():
    assert count_words("Python is readable") == 3


def test_count_words_with_extra_spaces():
    assert count_words("  Python   is   readable  ") == 3


def test_longest_word():
    assert longest_word("Python Ruby JavaScript") == "JavaScript"


def test_longest_word_returns_first_when_tied():
    assert longest_word("Python coding") == "Python"


def test_acronym():
    assert acronym("artificial intelligence engineering") == "AIE"


def test_acronym_ignores_extra_spaces():
    assert acronym("  artificial   intelligence  engineering ") == "AIE"


def test_extract_domain():
    assert extract_domain("alistair@example.com") == "example.com"


def test_extract_domain_with_subdomain():
    assert extract_domain("user@mail.example.com") == "mail.example.com"


def test_remove_prefix():
    assert remove_prefix("unhappy", "un") == "happy"


def test_remove_prefix_when_prefix_is_absent():
    assert remove_prefix("happy", "un") == "happy"


def test_word_frequency():
    text = "python ruby python java python ruby"

    assert word_frequency(text) == {
        "python": 3,
        "ruby": 2,
        "java": 1,
    }


def test_word_frequency_ignores_case():
    text = "Python python PYTHON"

    assert word_frequency(text) == {
        "python": 3,
    }


def test_word_frequency_ignores_extra_whitespace():
    text = "  python   ruby  python "

    assert word_frequency(text) == {
        "python": 2,
        "ruby": 1,
    }
