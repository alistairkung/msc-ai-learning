import pandas as pd
from sklearn.model_selection import train_test_split

from exercises.lesson21_sklearn_intro import (
    evaluate_accuracy,
    evaluate_classifier,
    get_confusion_matrix,
    make_predictions,
    train_classifier,
)


def make_students():
    return pd.DataFrame(
        {
            "age": [
                20,
                22,
                24,
                26,
                28,
                30,
                32,
                34,
                36,
                38,
                40,
                42,
            ],
            "income": [
                25000,
                28000,
                32000,
                35000,
                40000,
                45000,
                50000,
                55000,
                62000,
                68000,
                75000,
                82000,
            ],
            "attendance": [
                0.55,
                0.60,
                0.62,
                0.68,
                0.72,
                0.76,
                0.80,
                0.84,
                0.88,
                0.91,
                0.94,
                0.97,
            ],
            "passed": [
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
        }
    )


def test_train_and_predict_classifier():
    df = make_students()

    X = df[["age", "income", "attendance"]]
    y = df["passed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    model = train_classifier(X_train, y_train)

    predictions = make_predictions(model, X_test)

    assert len(predictions) == len(y_test)

    accuracy = evaluate_accuracy(y_test, predictions)

    assert 0.0 <= accuracy <= 1.0


def test_get_confusion_matrix():
    y_test = [1, 1, 1, 0, 0, 0]
    predictions = [1, 0, 1, 0, 1, 0]

    result = get_confusion_matrix(y_test, predictions)

    assert result.shape == (2, 2)
    assert result.tolist() == [
        [2, 1],
        [1, 2],
    ]


def test_evaluate_classifier():
    y_test = [1, 1, 1, 0, 0, 0]
    predictions = [1, 0, 1, 0, 1, 0]

    result = evaluate_classifier(y_test, predictions)

    assert result["accuracy"] == 4 / 6
    assert result["precision"] == 2 / 3
    assert result["recall"] == 2 / 3
