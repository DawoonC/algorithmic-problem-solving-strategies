def bfs(graph, start):
    distances = { start: 0 }
    path = { start: [start] }
    queue = [start]
    while queue:
        curr = queue.pop(0)
        for neighbor in graph[curr].keys():
            if neighbor not in distances:
                distances[neighbor] = distances[curr] + graph[curr][neighbor]
                path[neighbor] = path[curr] + [neighbor]
                queue.append(neighbor)
    return (distances, path)
