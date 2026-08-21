from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


def predict_with_threshold(model, X_test, threshold):
    probabilities = model.predict_proba(X_test)
    class_1_prob = probabilities[:, 1]

    return (class_1_prob >= threshold).astype(int)


def run_classification_pipeline(df):
    X = df[["age", "income", "attendance"]]
    y = df["passed"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = train_model(X_train, y_train)
    predictions = predict_model(model, X_test)
    evaluation = evaluate_model(y_test, predictions)

    output = {
        "model": model,
        "predictions": predictions,
        "actual": y_test,
    }

    return output | evaluation


def train_model(X_train, y_train):
    model = LogisticRegression()
    return model.fit(X_train, y_train)


def predict_model(model, X_test):
    return model.predict(X_test)


def evaluate_model(y_test, predictions):
    return {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
        "confusion_matrix": confusion_matrix(y_test, predictions),
    }
