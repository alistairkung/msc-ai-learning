import numpy as np

from lesson11_broadcasting_numpy import center_features, standardise_features


def test_center_features():
    features = np.array(
        [
            [10, 100, 1000],
            [20, 200, 2000],
            [30, 300, 3000],
            [40, 400, 4000],
        ]
    )

    result = center_features(features)

    expected = np.array(
        [
            [-15, -150, -1500],
            [-5, -50, -500],
            [5, 50, 500],
            [15, 150, 1500],
        ]
    )

    np.testing.assert_array_equal(result, expected)


def test_centered_features_have_mean_zero():
    features = np.array(
        [
            [10, 100, 1000],
            [20, 200, 2000],
            [30, 300, 3000],
            [40, 400, 4000],
        ]
    )

    result = center_features(features)

    np.testing.assert_allclose(
        result.mean(axis=0),
        np.array([0, 0, 0]),
    )


def test_standardise_features():
    features = np.array(
        [
            [10, 100, 1000],
            [20, 200, 2000],
            [30, 300, 3000],
            [40, 400, 4000],
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
