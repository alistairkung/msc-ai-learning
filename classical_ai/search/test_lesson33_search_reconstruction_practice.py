"""Practice exercises: reconstruct BFS and DFS without reading the lesson implementations first.

This file is intentionally skipped at module level so it never blocks the normal
pytest/CI pipeline. When practising, temporarily remove/comment the pytestmark
line (or copy the cases into a scratch test file) and implement the target
function below.
"""

from collections import deque
import heapq

import pytest

# pytestmark = pytest.mark.skip(
#     reason="Practice-only search reconstruction exercises; skipped in CI"
# )


def bfs(graph, start, goal):
    """Return a BFS path from start to goal, or None when goal is unreachable.

    Practice constraints:
    - Implement this yourself before looking at lesson24_bfs.py.
    - Use breadth-first frontier behaviour.
    - Avoid revisiting already discovered nodes.
    - Reconstruct and return the path, including both start and goal.
    """
    frontier = deque([start])
    parents = {start: None}

    while frontier:
        current = frontier.popleft()

        if current == goal:
            next = current
            path = []
            while next is not None:
                path.append(next)
                next = parents[next]

            path.reverse()
            return path

        neighbours = graph[current]
        for node in neighbours:
            if node not in parents:
                parents[node] = current
                frontier.append(node)

    return None


def dfs(graph, start, goal):
    """Return a DFS path from start to goal, or None when goal is unreachable.

    Practice constraints:
    - Implement this yourself before looking at lesson25_dfs.py.
    - Use depth-first frontier behaviour.
    - Avoid revisiting already discovered nodes.
    - Reconstruct and return the path, including both start and goal.
    """
    parents = {start: None}
    frontier = deque([start])

    while frontier:
        current = frontier.pop()

        # reconstruct if current is goal
        if current == goal:
            next_node = current
            path = []

            while next_node is not None:
                path.append(next_node)
                next_node = parents[next_node]

            path.reverse()
            return path

        # inspect neighbours unless already seen
        neighbours = graph[current]
        for node in neighbours:
            if node not in parents:
                frontier.append(node)
                parents[node] = current

    return None


def ucs(graph, start, goal):
    frontier = [(0, start)]
    cost_so_far = {start: 0}
    parents = {start: None}

    while frontier:
        current_cost, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            next_node = current
            while next_node is not None:
                path.append(next_node)
                next_node = parents[next_node]

            path.reverse()

            return (path, current_cost)

        for node, edge_cost in graph[current]:
            new_cost = current_cost + edge_cost

            if node not in parents or new_cost < cost_so_far[node]:
                heapq.heappush(frontier, (new_cost, node))
                cost_so_far[node] = new_cost
                parents[node] = current

    return None


def astar(graph, heuristic, start, goal):
    frontier = [(heuristic[start], 0, start)]
    parents = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _current_priority, current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            next_node = current_node
            while next_node is not None:
                path.append(next_node)
                next_node = parents[next_node]

            path.reverse()

            return (path, current_cost)

        for neighbour_node, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost

            if (
                neighbour_node not in cost_so_far
                or new_cost < cost_so_far[neighbour_node]
            ):
                priority = new_cost + heuristic[neighbour_node]
                heapq.heappush(frontier, (priority, new_cost, neighbour_node))
                cost_so_far[neighbour_node] = new_cost
                parents[neighbour_node] = current_node

    return None


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


# ---------------------------------------------------------------------------
# BFS
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# DFS
# ---------------------------------------------------------------------------


def test_dfs_follows_lifo_branch_order(graph):
    assert dfs(graph, "A", "G") == ["A", "C", "F", "G"]


def test_dfs_returns_start_when_start_is_goal(graph):
    assert dfs(graph, "C", "C") == ["C"]


def test_dfs_returns_none_when_goal_is_unreachable(graph):
    assert dfs(graph, "A", "X") is None


def test_dfs_handles_cycle_without_looping_forever():
    cyclic_graph = {
        "A": ["B"],
        "B": ["C", "A"],
        "C": ["B", "G"],
        "G": [],
    }

    assert dfs(cyclic_graph, "A", "G") == ["A", "B", "C", "G"]


