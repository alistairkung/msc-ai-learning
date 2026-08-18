import numpy as np

from exercises.lesson17_retrieval import (
    max_sum_of_k,
    model_loss,
    predict_classes,
    standardise_features,
    two_sum,
)


def test_two_sum():
    numbers = [4, 9, 1, 6, 3]

    assert two_sum(numbers, 10) == (1, 2)


def test_two_sum_returns_none():
    numbers = [1, 2, 3]

    assert two_sum(numbers, 20) is None


def test_max_sum_of_k():
    numbers = [2, 1, 5, 1, 3, 2]

    assert max_sum_of_k(numbers, 3) == 9


def test_max_sum_of_k_with_different_window():
    numbers = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]

    assert max_sum_of_k(numbers, 3) == 16


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
