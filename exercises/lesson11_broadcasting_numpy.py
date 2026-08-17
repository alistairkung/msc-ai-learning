def center_features(features):
    feature_mean = features.mean(axis=0)
    centered_features = features - feature_mean

    return centered_features


def standardise_features(features):
    centered = center_features(features)
    stds = centered.std(axis=0)

    return centered / stds
