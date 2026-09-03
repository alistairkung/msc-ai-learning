import numpy as np
import pandas as pd

from lesson18_pandas_basics import (
    add_passed_column,
    add_teacher_information,
    add_teacher_information_keep_all,
    add_weighted_score,
    average_grade_by_course,
    course_summary,
    fill_missing_grades,
    get_engaged_students,
    get_first_two_students,
    get_grades,
    get_high_achiever_summary,
    get_high_achievers,
    get_ml_or_high_grade,
    get_ml_students,
    get_names_and_grades,
    get_top_left,
    grade_statistics_by_course,
    highest_grade_by_course,
    make_students,
    rank_students,
    remove_missing_grades,
    sort_by_course_and_grade,
)


def test_make_students():
    students = make_students()

    assert students.shape == (4, 4)

    assert list(students.columns) == [
        "name",
        "course",
        "grade",
        "attendance",
    ]


def test_get_grades():
    students = make_students()

    result = get_grades(students)

    assert isinstance(result, pd.Series)

    assert result.tolist() == [82, 71, 93, 64]


def test_get_names_and_grades():
    students = make_students()

    result = get_names_and_grades(students)

    assert isinstance(result, pd.DataFrame)

    assert list(result.columns) == ["name", "grade"]
    assert result.shape == (4, 2)


def test_get_high_achievers():
    students = make_students()

    result = get_high_achievers(students, 80)

    assert result["name"].tolist() == ["Alice", "Cara"]


def test_get_ml_students():
    students = make_students()

    result = get_ml_students(students)

    assert result["name"].tolist() == ["Alice", "Cara"]


def test_get_engaged_students():
    students = make_students()

    result = get_engaged_students(
        students,
        minimum_grade=70,
        minimum_attendance=0.85,
    )

    assert result["name"].tolist() == ["Alice", "Cara"]


def test_get_ml_or_high_grade():
    students = make_students()

    result = get_ml_or_high_grade(
        students,
        minimum_grade=70,
    )

    assert result["name"].tolist() == ["Alice", "Bob", "Cara"]


def test_get_high_achiever_summary():
    students = make_students()

    result = get_high_achiever_summary(students, 80)

    assert result["name"].tolist() == ["Alice", "Cara"]
    assert list(result.columns) == ["name", "grade"]


def test_get_first_two_students():
    students = make_students()

    result = get_first_two_students(students)

    assert result["name"].tolist() == ["Alice", "Bob"]
    assert result.shape == (2, 4)


def test_get_top_left():
    students = make_students()

    result = get_top_left(students)

    assert result.shape == (2, 2)
    assert list(result.columns) == ["name", "course"]


def test_add_passed_column():
    students = make_students()

    result = add_passed_column(students, 70)

    assert result["passed"].tolist() == [
        True,
        True,
        True,
        False,
    ]

    # Original DataFrame should remain unchanged
    assert "passed" not in students.columns


def test_add_weighted_score():
    students = make_students()

    result = add_weighted_score(students)

    expected = np.array(
        [
            74.62,
            59.64,
            89.28,
            46.08,
        ]
    )

    np.testing.assert_allclose(
        result["weighted_score"].to_numpy(),
        expected,
    )

    assert "weighted_score" not in students.columns


def test_rank_students():
    students = make_students()

    result = rank_students(students)

    assert result["name"].tolist() == [
        "Cara",
        "Alice",
        "Bob",
        "Dan",
    ]

    assert result["grade"].tolist() == [
        93,
        82,
        71,
        64,
    ]


def test_sort_by_course_and_grade():
    students = make_students()

    result = sort_by_course_and_grade(students)

    assert result["name"].tolist() == [
        "Cara",  # ML 93
        "Alice",  # ML 82
        "Bob",  # NLP 71
        "Dan",  # NLP 64
    ]


def test_remove_missing_grades():
    students = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cara", "Dan"],
            "grade": [82.0, np.nan, 93.0, 64.0],
        }
    )

    result = remove_missing_grades(students)

    assert result["name"].tolist() == [
        "Alice",
        "Cara",
        "Dan",
    ]


def test_fill_missing_grades():
    students = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cara", "Dan"],
            "grade": [82.0, np.nan, 93.0, 64.0],
        }
    )

    result = fill_missing_grades(students)

    expected_mean = (82 + 93 + 64) / 3

    assert result.loc[1, "grade"] == expected_mean

    # Don't mutate the input
    assert pd.isna(students.loc[1, "grade"])


def test_average_grade_by_course():
    students = make_students()

    result = average_grade_by_course(students)

    assert isinstance(result, pd.Series)

    assert result["ML"] == 87.5
    assert result["NLP"] == 67.5


def test_highest_grade_by_course():
    students = make_students()

    result = highest_grade_by_course(students)

    assert result["ML"] == 93
    assert result["NLP"] == 71


def test_grade_statistics_by_course():
    students = make_students()

    result = grade_statistics_by_course(students)

    assert result.loc["ML", "mean"] == 87.5
    assert result.loc["ML", "max"] == 93
    assert result.loc["ML", "min"] == 82

    assert result.loc["NLP", "mean"] == 67.5
    assert result.loc["NLP", "max"] == 71
    assert result.loc["NLP", "min"] == 64


def test_course_summary():
    students = make_students()

    result = course_summary(students)

    assert list(result.columns) == [
        "course",
        "mean",
        "max",
        "min",
    ]

    assert result["course"].tolist() == ["ML", "NLP"]

    assert result["mean"].tolist() == [87.5, 67.5]


def test_add_teacher_information():
    students = make_students()

    courses = pd.DataFrame(
        {
            "course": ["ML", "NLP"],
            "teacher": ["Sarah", "James"],
        }
    )

    result = add_teacher_information(students, courses)

    assert result["teacher"].tolist() == [
        "Sarah",
        "James",
        "Sarah",
        "James",
    ]

    assert result.shape == (4, 5)


def test_add_teacher_information_keep_all():
    students = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cara", "Dan"],
            "course": ["ML", "NLP", "ML", "Robotics"],
        }
    )

    courses = pd.DataFrame(
        {
            "course": ["ML", "NLP"],
            "teacher": ["Sarah", "James"],
        }
    )

    result = add_teacher_information_keep_all(
        students,
        courses,
    )

    assert result["name"].tolist() == [
        "Alice",
        "Bob",
        "Cara",
        "Dan",
    ]

    assert pd.isna(result.loc[3, "teacher"])
