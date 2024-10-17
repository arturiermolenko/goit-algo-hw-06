from collections import deque


def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path + [neighbor])
            if new_path:
                return new_path
    return None


def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    visited = set()
    path = {node: [] for node in graph.nodes}

    while visited != graph.nodes:
        unvisited_nodes = {
            node
            for node in distances
            if node not in visited and distances[node] != float("infinity")
        }

        if not unvisited_nodes:
            break

        current_node = min(unvisited_nodes, key=distances.get)
        visited.add(current_node)

        for neighbor, attributes in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + attributes["weight"]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    path[neighbor] = path[current_node] + [current_node]

    for node in path:
        path[node].append(node)

    return distances, path
