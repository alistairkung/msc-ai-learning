def passing_values(values, threshold):
    return values[values >= threshold]


def column_means(array):
    return array.mean(axis=0)


def center_features(features):
    means = features.mean(axis=0)
    return features - means


def standardise_features(features):
    means = features.mean(axis=0)
    centered = features - means
    std = centered.std(axis=0)

    return centered / std


def add_row_offsets(matrix, offsets):
    return matrix + offsets.reshape(-1, 1)
