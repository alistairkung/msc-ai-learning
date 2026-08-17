import numpy as np

from exercises.lesson14_classification_pipeline import (
    class_scores,
    classification_accuracy,
    predict_classes,
)


def test_class_scores():
    features = np.array(
        [
            [1, 2],
            [3, 1],
            [2, 4],
            [5, 2],
        ]
    )

    weights = np.array(
        [
            [2, 1, 0],
            [0, 1, 2],
        ]
    )

    biases = np.array([0, 1, 0])

    result = class_scores(features, weights, biases)

    expected = np.array(
        [
            [2, 4, 4],
            [6, 5, 2],
            [4, 7, 8],
            [10, 8, 4],
        ]
    )

    np.testing.assert_array_equal(result, expected)


def test_predict_classes():
    features = np.array(
        [
            [1, 2],
            [3, 1],
            [2, 4],
            [5, 2],
        ]
    )

    weights = np.array(
        [
            [2, 1, 0],
            [0, 1, 2],
        ]
    )

    biases = np.array([0, 1, 0])

    result = predict_classes(features, weights, biases)

    np.testing.assert_array_equal(
        result,
        np.array([1, 0, 2, 0]),
    )


def test_classification_accuracy():
    features = np.array(
        [
            [1, 2],
            [3, 1],
            [2, 4],
            [5, 2],
        ]
    )

    weights = np.array(
        [
            [2, 1, 0],
            [0, 1, 2],
        ]
    )

    biases = np.array([0, 1, 0])

    actual = np.array([1, 0, 1, 0])

    result = classification_accuracy(
        features,
        weights,
        biases,
        actual,
    )

    assert result == 0.75
