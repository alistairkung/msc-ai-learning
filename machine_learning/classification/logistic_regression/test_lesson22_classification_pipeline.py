import pandas as pd

from exercises.lesson22_classification_pipeline import (
    predict_with_threshold,
    run_classification_pipeline,
)


def make_dataset():
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
                44,
                46,
                48,
                50,
                52,
                54,
                56,
                58,
            ],
            "income": [
                25000,
                28000,
                30000,
                33000,
                36000,
                40000,
                43000,
                47000,
                50000,
                54000,
                58000,
                62000,
                66000,
                70000,
                74000,
                78000,
                82000,
                86000,
                90000,
                95000,
            ],
            "attendance": [
                0.55,
                0.58,
                0.61,
                0.64,
                0.67,
                0.70,
                0.73,
                0.76,
                0.79,
                0.82,
                0.84,
                0.86,
                0.88,
                0.90,
                0.91,
                0.93,
                0.94,
                0.95,
                0.96,
                0.98,
            ],
            "passed": [
                0,
                0,
                0,
                0,
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
                1,
                1,
                1,
                1,
            ],
        }
    )


def test_run_classification_pipeline_returns_expected_keys():
    df = make_dataset()

    result = run_classification_pipeline(df)

    assert set(result.keys()) == {
        "model",
        "predictions",
        "actual",
        "accuracy",
        "precision",
        "recall",
        "confusion_matrix",
    }


def test_run_classification_pipeline_uses_test_set():
    df = make_dataset()

    result = run_classification_pipeline(df)

    assert len(result["predictions"]) == 4
    assert len(result["actual"]) == 4


def test_run_classification_pipeline_metrics_are_valid():
    df = make_dataset()

    result = run_classification_pipeline(df)

    assert 0.0 <= result["accuracy"] <= 1.0
    assert 0.0 <= result["precision"] <= 1.0
    assert 0.0 <= result["recall"] <= 1.0


def test_run_classification_pipeline_confusion_matrix():
    df = make_dataset()

    result = run_classification_pipeline(df)

    assert result["confusion_matrix"].shape == (2, 2)


def test_run_classification_pipeline_model_is_fitted():
    df = make_dataset()

    result = run_classification_pipeline(df)

    model = result["model"]

    assert hasattr(model, "coef_")
    assert hasattr(model, "intercept_")


import numpy as np


def test_predict_with_threshold():
    class FakeModel:
        def predict_proba(self, X):
            return np.array(
                [
                    [0.90, 0.10],
                    [0.60, 0.40],
                    [0.45, 0.55],
                    [0.20, 0.80],
                ]
            )

    model = FakeModel()
    X_test = np.zeros((4, 2))

    result = predict_with_threshold(
        model,
        X_test,
        threshold=0.5,
    )

    np.testing.assert_array_equal(
        result,
        np.array([0, 0, 1, 1]),
    )


def test_lower_threshold_produces_more_positive_predictions():
    class FakeModel:
        def predict_proba(self, X):
            return np.array(
                [
                    [0.90, 0.10],
                    [0.60, 0.40],
                    [0.45, 0.55],
                    [0.20, 0.80],
                ]
            )

    model = FakeModel()
    X_test = np.zeros((4, 2))

    result = predict_with_threshold(
        model,
        X_test,
        threshold=0.3,
    )

    np.testing.assert_array_equal(
        result,
        np.array([0, 1, 1, 1]),
    )
