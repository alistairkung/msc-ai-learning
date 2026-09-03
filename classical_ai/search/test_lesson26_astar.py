from lesson26_astar import astar_path


def test_astar_finds_lowest_cost_path():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2), ("G", 10)],
        "C": [("G", 3)],
        "D": [("G", 2)],
        "G": [],
    }

    heuristic = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "G": 0,
    }

    result = astar_path(graph, heuristic, "A", "G")

    assert result == ["A", "B", "D", "G"]


def test_astar_returns_none_when_unreachable():
    graph = {
        "A": [("B", 1)],
        "B": [],
        "G": [],
    }

    heuristic = {
        "A": 2,
        "B": 1,
        "G": 0,
    }

    assert astar_path(graph, heuristic, "A", "G") is None
