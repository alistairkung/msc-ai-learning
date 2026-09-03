from exercises.lesson25_dfs import dfs_path


def test_dfs_path():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["G"],
        "D": ["E"],
        "E": ["G"],
        "G": [],
    }

    result = dfs_path(graph, "A", "G")

    assert result is not None
    assert result[0] == "A"
    assert result[-1] == "G"


def test_dfs_returns_none_when_goal_unreachable():
    graph = {
        "A": ["B"],
        "B": [],
        "C": [],
    }

    assert dfs_path(graph, "A", "C") is None


def test_dfs_returns_start_when_start_is_goal():
    graph = {
        "A": ["B"],
        "B": [],
    }

    assert dfs_path(graph, "A", "A") == ["A"]
