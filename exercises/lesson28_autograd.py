import torch


def scalar_gradient(x_value):
    x = torch.tensor(x_value, requires_grad=True)
    loss = x**2

    loss.backward()

    if x.grad is None:
        raise RuntimeError("Gradient was not calculated")

    return x.grad


def two_variable_gradients(x_value, y_value):
    x = torch.tensor(x_value, requires_grad=True)
    y = torch.tensor(y_value, requires_grad=True)

    loss = x**3 + 4 * x * y + 2 * y**2

    loss.backward()

    if x.grad is None or y.grad is None:
        raise RuntimeError("Gradient was not calculated")

    return (x.grad, y.grad)


def gradient_descent_step(x_value, y_value, learning_rate):
    x_grad, y_grad = two_variable_gradients(x_value, y_value)

    new_x = x_value - learning_rate * x_grad
    new_y = y_value - learning_rate * y_grad

    return (new_x, new_y)


def train_single_weight(
    x_value,
    y_value,
    initial_weight,
    learning_rate,
    steps,
):

    w = torch.tensor(initial_weight, requires_grad=True)

    for _ in range(steps):
        y_hat = x_value * w
        loss = (y_value - y_hat) ** 2
        loss.backward()

        if w.grad is None:
            raise RuntimeError("Gradient was not calculated")

        with torch.no_grad():
            w -= learning_rate * w.grad

        w.grad.zero_()

    return w


def linear_model_gradients(X, y):
    W = torch.zeros((2, 1), requires_grad=True)
    b = torch.zeros((1,), requires_grad=True)

    y_hat = X @ W + b
    loss = ((y_hat - y) ** 2).mean()

    loss.backward()

    if W.grad is None or b.grad is None:
        raise RuntimeError("Gradient was not calculated")

    return (W.grad, b.grad)


def train_linear_model(X, y, learning_rate, steps):
    W = torch.zeros((2, 1), requires_grad=True)
    b = torch.zeros((1,), requires_grad=True)

    for _ in range(steps):
        y_hat = X @ W + b
        loss = ((y_hat - y) ** 2).mean()

        loss.backward()

        if W.grad is None or b.grad is None:
            raise RuntimeError("Gradient was not calculated")

        with torch.no_grad():
            W -= learning_rate * W.grad
            b -= learning_rate * b.grad

        W.grad.zero_()
        b.grad.zero_()

    return (W, b)
