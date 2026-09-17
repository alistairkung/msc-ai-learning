"""Changed-example practice for AIMS5702 Assignment 1 preparation.

These functions deliberately mirror the *concepts* required by the assignment without
copying the assignment's exact functions or data. Implement them from the tests.

Learning boundary: do not use torch.matmul, torch.mm, the @ operator, or torch.dot.
"""

import torch


def dot_product(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Return the dot product of two 1D tensors using primitive tensor operations."""
    raise NotImplementedError


def pairwise_dot_loops(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Return all row-pair dot products using exactly two Python loops.

    x has shape (m, k), y has shape (n, k), and the result must have shape (m, n).
    """
    raise NotImplementedError


def pairwise_dot_broadcast(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Return all row-pair dot products using broadcasting and reduction, no loops.

    x has shape (m, k), y has shape (n, k), and the result must have shape (m, n).
    """
    raise NotImplementedError


def pairwise_dot_einsum(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Return all row-pair dot products using torch.einsum."""
    raise NotImplementedError
