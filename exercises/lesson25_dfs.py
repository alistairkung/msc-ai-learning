from collections import deque


def dfs_path(graph, start, goal):
    queue = deque([start])
    seen = {start}
    parent = {start: None}

    while queue:
        current_state = queue.pop()

        if current_state == goal:
            traverse_state = goal
            path = []

            while traverse_state is not None:
                path.append(traverse_state)
                traverse_state = parent[traverse_state]

            path.reverse()
            return path

        neighbours = graph[current_state]

        for neighbour in neighbours:
            if neighbour not in seen:
                seen.add(neighbour)
                parent[neighbour] = current_state
                queue.append(neighbour)

    return None