def test_dfs_can_choose_deeper_route_over_shorter_route():
    graph = {
        "A": ["C", "B"],
        "B": ["D"],
        "D": ["E"],
        "E": ["G"],
        "C": ["G"],
        "G": [],
    }

    assert dfs(graph, "A", "G") == ["A", "B", "D", "E", "G"]


# ---------------------------------------------------------------------------
# UCS
# ---------------------------------------------------------------------------


def test_ucs_finds_lowest_cost_path():
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("G", 2)],
        "C": [("D", 1)],
        "D": [("B", 1), ("G", 10)],
        "G": [],
    }

    assert ucs(graph, "A", "G") == (
        ["A", "C", "D", "B", "G"],
        5,
    )


def test_ucs_returns_start_when_start_is_goal():
    graph = {
        "A": [("B", 3)],
        "B": [],
    }

    assert ucs(graph, "A", "A") == (["A"], 0)


def test_ucs_returns_none_when_goal_is_unreachable():
    graph = {
        "A": [("B", 2)],
        "B": [],
        "X": [],
    }

    assert ucs(graph, "A", "X") is None


def test_ucs_updates_node_when_cheaper_path_is_found():
    graph = {
        "A": [("B", 10), ("C", 2)],
        "B": [("G", 1)],
        "C": [("B", 3)],
        "G": [],
    }

    assert ucs(graph, "A", "G") == (
        ["A", "C", "B", "G"],
        6,
    )


def test_ucs_prefers_lower_cost_over_fewer_edges():
    graph = {
        "A": [("B", 8), ("C", 2)],
        "B": [("G", 1)],
        "C": [("D", 2)],
        "D": [("E", 2)],
        "E": [("G", 1)],
        "G": [],
    }

    assert ucs(graph, "A", "G") == (
        ["A", "C", "D", "E", "G"],
        7,
    )


# ---------------------------------------------------------------------------
# A*
# ---------------------------------------------------------------------------


def test_astar_finds_lowest_cost_path():
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("G", 2)],
        "C": [("D", 1)],
        "D": [("B", 1), ("G", 10)],
        "G": [],
    }

    heuristic = {
        "A": 4,
        "B": 1,
        "C": 3,
        "D": 2,
        "G": 0,
    }

    assert astar(graph, heuristic, "A", "G") == (
        ["A", "C", "D", "B", "G"],
        5,
    )


def test_astar_returns_start_when_start_is_goal():
    graph = {
        "A": [("B", 3)],
        "B": [],
    }

    heuristic = {
        "A": 0,
        "B": 0,
    }

    assert astar(graph, heuristic, "A", "A") == (["A"], 0)


def test_astar_returns_none_when_goal_is_unreachable():
    graph = {
        "A": [("B", 2)],
        "B": [],
        "X": [],
    }

    heuristic = {
        "A": 2,
        "B": 1,
        "X": 0,
    }

    assert astar(graph, heuristic, "A", "X") is None


def test_astar_updates_node_when_cheaper_path_is_found():
    graph = {
        "A": [("B", 10), ("C", 2)],
        "B": [("G", 1)],
        "C": [("B", 3)],
        "G": [],
    }

    heuristic = {
        "A": 4,
        "B": 1,
        "C": 3,
        "G": 0,
    }

    assert astar(graph, heuristic, "A", "G") == (
        ["A", "C", "B", "G"],
        6,
    )


def test_astar_uses_heuristic_to_prioritise_frontier():
    graph = {
        "A": [("B", 2), ("C", 2)],
        "B": [("G", 5)],
        "C": [("D", 1)],
        "D": [("G", 1)],
        "G": [],
    }

    heuristic = {
        "A": 4,
        "B": 5,
        "C": 2,
        "D": 1,
        "G": 0,
    }

    assert astar(graph, heuristic, "A", "G") == (
        ["A", "C", "D", "G"],
        4,
    )


def test_astar_with_zero_heuristic_behaves_like_ucs():
    graph = {
        "A": [("B", 8), ("C", 2)],
        "B": [("G", 1)],
        "C": [("D", 2)],
        "D": [("E", 2)],
        "E": [("G", 1)],
        "G": [],
    }

    heuristic = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "G": 0,
    }

    assert astar(graph, heuristic, "A", "G") == (
        ["A", "C", "D", "E", "G"],
        7,
    )
