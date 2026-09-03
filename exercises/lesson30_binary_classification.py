import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def train_classifier(X, y, batch_size, learning_rate, epochs):
    model = make_classifier()
    loader = make_dataloader(X, y, batch_size)

    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        for X_batch, y_batch in loader:
            optimizer.zero_grad()

            logits = model(X_batch)
            loss = loss_fn(logits, y_batch)

            loss.backward()

            optimizer.step()

    return model


def classification_accuracy(model, X, y):
    with torch.no_grad():
        logits = model(X)
        probabilities = torch.sigmoid(logits)
        predictions = (probabilities >= 0.5).float()
        accuracy = (predictions == y).float().mean()

    return accuracy


def make_dataloader(X, y, batch_size):
    dataset = TensorDataset(X, y)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)


def make_classifier():
    model = nn.Sequential(
        nn.Linear(in_features=10, out_features=6),
        nn.ReLU(),
        nn.Linear(in_features=6, out_features=1),
    )

    return model
