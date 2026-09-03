import numpy as np

from exercises.refresher_np import (
    add_row_offsets,
    center_features,
    column_means,
    passing_values,
    standardise_features,
)


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

    np.testing.assert_allclose(
        result,
        np.array([30, 40, 50]),
    )


def test_center_features():
    features = np.array(
        [
            [10, 100],
            [20, 200],
            [30, 300],
        ]
    )

    result = center_features(features)

    np.testing.assert_allclose(
        result.mean(axis=0),
        np.zeros(2),
        atol=1e-10,
    )


def test_standardise_features():
    features = np.array(
        [
            [10, 100],
            [20, 200],
            [30, 300],
            [40, 400],
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

    np.testing.assert_array_equal(
        result,
        np.array(
            [
                [11, 21, 31],
                [42, 52, 62],
                [73, 83, 93],
                [104, 114, 124],
            ]
        ),
    )
