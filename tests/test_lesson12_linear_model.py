import numpy as np

from exercises.lesson12_linear_model import (
    linear_layer,
    mean_squared_error,
    model_loss,
    predict,
    predicted_classes,
    prediction_errors,
    squared_errors,
)


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


def test_prediction_errors():
    predictions = np.array([85, 145, 205])
    actual = np.array([80, 150, 200])

    result = prediction_errors(predictions, actual)

    np.testing.assert_array_equal(
        result,
        np.array([5, -5, 5]),
    )


def test_squared_errors():
    predictions = np.array([85, 145, 205])
    actual = np.array([80, 150, 200])

    result = squared_errors(predictions, actual)

    np.testing.assert_array_equal(
        result,
        np.array([25, 25, 25]),
    )


def test_mean_squared_error():
    predictions = np.array([85, 145, 205])
    actual = np.array([80, 150, 200])

    assert mean_squared_error(predictions, actual) == 25


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


def test_predicted_classes():
    scores = np.array(
        [
            [2.1, 5.7, 1.2],
            [8.4, 3.2, 4.1],
            [1.5, 2.8, 6.9],
            [4.2, 7.1, 5.3],
        ]
    )

    result = predicted_classes(scores)

    np.testing.assert_array_equal(
        result,
        np.array([1, 0, 2, 1]),
    )
