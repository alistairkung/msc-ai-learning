import torch

from lesson30_binary_classification import (
    classification_accuracy,
    make_classifier,
    make_dataloader,
    train_classifier,
)


def test_classifier_can_learn_simple_pattern():
    torch.manual_seed(42)

    X = torch.randn(1000, 10)

    # Simple rule:
    # class 1 if feature 0 + feature 1 > 0
    y = ((X[:, 0] + X[:, 1]) > 0).float().reshape(-1, 1)

    model = train_classifier(
        X,
        y,
        batch_size=32,
        learning_rate=0.1,
        epochs=10,
    )

    accuracy = classification_accuracy(model, X, y)

    assert accuracy > 0.90


def test_make_dataloader():
    X = torch.randn(100, 10)
    y = torch.randint(0, 2, (100, 1)).float()

    loader = make_dataloader(X, y, batch_size=32)

    X_batch, y_batch = next(iter(loader))

    assert X_batch.shape == (32, 10)
    assert y_batch.shape == (32, 1)


def test_make_classifier():
    model = make_classifier()
    X = torch.randn(32, 10)

    logits = model(X)

    assert logits.shape == (32, 1)
