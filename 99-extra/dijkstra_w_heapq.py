import heapq


def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {start: 0}
    path = {start: [start]}
    while queue:
        (_, curr) = heapq.heappop(queue)
        for neighbor in graph[curr].keys():
            if (neighbor not in distances) or (distances[curr] + graph[curr][neighbor] < distances[neighbor]):
                distances[neighbor] = distances[curr] + graph[curr][neighbor]
                path[neighbor] = path[curr] + [neighbor]
                heapq.heappush(queue, (distances[neighbor], neighbor))
    return (distances, path)
