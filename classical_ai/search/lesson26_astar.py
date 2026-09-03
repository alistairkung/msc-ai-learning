import heapq


def astar_path(graph, heuristic, start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))

    cost_so_far = {start: 0}
    parent = {start: None}

    while frontier:
        _, current_state = heapq.heappop(frontier)

        if current_state == goal:
            state = goal
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()
            return path

        for neighbour, edge_cost in graph[current_state]:
            new_cost = cost_so_far[current_state] + edge_cost

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                parent[neighbour] = current_state

                priority = new_cost + heuristic[neighbour]
                heapq.heappush(frontier, (priority, neighbour))

    return None
