from exercises.lesson24_bfs import bfs_path


def test_bfs_path():
    graph = {
        "A": ["C"],
        "B": ["E"],
        "C": ["B", "D", "F"],
        "D": [],
        "E": [],
        "F": ["G"],
        "G": [],
    }

    result = bfs_path(graph, "A", "G")

    assert result == ["A", "C", "F", "G"]


def test_bfs_path_returns_none_when_goal_unreachable():
    graph = {
        "A": ["B"],
        "B": [],
        "C": [],
    }

    result = bfs_path(graph, "A", "C")

    assert result is None


def test_bfs_returns_start_when_start_is_goal():
    graph = {
        "A": ["B"],
        "B": [],
    }

    result = bfs_path(graph, "A", "A")

    assert result == ["A"]
