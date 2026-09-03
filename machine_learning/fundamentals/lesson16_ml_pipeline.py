import numpy as np


def prepare_features(features):
    means = features.mean(axis=0)
    centered = features - means
    std = centered.std(axis=0)

    return centered / std


def run_model(features, weights, biases):
    return features @ weights + biases


def predict_classes(scores):
    return np.argmax(scores, axis=1)


def classification_accuracy(predictions, actual):
    return (predictions == actual).mean()


def evaluate_model(features, weights, biases, actual):
    prepared = prepare_features(features)
    scores = run_model(prepared, weights, biases)
    predicted = predict_classes(scores)

    return classification_accuracy(predicted, actual)
