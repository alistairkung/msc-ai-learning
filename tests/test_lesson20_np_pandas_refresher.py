import numpy as np
import pandas as pd

from exercises.lesson20_np_pandas_refresher import (
    add_weighted_score,
    course_summary,
    fill_missing_grades,
    high_attendance_students,
    model_loss,
    predict_classes,
    standardise_features,
)

# -------------------------
# NumPy / ML
# -------------------------


def test_standardise_features():
    features = np.array(
        [
            [10.0, 100.0],
            [20.0, 200.0],
            [30.0, 300.0],
            [40.0, 400.0],
        ]
    )

    result = standardise_features(features)

    assert result.shape == features.shape

    np.testing.assert_allclose(
        result.mean(axis=0),
        np.zeros(2),
        atol=1e-10,
    )

    np.testing.assert_allclose(
        result.std(axis=0),
        np.ones(2),
        atol=1e-10,
    )


def test_predict_classes():
    features = np.array(
        [
            [1.0, 2.0],
            [3.0, 1.0],
            [2.0, 4.0],
        ]
    )

    weights = np.array(
        [
            [2.0, 1.0, 0.0],
            [0.0, 1.0, 2.0],
        ]
    )

    biases = np.array([0.0, 1.0, 0.0])

    result = predict_classes(features, weights, biases)

    np.testing.assert_array_equal(
        result,
        np.array([1, 0, 2]),
    )


def test_model_loss():
    features = np.array(
        [
            [1.0],
            [2.0],
            [3.0],
        ]
    )

    weights = np.array([2.0])
    bias = 1.0

    actual = np.array([3.0, 5.0, 7.0])

    result = model_loss(features, weights, bias, actual)

    assert result == 0.0


# -------------------------
# pandas
# -------------------------


def make_students():
    return pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cara", "Dan"],
            "course": ["ML", "NLP", "ML", "NLP"],
            "grade": [82.0, np.nan, 93.0, 64.0],
            "attendance": [0.91, 0.84, 0.96, 0.72],
        }
    )


def test_high_attendance_students():
    students = make_students()

    result = high_attendance_students(
        students,
        minimum_attendance=0.90,
    )

    assert result["name"].tolist() == [
        "Alice",
        "Cara",
    ]


def test_add_weighted_score():
    students = make_students()

    result = add_weighted_score(students)

    assert "weighted_score" in result.columns
    assert "weighted_score" not in students.columns

    np.testing.assert_allclose(
        result.loc[[0, 2, 3], "weighted_score"].to_numpy(),
        np.array(
            [
                82.0 * 0.91,
                93.0 * 0.96,
                64.0 * 0.72,
            ]
        ),
    )


def test_fill_missing_grades():
    students = make_students()

    result = fill_missing_grades(students)

    expected_mean = (82.0 + 93.0 + 64.0) / 3

    assert result.loc[1, "grade"] == expected_mean
    assert pd.isna(students.loc[1, "grade"])


def test_course_summary():
    students = make_students()

    result = course_summary(students)

    assert list(result.columns) == [
        "course",
        "mean_grade",
        "highest_grade",
    ]

    ml = result[result["course"] == "ML"].iloc[0]
    nlp = result[result["course"] == "NLP"].iloc[0]

    assert ml["mean_grade"] == 87.5
    assert ml["highest_grade"] == 93.0

    # Bob is NaN, so mean ignores him
    assert nlp["mean_grade"] == 64.0
    assert nlp["highest_grade"] == 64.0
