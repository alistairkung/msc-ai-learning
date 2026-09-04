import numpy as np
import torch

from lesson31_real_data import (
    load_data,
    make_classifier,
    prepare_data,
    run_experiment,
    scale_data,
    split_data,
    to_tensors,
)


def test_run_experiment():
    epochs = 3

    model, train_losses, val_losses, test_accuracy = run_experiment(
        batch_size=32,
        learning_rate=0.01,
        epochs=epochs,
    )

    assert model(torch.randn(4, 30)).shape == (4, 1)
    assert len(train_losses) == epochs
    assert len(val_losses) == epochs
    assert all(np.isfinite(loss) for loss in train_losses)
    assert all(np.isfinite(loss) for loss in val_losses)
    assert 0.0 <= test_accuracy.item() <= 1.0


def test_prepare_data():
    train_loader, X_val, y_val, X_test, y_test = prepare_data(batch_size=32)

    assert len(train_loader.dataset) == 341
    assert X_val.shape == (114, 30)
    assert y_val.shape == (114, 1)
    assert X_test.shape == (114, 30)
    assert y_test.shape == (114, 1)


def test_make_classifier():
    model = make_classifier()
    X = torch.randn(32, 30)

    logits = model(X)

    assert logits.shape == (32, 1)


def test_load_data():
    x, y = load_data()

    assert x.shape == (569, 30)
    assert y.shape == (569,)


def test_split_data():
    x, y = load_data()
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(x, y)

    assert X_train.shape == (341, 30)
    assert X_val.shape == (114, 30)
    assert X_test.shape == (114, 30)
    assert y_train.shape == (341,)
    assert y_val.shape == (114,)
    assert y_test.shape == (114,)


def test_scale_data():
    x, y = load_data()
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(x, y)

    X_train_scaled, X_val_scaled, X_test_scaled = scale_data(X_train, X_val, X_test)

    assert np.allclose(X_train_scaled.mean(axis=0), 0, atol=1e-7)
    assert np.allclose(X_train_scaled.std(axis=0), 1, atol=1e-7)


def test_to_tensors():
    x, y = load_data()
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(x, y)

    X_train_scaled, X_val_scaled, X_test_scaled = scale_data(X_train, X_val, X_test)
    X_tensor, y_tensor = to_tensors(X_train_scaled, y_train)

    assert X_tensor.shape == (341, 30)
    assert y_tensor.shape == (341, 1)
    assert X_tensor.dtype == torch.float32
    assert y_tensor.dtype == torch.float32
