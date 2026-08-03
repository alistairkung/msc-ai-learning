import pytest

from exercises.lesson02_dictionaries import (
    add_grade,
    average_grade,
    count_words,
    create_student,
    find_top_student,
    get_grade,
    group_students_by_course,
    increment_inventory,
    invert_dictionary,
    merge_settings,
    remove_student,
    student_names,
)


def test_create_student():
    result = create_student("Alice", 24, "Artificial Intelligence")

    assert result == {
        "name": "Alice",
        "age": 24,
        "course": "Artificial Intelligence",
    }


def test_add_grade_adds_a_new_key_and_mutates_student():
    student = {
        "name": "Alice",
        "age": 24,
        "course": "Artificial Intelligence",
    }

    result = add_grade(student, 88)

    assert student["grade"] == 88
    assert result is None


def test_add_grade_replaces_an_existing_grade():
    student = {
        "name": "Alice",
        "grade": 72,
    }

    add_grade(student, 91)

    assert student["grade"] == 91


def test_get_grade_returns_existing_grade():
    student = {
        "name": "Alice",
        "grade": 88,
    }

    assert get_grade(student) == 88


def test_get_grade_returns_none_when_grade_is_missing():
    student = {
        "name": "Alice",
    }

    assert get_grade(student) is None


def test_student_names_returns_names_in_insertion_order():
    students = {
        101: {"name": "Alice", "grade": 88},
        102: {"name": "Bob", "grade": 74},
        103: {"name": "Charlie", "grade": 92},
    }

    assert student_names(students) == ["Alice", "Bob", "Charlie"]


def test_remove_student_removes_and_returns_student():
    students = {
        101: {"name": "Alice"},
        102: {"name": "Bob"},
    }

    result = remove_student(students, 101)

    assert result == {"name": "Alice"}
    assert students == {
        102: {"name": "Bob"},
    }


def test_remove_student_returns_none_for_unknown_id():
    students = {
        101: {"name": "Alice"},
    }

    result = remove_student(students, 999)

    assert result is None
    assert students == {
        101: {"name": "Alice"},
    }


def test_count_words():
    words = [
        "python",
        "java",
        "python",
        "ruby",
        "python",
        "java",
    ]

    assert count_words(words) == {
        "python": 3,
        "java": 2,
        "ruby": 1,
    }


def test_count_words_with_empty_list():
    assert count_words([]) == {}


def test_increment_inventory_increases_existing_quantity():
    inventory = {
        "apple": 3,
        "banana": 5,
    }

    increment_inventory(inventory, "apple", 2)

    assert inventory == {
        "apple": 5,
        "banana": 5,
    }


def test_increment_inventory_adds_missing_item():
    inventory = {
        "apple": 3,
    }

    increment_inventory(inventory, "banana", 4)

    assert inventory == {
        "apple": 3,
        "banana": 4,
    }


def test_average_grade():
    grades = {
        "Alice": 80,
        "Bob": 90,
        "Charlie": 100,
    }

    assert average_grade(grades) == 90


def test_average_grade_returns_none_for_empty_dictionary():
    assert average_grade({}) is None


def test_find_top_student():
    grades = {
        "Alice": 80,
        "Bob": 95,
        "Charlie": 87,
    }

    assert find_top_student(grades) == ("Bob", 95)


def test_find_top_student_returns_none_for_empty_dictionary():
    assert find_top_student({}) is None


def test_merge_settings_returns_merged_dictionary():
    defaults = {
        "theme": "light",
        "language": "English",
        "notifications": True,
    }

    overrides = {
        "theme": "dark",
        "notifications": False,
    }

    result = merge_settings(defaults, overrides)

    assert result == {
        "theme": "dark",
        "language": "English",
        "notifications": False,
    }


def test_merge_settings_does_not_mutate_inputs():
    defaults = {
        "theme": "light",
        "language": "English",
    }

    overrides = {
        "theme": "dark",
    }

    merge_settings(defaults, overrides)

    assert defaults == {
        "theme": "light",
        "language": "English",
    }
    assert overrides == {
        "theme": "dark",
    }


def test_invert_dictionary():
    country_capitals = {
        "UK": "London",
        "France": "Paris",
        "Japan": "Tokyo",
    }

    assert invert_dictionary(country_capitals) == {
        "London": "UK",
        "Paris": "France",
        "Tokyo": "Japan",
    }


def test_invert_dictionary_rejects_duplicate_values():
    data = {
        "first": "shared",
        "second": "shared",
    }

    with pytest.raises(ValueError):
        invert_dictionary(data)


def test_group_students_by_course():
    students = [
        {"name": "Alice", "course": "AI"},
        {"name": "Bob", "course": "Finance"},
        {"name": "Charlie", "course": "AI"},
        {"name": "Diana", "course": "Computer Science"},
        {"name": "Eve", "course": "Finance"},
    ]

    assert group_students_by_course(students) == {
        "AI": ["Alice", "Charlie"],
        "Finance": ["Bob", "Eve"],
        "Computer Science": ["Diana"],
    }


def test_group_students_by_course_with_empty_list():
    assert group_students_by_course([]) == {}
