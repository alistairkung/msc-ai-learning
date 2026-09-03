import torch
from torch import nn


def train_linear_model_with_sgd(X, y, learning_rate, steps):
    model = nn.Linear(in_features=2, out_features=1)
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    for _ in range(steps):
        optimizer.zero_grad()
        y_hat = model(X)
        loss = loss_fn(y_hat, y)

        loss.backward()

        optimizer.step()

    return model
