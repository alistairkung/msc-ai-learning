import numpy as np


def standardise_features(features):
    means = features.mean(axis=0)
    centered = features - means
    std = centered.std(axis=0)

    return centered / std


def predict_classes(features, weights, biases):
    scores = features @ weights + biases
    return np.argmax(scores, axis=1)


def model_loss(features, weights, bias, actual):
    predictions = features @ weights + bias
    errors = predictions - actual
    squared_errors = errors**2
    mse = squared_errors.mean()

    return mse


def high_attendance_students(students, minimum_attendance):
    return students[students["attendance"] >= minimum_attendance]


def add_weighted_score(students):
    df = students.copy()
    df["weighted_score"] = df["grade"] * df["attendance"]

    return df


def fill_missing_grades(students):
    df = students.copy()
    mean = df["grade"].mean()
    df["grade"] = df["grade"].fillna(mean)

    return df


def course_summary(students):
    result = students.groupby("course")["grade"].agg(["mean", "max"]).reset_index()

    return result.rename(columns={"mean": "mean_grade", "max": "highest_grade"})
