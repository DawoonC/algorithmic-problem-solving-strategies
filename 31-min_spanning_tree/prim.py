import heapq


def prim(root, graph):
    queue = [(0, root, root)]
    selected = []
    visited = set()
    total = 0
    while queue:
        w, curr, prev = heapq.heappop(queue)
        if curr in visited:
            continue
        selected.append((prev, curr, w))
        total += w
        visited.add(curr)
        for neighbor in graph[curr].keys():
            heapq.heappush(queue, (graph[curr][neighbor], neighbor, curr))
    return selected, total
