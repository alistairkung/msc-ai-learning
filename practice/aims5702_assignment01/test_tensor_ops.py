"""Red test suite for changed-example AIMS5702 tensor practice.

Work through these sequentially. The tests specify behaviour; the implementation is
intentionally left to the learner.
"""

import inspect

import pytest
import torch

from practice.aims5702_assignment01.tensor_ops import (
    dot_product,
    pairwise_dot_broadcast,
    pairwise_dot_einsum,
    pairwise_dot_loops,
)


@pytest.fixture
def small_pairwise_case():
    x = torch.tensor(
        [
            [2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0],
        ]
    )
    y = torch.tensor(
        [
            [5.0, 6.0, 7.0],
            [2.0, 1.0, 0.0],
            [3.0, 3.0, 3.0],
            [-1.0, 2.0, 1.0],
        ]
    )
    expected = torch.tensor(
        [
            [56.0, 7.0, 27.0, 8.0],
            [38.0, 4.0, 18.0, 6.0],
        ]
    )
    return x, y, expected


def test_dot_product_multiplies_then_reduces_features():
    x = torch.tensor([2.0, 3.0, 4.0])
    y = torch.tensor([5.0, 6.0, 7.0])

    result = dot_product(x, y)

    assert result.shape == torch.Size([])
    assert result.item() == pytest.approx(56.0)


def test_pairwise_loops_matches_known_values_and_shape(small_pairwise_case):
    x, y, expected = small_pairwise_case

    result = pairwise_dot_loops(x, y)

    assert result.shape == (2, 4)
    assert torch.allclose(result, expected)


def test_pairwise_loops_transfers_to_different_dimensions():
    x = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])  # (3, 2)
    y = torch.tensor([[2.0, 0.0], [0.0, 2.0], [1.0, 1.0], [-1.0, 1.0]])  # (4, 2)
    expected = torch.tensor(
        [
            [2.0, 4.0, 3.0, 1.0],
            [6.0, 8.0, 7.0, 1.0],
            [10.0, 12.0, 11.0, 1.0],
        ]
    )

    result = pairwise_dot_loops(x, y)

    assert result.shape == (3, 4)
    assert torch.allclose(result, expected)


def test_pairwise_broadcast_matches_loop_contract(small_pairwise_case):
    x, y, expected = small_pairwise_case

    result = pairwise_dot_broadcast(x, y)

    assert result.shape == (2, 4)
    assert torch.allclose(result, expected)


def test_pairwise_broadcast_handles_single_row_without_special_case():
    x = torch.tensor([[1.0, -1.0, 2.0, 0.5]])  # (1, 4)
    y = torch.tensor(
        [
            [2.0, 3.0, 1.0, 4.0],
            [0.0, -2.0, 5.0, 2.0],
            [1.0, 1.0, 1.0, 1.0],
        ]
    )  # (3, 4)
    expected = torch.tensor([[3.0, 13.0, 2.5]])

    result = pairwise_dot_broadcast(x, y)

    assert result.shape == (1, 3)
    assert torch.allclose(result, expected)


def test_pairwise_einsum_matches_same_contract(small_pairwise_case):
    x, y, expected = small_pairwise_case

    result = pairwise_dot_einsum(x, y)

    assert result.shape == (2, 4)
    assert torch.allclose(result, expected)


def test_all_three_pairwise_representations_agree_on_changed_case():
    x = torch.tensor(
        [
            [1.0, 0.0, 2.0, -1.0, 3.0],
            [2.0, 1.0, 0.0, 4.0, -2.0],
            [0.5, 1.5, -1.0, 2.0, 1.0],
        ]
    )  # (3, 5)
    y = torch.tensor(
        [
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [-1.0, 0.0, 1.0, 0.0, -1.0],
        ]
    )  # (2, 5)

    loops = pairwise_dot_loops(x, y)
    broadcast = pairwise_dot_broadcast(x, y)
    einsum = pairwise_dot_einsum(x, y)

    assert loops.shape == broadcast.shape == einsum.shape == (3, 2)
    assert torch.allclose(loops, broadcast)
    assert torch.allclose(loops, einsum)


def test_practice_functions_do_not_use_forbidden_matrix_shortcuts():
    """Keep this practice aligned with the assignment's primitive-op constraint."""
    functions = [
        dot_product,
        pairwise_dot_loops,
        pairwise_dot_broadcast,
        pairwise_dot_einsum,
    ]
    forbidden_tokens = ("torch.matmul", "torch.mm", "torch.dot", " @ ")

    for function in functions:
        source = inspect.getsource(function)
        for token in forbidden_tokens:
            assert token not in source, f"{function.__name__} uses forbidden shortcut {token!r}"
