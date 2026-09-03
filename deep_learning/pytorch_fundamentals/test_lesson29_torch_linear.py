import torch

from lesson29_torch_linear import train_linear_model_with_sgd


def test_train_linear_model_with_sgd():
    X = torch.tensor(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    y = torch.tensor(
        [
            [5.0],
            [11.0],
        ]
    )

    model = train_linear_model_with_sgd(
        X,
        y,
        learning_rate=0.01,
        steps=1000,
    )

    predictions = model(X)
    loss = ((predictions - y) ** 2).mean()

    assert loss.item() < 0.01
