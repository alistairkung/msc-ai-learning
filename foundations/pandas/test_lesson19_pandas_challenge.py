import numpy as np
import pandas as pd

from lesson19_pandas_challenge import (
    clean_students,
    course_performance,
    top_students,
)


def make_messy_students():
    return pd.DataFrame(
        {
            "name": [
                "Alice",
                "Bob",
                "Cara",
                "Dan",
                "Eva",
                "Finn",
            ],
            "course": [
                "ML",
                "NLP",
                "ML",
                "NLP",
                "ML",
                "NLP",
            ],
            "grade": [
                82.0,
                np.nan,
                93.0,
                64.0,
                76.0,
                88.0,
            ],
            "attendance": [
                0.91,
                0.84,
                0.96,
                0.72,
                0.89,
                0.94,
            ],
        }
    )


def test_clean_students():
    students = make_messy_students()

    result = clean_students(students)

    # Missing grade should be filled
    assert result["grade"].isna().sum() == 0

    # New column should exist
    assert "weighted_score" in result.columns

    # Original should not be modified
    assert pd.isna(students.loc[1, "grade"])
    assert "weighted_score" not in students.columns


def test_top_students():
    students = make_messy_students()

    result = top_students(
        students,
        minimum_grade=80,
        minimum_attendance=0.90,
    )

    assert result["name"].tolist() == [
        "Cara",
        "Finn",
        "Alice",
    ]

    assert result["grade"].tolist() == [
        93.0,
        88.0,
        82.0,
    ]


def test_course_performance():
    students = make_messy_students()

    result = course_performance(students)

    assert list(result.columns) == [
        "course",
        "mean_grade",
        "highest_grade",
    ]

    ml = result[result["course"] == "ML"].iloc[0]
    nlp = result[result["course"] == "NLP"].iloc[0]

    assert ml["mean_grade"] == (82 + 93 + 76) / 3
    assert ml["highest_grade"] == 93

    # pandas mean ignores Bob's missing grade
    assert nlp["mean_grade"] == (64 + 88) / 2
    assert nlp["highest_grade"] == 88
