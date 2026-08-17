import numpy as np


def class_scores(features, weights, biases):
    return features @ weights + biases


def predict_classes(features, weights, biases):
    classes = class_scores(features, weights, biases)
    predictions = np.argmax(classes, axis=1)

    return predictions


def classification_accuracy(features, weights, biases, actual):
    predictions = predict_classes(features, weights, biases)

    return (predictions == actual).mean()
