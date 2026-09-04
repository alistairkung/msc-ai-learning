from typing import Any

import torch
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def run_experiment(batch_size, learning_rate, epochs):
    train_loader, X_val, y_val, X_test, y_test = prepare_data(batch_size)

    model = make_classifier()
    train_losses, val_losses = train_classifier(
        model, train_loader, X_val, y_val, learning_rate, epochs
    )

    test_accuracy = classification_accuracy(model, X_test, y_test, threshold=0.5)

    return model, train_losses, val_losses, test_accuracy


def prepare_data(batch_size):
    X, y = load_data()
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)

    X_train_scaled, X_val_scaled, X_test_scaled = scale_data(X_train, X_val, X_test)

    X_train_tensor, y_train_tensor = to_tensors(X_train_scaled, y_train)
    X_val_tensor, y_val_tensor = to_tensors(X_val_scaled, y_val)
    X_test_tensor, y_test_tensor = to_tensors(X_test_scaled, y_test)

    train_loader = make_dataloader(X_train_tensor, y_train_tensor, batch_size)

    return train_loader, X_val_tensor, y_val_tensor, X_test_tensor, y_test_tensor


def classification_accuracy(model, X, y, threshold=0.5):
    with torch.no_grad():
        probabilities = torch.sigmoid(model(X))
        predictions = (probabilities >= threshold).float()
        accuracy = (predictions == y).float().mean()

        return accuracy


def train_classifier(model, train_loader, X_val, y_val, learning_rate, epochs):
    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    train_losses = []
    val_losses = []

    for epoch in range(epochs):
        total_train_losses = 0
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            logits = model(X_batch)
            loss = loss_fn(logits, y_batch)
            total_train_losses += loss.item()

            loss.backward()
            optimizer.step()

        train_losses.append(total_train_losses / len(train_loader))

        with torch.no_grad():
            val_logits = model(X_val)
            val_loss = loss_fn(val_logits, y_val)

            val_losses.append(val_loss.item())

    return train_losses, val_losses


def make_classifier():
    model = nn.Sequential(nn.Linear(30, 16), nn.ReLU(), nn.Linear(16, 1))
    return model


def load_data() -> tuple[Any, Any]:
    x, y = load_breast_cancer(return_X_y=True)

    return x, y


def split_data(X, y):
    X_train, X_remainder, y_train, y_remainder = train_test_split(
        X, y, test_size=0.4, stratify=y, random_state=42
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_remainder, y_remainder, test_size=0.5, stratify=y_remainder, random_state=42
    )

    return X_train, X_val, X_test, y_train, y_val, y_test


def scale_data(X_train, X_val, X_test):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_val_scaled, X_test_scaled


def to_tensors(X, y):
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)

    return X, y


def make_dataloader(X, y, batch_size):
    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    return loader
