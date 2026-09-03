import numpy as np


def center_columns(features):
    means = features.mean(axis=0)
    return features - means


def standardise(features):
    centered = center_columns(features)
    std = centered.std(axis=0)

    return centered / std


def combine_feature_sets(first, second):
    return np.concatenate([first, second], axis=1)


def predict(features, weights, biases):
    scores = features @ weights + biases
    return scores


def best_class(scores):
    return scores.argmax(axis=1)


def count_correct(predictions, actual):
    return np.sum(predictions == actual)


def accuracy(predictions, actual):
    return (predictions == actual).mean()


def normalise_scores(scores):
    s = scores / 100
    return np.clip(s, 0, 1)


def confidence_margin(scores):
    sorted_scores = np.sort(scores, axis=1)
    largest = sorted_scores[:, -1]
    second_largest = sorted_scores[:, -2]

    return largest - second_largest
