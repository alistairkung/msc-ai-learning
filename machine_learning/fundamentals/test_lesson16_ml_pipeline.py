import numpy as np

from lesson16_ml_pipeline import (
    classification_accuracy,
    evaluate_model,
    predict_classes,
    prepare_features,
    run_model,
)


def test_prepare_features():
    features = np.array(
        [
            [20.0, 30000.0, 2.0],
            [30.0, 50000.0, 4.0],
            [40.0, 70000.0, 6.0],
            [50.0, 90000.0, 8.0],
        ]
    )

    result = prepare_features(features)

    assert result.shape == (4, 3)

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


def test_run_model():
    features = np.array(
        [
            [-1.0, 0.5, 2.0],
            [0.0, 1.0, -1.0],
            [1.0, -0.5, 0.5],
            [2.0, 1.5, 1.0],
        ]
    )

    weights = np.array(
        [
            [2.0, -1.0, 0.5],
            [1.0, 2.0, -1.0],
            [-1.0, 0.5, 2.0],
        ]
    )

    biases = np.array([0.5, -0.5, 1.0])

    result = run_model(features, weights, biases)

    expected = np.array(
        [
            [-3.0, 2.5, 4.0],
            [2.5, 1.0, -2.0],
            [1.5, -2.25, 3.0],
            [5.0, 1.0, 2.5],
        ]
    )

    np.testing.assert_allclose(result, expected)


def test_predict_classes():
    scores = np.array(
        [
            [-3.0, 2.5, 4.0],
            [2.5, 1.0, -2.0],
            [1.5, -2.25, 2.0],
            [5.0, 1.0, 2.5],
        ]
    )

    result = predict_classes(scores)

    np.testing.assert_array_equal(
        result,
        np.array([2, 0, 2, 0]),
    )


def test_classification_accuracy():
    predictions = np.array([2, 0, 2, 0])
    actual = np.array([2, 1, 2, 0])

    result = classification_accuracy(predictions, actual)

    assert result == 0.75


def test_evaluate_model():
    features = np.array(
        [
            [10.0, 100.0],
            [20.0, 200.0],
            [30.0, 300.0],
            [40.0, 400.0],
        ]
    )

    weights = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ]
    )

    biases = np.array([0.0, 0.0])
    actual = np.array([0, 0, 1, 1])

    prepared = prepare_features(features)
    scores = run_model(prepared, weights, biases)
    predictions = predict_classes(scores)
    expected = classification_accuracy(predictions, actual)

    assert expected == evaluate_model(features, weights, biases, actual)
