from collections import defaultdict


def bellman_ford(g, start, num_of_v):
    upper_dist = defaultdict(lambda: float('inf'))
    upper_dist[start] = 0
    v_list = range(num_of_v)
    updated = False
    # iterate V times
    for _ in v_list:
        updated = False
        for v in g.keys():
            for w in g[v].keys():
                if upper_dist[w] > upper_dist[v] + g[v][w]:
                    upper_dist[w] = upper_dist[v] + g[v][w]
                    updated = True
        # if there is no vertex to update, then break
        if not updated:
            break
    # if it's updated after all iteration,
    # it means there is a negative cycle
    if updated:
        return None
    return upper_dist


def bellman_ford_new(start, graph):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    n = len(graph.keys())
    updated = False
    for _ in xrange(n):
        updated = False
        for curr in graph.keys():
            for neighbor, w in graph[curr].items():
                if (dist[curr] + w) < dist[neighbor]:
                    dist[neighbor] = dist[curr] + w
                    updated = True
        if not updated:
            break
    # if there is no negative cycle in a graph
    # nth iteration will not be updated
    # so if it's updated after nth iteration,
    # it means there is a negative cycle in a graph.
    if updated:
        return 'there is a negative cycle in a graph!'
    return dist
