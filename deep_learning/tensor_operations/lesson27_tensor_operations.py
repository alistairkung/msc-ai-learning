def batch_mean(X):
    return X.mean(axis=0)


def center_features(X):
    means = batch_mean(X)
    return X - means


def flatten_samples(X):
    return X.reshape(X.shape[0], -1)


def swap_last_two_axes(X):
    return X.transpose(0, 2, 1)


def linear_layer(X, W, b):
    return X @ W + b
