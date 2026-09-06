"""Practice exercise: reconstruct BFS without reading lesson24_bfs.py first.

This file is intentionally skipped at module level so it never blocks the normal
pytest/CI pipeline. When practising, temporarily remove/comment the pytestmark
line (or copy the cases into a scratch test file) and implement `bfs` below.
"""

import pytest

pytestmark = pytest.mark.skip(reason="Practice-only BFS reconstruction exercise; skipped in CI")


def bfs(graph, start, goal):
    """Return a BFS path from start to goal, or None when goal is unreachable.

    Practice constraints:
    - Implement this yourself before looking at lesson24_bfs.py.
    - Use breadth-first frontier behaviour.
    - Avoid revisiting already discovered nodes.
    - Reconstruct and return the path, including both start and goal.
    """
    raise NotImplementedError("Practice: implement BFS")


@pytest.fixture
def graph():
    return {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": ["G"],
        "G": [],
        "X": [],
    }


def test_bfs_finds_expected_shortest_path(graph):
    assert bfs(graph, "A", "G") == ["A", "B", "E", "G"]


def test_bfs_returns_start_when_start_is_goal(graph):
    assert bfs(graph, "C", "C") == ["C"]


def test_bfs_returns_none_when_goal_is_unreachable(graph):
    assert bfs(graph, "A", "X") is None


def test_bfs_handles_cycle_without_looping_forever():
    cyclic_graph = {
        "A": ["B"],
        "B": ["C", "A"],
        "C": ["B", "G"],
        "G": [],
    }

    assert bfs(cyclic_graph, "A", "G") == ["A", "B", "C", "G"]


def test_bfs_prefers_fewer_edges_over_deeper_route():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "D": ["E"],
        "E": ["G"],
        "C": ["G"],
        "G": [],
    }

    assert bfs(graph, "A", "G") == ["A", "C", "G"]
