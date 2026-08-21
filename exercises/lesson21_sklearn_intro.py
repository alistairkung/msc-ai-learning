from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)


def train_classifier(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model


def make_predictions(model, X_test):
    return model.predict(X_test)


def evaluate_accuracy(y_test, predictions):
    return (predictions == y_test).mean()

    # return accuracy_score(y_test, predictions)


def get_confusion_matrix(y_test, predictions):
    return confusion_matrix(y_test, predictions)


def evaluate_classifier(y_test, predictions):
    return {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
    }
