import numpy as np

from lesson27_tensor_operations import (
    batch_mean,
    center_features,
    flatten_samples,
    linear_layer,
    swap_last_two_axes,
)


def test_batch_mean():
    X = np.array(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
            [[9, 10], [11, 12]],
        ]
    )

    result = batch_mean(X)

    expected = np.array(
        [
            [5, 6],
            [7, 8],
        ]
    )

    np.testing.assert_array_equal(result, expected)
    assert result.shape == (2, 2)


def test_center_features():
    X = np.array(
        [
            [1.0, 10.0],
            [3.0, 20.0],
            [5.0, 30.0],
        ]
    )

    result = center_features(X)

    expected = np.array(
        [
            [-2.0, -10.0],
            [0.0, 0.0],
            [2.0, 10.0],
        ]
    )

    np.testing.assert_array_equal(result, expected)
    assert result.shape == (3, 2)


def test_flatten_samples():
    X = np.arange(24).reshape(2, 3, 4)

    result = flatten_samples(X)

    assert result.shape == (2, 12)

    np.testing.assert_array_equal(
        result[0],
        np.arange(12),
    )


def test_flatten_samples_works_in_any_dimension():
    X = np.arange(24).reshape(3, 2, 4)

    result = flatten_samples(X)

    assert result.shape == (3, 8)

    np.testing.assert_array_equal(
        result[0],
        np.arange(8),
    )


def test_swap_last_two_axes():
    X = np.arange(24).reshape(2, 3, 4)

    result = swap_last_two_axes(X)

    assert result.shape == (2, 4, 3)

    assert result[0, 0, 0] == X[0, 0, 0]
    assert result[0, 1, 2] == X[0, 2, 1]


def test_linear_layer():
    X = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
        ]
    )

    W = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [1.0, 1.0],
        ]
    )

    b = np.array([10.0, 20.0])

    result = linear_layer(X, W, b)

    expected = np.array(
        [
            [14.0, 25.0],
            [20.0, 31.0],
        ]
    )

    np.testing.assert_array_equal(result, expected)
    assert result.shape == (2, 2)
