import numpy as np

from exercises.lesson13_cold_retrieval import (
    add_row_offsets,
    column_means,
    first_duplicate,
    is_palindrome,
    linear_layer,
    model_loss,
    passing_values,
    predict,
    standardise_features,
    two_sum,
)

# -------------------------
# Python / DSA retrieval
# -------------------------


def test_first_duplicate():
    numbers = [4, 7, 2, 9, 7, 4]

    assert first_duplicate(numbers) == 7


def test_first_duplicate_returns_none():
    numbers = [4, 7, 2, 9]

    assert first_duplicate(numbers) is None


def test_two_sum():
    numbers = [3, 8, 4, 7, 2]

    assert two_sum(numbers, 11) == (0, 1)


def test_two_sum_returns_none():
    numbers = [1, 2, 3]

    assert two_sum(numbers, 100) is None


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("python") is False


# -------------------------
# NumPy fundamentals
# -------------------------


def test_passing_values():
    values = np.array([42, 70, 51, 49, 90])

    result = passing_values(values, 50)

    np.testing.assert_array_equal(
        result,
        np.array([70, 51, 90]),
    )


def test_column_means():
    array = np.array(
        [
            [10, 20, 30],
            [30, 40, 50],
            [50, 60, 70],
        ]
    )

    result = column_means(array)

    np.testing.assert_array_equal(
        result,
        np.array([30.0, 40.0, 50.0]),
    )


def test_standardise_features():
    features = np.array(
        [
            [10, 100, 5],
            [20, 200, 15],
            [30, 300, 25],
            [40, 400, 35],
        ]
    )

    result = standardise_features(features)

    assert result.shape == features.shape

    np.testing.assert_allclose(
        result.mean(axis=0),
        np.zeros(3),
        atol=1e-10,
    )

    np.testing.assert_allclose(
        result.std(axis=0),
        np.ones(3),
        atol=1e-10,
    )


# -------------------------
# Broadcasting
# -------------------------


def test_add_row_offsets():
    matrix = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90],
            [100, 110, 120],
        ]
    )

    offsets = np.array([1, 2, 3, 4])

    result = add_row_offsets(matrix, offsets)

    expected = np.array(
        [
            [11, 21, 31],
            [42, 52, 62],
            [73, 83, 93],
            [104, 114, 124],
        ]
    )

    np.testing.assert_array_equal(result, expected)


# -------------------------
# Matrix multiplication / ML
# -------------------------


def test_predict():
    features = np.array(
        [
            [2, 3],
            [4, 5],
            [6, 7],
        ]
    )

    weights = np.array([10, 20])
    bias = 5

    result = predict(features, weights, bias)

    np.testing.assert_array_equal(
        result,
        np.array([85, 145, 205]),
    )


def test_linear_layer():
    inputs = np.array(
        [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
    )

    weights = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
        ]
    )

    biases = np.array([1, 2, 3])

    result = linear_layer(inputs, weights, biases)

    expected = np.array(
        [
            [91, 122, 153],
            [191, 262, 333],
            [291, 402, 513],
        ]
    )

    np.testing.assert_array_equal(result, expected)


def test_model_loss():
    features = np.array(
        [
            [2, 3],
            [4, 5],
            [6, 7],
        ]
    )

    weights = np.array([10, 20])
    bias = 5
    actual = np.array([80, 150, 200])

    result = model_loss(features, weights, bias, actual)

    assert result == 25
