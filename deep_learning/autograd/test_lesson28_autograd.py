import torch

from exercises.lesson28_autograd import (
    gradient_descent_step,
    linear_model_gradients,
    scalar_gradient,
    train_linear_model,
    train_single_weight,
    two_variable_gradients,
)


def test_scalar_gradient():
    result = scalar_gradient(3.0)

    assert result == 6.0


def test_two_variable_gradients():
    dx, dy = two_variable_gradients(2.0, 3.0)

    assert dx == 24.0
    assert dy == 20.0


def test_gradient_descent_step():
    new_x, new_y = gradient_descent_step(
        x_value=2.0,
        y_value=3.0,
        learning_rate=0.01,
    )

    assert abs(new_x - 1.76) < 1e-6
    assert abs(new_y - 2.8) < 1e-6


def test_train_single_weight():
    result = train_single_weight(
        x_value=3.0,
        y_value=6.0,
        initial_weight=1.0,
        learning_rate=0.01,
        steps=100,
    )

    assert abs(result - 2.0) < 0.01


def test_linear_model_gradients():
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

    W_grad, b_grad = linear_model_gradients(X, y)

    assert W_grad.shape == (2, 1)
    assert b_grad.shape == (1,)


def test_train_linear_model_reduces_loss():
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

    W, b = train_linear_model(
        X,
        y,
        learning_rate=0.01,
        steps=100,
    )

    y_hat = X @ W + b
    loss = ((y_hat - y) ** 2).mean()
    assert loss.item() < 0.01
