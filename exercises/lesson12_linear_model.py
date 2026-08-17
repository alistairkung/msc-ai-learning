def predict(features, weights, bias):
    return features @ weights + bias


def prediction_errors(predictions, actual):
    return predictions - actual


def squared_errors(predictions, actual):
    return (predictions - actual) ** 2


def mean_squared_error(predictions, actual):
    errors_squared = (predictions - actual) ** 2

    return errors_squared.mean()


def model_loss(features, weights, bias, actual):
    predictions = predict(features, weights, bias)

    return mean_squared_error(predictions, actual)


def linear_layer(inputs, weights, biases):
    return inputs @ weights + biases
