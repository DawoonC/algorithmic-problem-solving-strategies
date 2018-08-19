from collections import defaultdict


def dfs_match(curr, graph, visited, a_match, b_match):
    if curr in visited:
        return False
    visited.add(curr)
    for neighbor in graph[curr].keys():
        if b_match[neighbor] is None or dfs_match(b_match[neighbor], graph, visited, a_match, b_match):
            a_match[curr] = neighbor
            b_match[neighbor] = curr
            return True
    return False


def bipartite_match(graph, n):
    a_match = defaultdict(lambda: None)
    b_match = defaultdict(lambda: None)
    size = 0
    for start in graph.keys():
        result = dfs_match(start, graph, set(), a_match, b_match)
        if result:
            size += 1
    return size
