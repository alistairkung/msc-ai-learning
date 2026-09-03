from lesson06_key_functions import (
    alphabetical_students,
    highest_grade,
    longest_name,
    longest_word,
    lowest_grade,
    oldest_person,
    shortest_word,
    sort_people_by_age,
    sort_words_by_last_letter,
    sort_words_by_length,
)


def test_longest_word():
    words = ["Python", "Ruby", "JavaScript"]

    assert longest_word(words) == "JavaScript"


def test_shortest_word():
    words = ["Python", "Ruby", "JavaScript"]

    assert shortest_word(words) == "Ruby"


def test_sort_words_by_length():
    words = ["JavaScript", "Ruby", "Python"]

    assert sort_words_by_length(words) == [
        "Ruby",
        "Python",
        "JavaScript",
    ]


def test_sort_words_by_last_letter():
    words = ["pear", "apple", "banana"]

    assert sort_words_by_last_letter(words) == [
        "banana",
        "apple",
        "pear",
    ]


def test_highest_grade():
    grades = {
        "Alice": 90,
        "Bob": 72,
        "Charlie": 98,
    }

    assert highest_grade(grades) == (
        "Charlie",
        98,
    )


def test_lowest_grade():
    grades = {
        "Alice": 90,
        "Bob": 72,
        "Charlie": 98,
    }

    assert lowest_grade(grades) == (
        "Bob",
        72,
    )


def test_alphabetical_students():
    students = [
        {"name": "Charlie", "grade": 80},
        {"name": "Alice", "grade": 95},
        {"name": "Bob", "grade": 70},
    ]

    assert alphabetical_students(students) == [
        {"name": "Alice", "grade": 95},
        {"name": "Bob", "grade": 70},
        {"name": "Charlie", "grade": 80},
    ]


def test_longest_name():
    students = [
        {"name": "Al", "grade": 80},
        {"name": "Charlotte", "grade": 70},
        {"name": "Bob", "grade": 95},
    ]

    assert longest_name(students) == {
        "name": "Charlotte",
        "grade": 70,
    }


def test_oldest_person():
    people = [
        {"name": "Alice", "age": 31},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 42},
    ]

    assert oldest_person(people) == {
        "name": "Charlie",
        "age": 42,
    }


def test_sort_people_by_age():
    people = [
        {"name": "Alice", "age": 31},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 42},
    ]

    assert sort_people_by_age(people) == [
        {"name": "Bob", "age": 25},
        {"name": "Alice", "age": 31},
        {"name": "Charlie", "age": 42},
    ]
