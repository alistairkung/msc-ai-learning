import numpy as np


def two_sum(numbers, target):
    seen = {}

    for index, number in enumerate(numbers):
        lookup = target - number

        if lookup in seen:
            return (seen[lookup], index)

        seen[number] = index

    return None


def max_sum_of_k(numbers, k):
    window_sum = sum(numbers[0:k])
    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum = window_sum - numbers[i - k] + numbers[i]
        max_sum = max(window_sum, max_sum)

    return max_sum


def standardise_features(features):
    means = features.mean(axis=0)
    centered = features - means
    std = centered.std(axis=0)

    return centered / std


def predict_classes(features, weights, biases):
    scores = features @ weights + biases

    return np.argmax(scores, axis=1)


def model_loss(features, weights, bias, actual):
    predictions = features @ weights + bias

    errors = actual - predictions
    squared_errors = errors**2
    mse = squared_errors.mean()

    return mse
