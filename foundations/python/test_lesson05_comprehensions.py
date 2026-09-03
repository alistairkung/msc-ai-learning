from lesson05_comprehensions import (
    course_names,
    even_numbers,
    grade_lookup,
    long_words,
    lowercase_unique_words,
    names_by_course,
    passing_student_names,
    square_numbers,
    student_summaries,
    word_lengths,
)


def test_square_numbers():
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]


def test_square_numbers_with_empty_list():
    assert square_numbers([]) == []


def test_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_even_numbers_with_no_matches():
    assert even_numbers([1, 3, 5]) == []


def test_long_words():
    words = ["AI", "Python", "Ruby", "JavaScript"]

    assert long_words(words, 5) == [
        "Python",
        "JavaScript",
    ]


def test_word_lengths():
    words = ["Python", "Ruby", "Java"]

    assert word_lengths(words) == {
        "Python": 6,
        "Ruby": 4,
        "Java": 4,
    }


def test_lowercase_unique_words():
    words = [
        "Python",
        "PYTHON",
        "Ruby",
        "ruby",
        "Java",
    ]

    assert lowercase_unique_words(words) == {
        "python",
        "ruby",
        "java",
    }


def test_course_names():
    students = [
        {"name": "Alice", "course": "AI"},
        {"name": "Bob", "course": "Finance"},
        {"name": "Charlie", "course": "AI"},
    ]

    assert course_names(students) == [
        "AI",
        "Finance",
        "AI",
    ]


def test_passing_student_names():
    students = [
        {"name": "Alice", "grade": 88},
        {"name": "Bob", "grade": 49},
        {"name": "Charlie", "grade": 72},
        {"name": "Diana", "grade": 50},
    ]

    assert passing_student_names(students, 50) == [
        "Alice",
        "Charlie",
        "Diana",
    ]


def test_grade_lookup():
    students = [
        {"name": "Alice", "grade": 88},
        {"name": "Bob", "grade": 74},
        {"name": "Charlie", "grade": 92},
    ]

    assert grade_lookup(students) == {
        "Alice": 88,
        "Bob": 74,
        "Charlie": 92,
    }


def test_student_summaries():
    students = [
        {"name": "Alice", "course": "AI"},
        {"name": "Bob", "course": "Finance"},
    ]

    assert student_summaries(students) == [
        "Alice studies AI",
        "Bob studies Finance",
    ]


def test_names_by_course():
    students = [
        {"name": "Alice", "course": "AI"},
        {"name": "Bob", "course": "Finance"},
        {"name": "Charlie", "course": "AI"},
        {"name": "Diana", "course": "Computer Science"},
        {"name": "Eve", "course": "Finance"},
    ]

    assert names_by_course(students) == {
        "AI": ["Alice", "Charlie"],
        "Finance": ["Bob", "Eve"],
        "Computer Science": ["Diana"],
    }
