from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split


def run_regression_pipeline(houses):
    X = houses[["size", "bedrooms", "age"]]
    y = houses["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train)
    y_pred = predict(model, X_test)

    return {
        "model": model,
        "predictions": y_pred,
        "actual": y_test,
        "mae": mean_absolute_error(y_test, y_pred),
        "mse": mean_squared_error(y_test, y_pred),
        "r2": r2_score(y_test, y_pred),
    }


def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def predict(model, X_test):
    return model.predict(X_test)
