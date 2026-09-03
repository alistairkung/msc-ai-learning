def first_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return number

        seen.add(number)

    return None


def two_sum(numbers, target):
    seen = {}

    for index, number in enumerate(numbers):
        lookup = target - number
        if lookup in seen:
            return (seen[lookup], index)

        seen[number] = index

    return None


def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


def passing_values(values, threshold):
    return values[values >= threshold]


def column_means(array):
    return array.mean(axis=0)


def standardise_features(features):
    means = features.mean(axis=0)
    centered = features - means
    stds = centered.std(axis=0)

    return centered / stds


def add_row_offsets(matrix, offsets):
    reshaped_offsets = offsets.reshape(-1, 1)
    return matrix + reshaped_offsets


def predict(features, weights, bias):
    return features @ weights + bias


def linear_layer(inputs, weights, biases):
    return inputs @ weights + biases


def model_loss(features, weights, bias, actual):
    predictions = predict(features, weights, bias)

    error_squared = (predictions - actual) ** 2
    mse = error_squared.mean()

    return mse
