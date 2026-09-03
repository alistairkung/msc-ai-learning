import numpy as np

from lesson15_numpy_challenge import (
    accuracy,
    best_class,
    center_columns,
    combine_feature_sets,
    confidence_margin,
    count_correct,
    normalise_scores,
    predict,
    standardise,
)


def test_center_columns():
    features = np.array(
        [
            [10.0, 100.0, 5.0],
            [20.0, 200.0, 15.0],
            [30.0, 300.0, 25.0],
            [40.0, 400.0, 35.0],
        ]
    )

    result = center_columns(features)

    expected = np.array(
        [
            [-15.0, -150.0, -15.0],
            [-5.0, -50.0, -5.0],
            [5.0, 50.0, 5.0],
            [15.0, 150.0, 15.0],
        ]
    )

    np.testing.assert_array_equal(result, expected)


def test_standardise():
    features = np.array(
        [
            [10.0, 100.0],
            [20.0, 200.0],
            [30.0, 300.0],
            [40.0, 400.0],
        ]
    )

    result = standardise(features)

    assert result.shape == (4, 2)

    np.testing.assert_allclose(
        result.mean(axis=0),
        np.array([0.0, 0.0]),
        atol=1e-10,
    )

    np.testing.assert_allclose(
        result.std(axis=0),
        np.array([1.0, 1.0]),
        atol=1e-10,
    )


def test_combine_feature_sets():
    physical_features = np.array(
        [
            [170, 70],
            [180, 85],
            [160, 55],
        ]
    )

    financial_features = np.array(
        [
            [50000, 2000],
            [80000, 5000],
            [40000, 1000],
        ]
    )

    result = combine_feature_sets(
        physical_features,
        financial_features,
    )

    expected = np.array(
        [
            [170, 70, 50000, 2000],
            [180, 85, 80000, 5000],
            [160, 55, 40000, 1000],
        ]
    )

    np.testing.assert_array_equal(result, expected)


def test_predict():
    features = np.array(
        [
            [1.0, 2.0],
            [3.0, 1.0],
            [2.0, 4.0],
            [5.0, 2.0],
        ]
    )

    weights = np.array(
        [
            [2.0, 1.0, 0.0],
            [0.0, 1.0, 2.0],
        ]
    )

    biases = np.array([0.0, 1.0, 0.0])

    result = predict(features, weights, biases)

    expected = np.array(
        [
            [2.0, 4.0, 4.0],
            [6.0, 5.0, 2.0],
            [4.0, 7.0, 8.0],
            [10.0, 8.0, 4.0],
        ]
    )

    np.testing.assert_array_equal(result, expected)


def test_best_class():
    scores = np.array(
        [
            [2.0, 4.0, 4.0],
            [6.0, 5.0, 2.0],
            [4.0, 7.0, 8.0],
            [10.0, 8.0, 4.0],
        ]
    )

    result = best_class(scores)

    np.testing.assert_array_equal(
        result,
        np.array([1, 0, 2, 0]),
    )


def test_count_correct():
    predictions = np.array([1, 0, 2, 0, 1])
    actual = np.array([1, 2, 2, 0, 0])

    result = count_correct(predictions, actual)

    assert result == 3


def test_accuracy():
    predictions = np.array([1, 0, 2, 0, 1])
    actual = np.array([1, 2, 2, 0, 0])

    result = accuracy(predictions, actual)

    assert result == 0.6


def test_normalise_scores():
    scores = np.array(
        [
            [-20.0, 50.0, 120.0],
            [30.0, 80.0, 90.0],
        ]
    )

    result = normalise_scores(scores)

    expected = np.array(
        [
            [0.0, 0.5, 1.0],
            [0.3, 0.8, 0.9],
        ]
    )

    np.testing.assert_allclose(result, expected)


def test_confidence_margin():
    scores = np.array(
        [
            [2.0, 8.0, 5.0],
            [9.0, 3.0, 4.0],
            [1.0, 6.0, 5.0],
        ]
    )

    result = confidence_margin(scores)

    np.testing.assert_array_equal(
        result,
        np.array([3.0, 5.0, 1.0]),
    )
