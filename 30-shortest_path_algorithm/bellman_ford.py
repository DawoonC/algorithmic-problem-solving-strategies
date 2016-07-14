from collections import defaultdict

def bellman_ford(g, start):
    upper_dist = defaultdict(lambda: float('inf'))
    upper_dist[start] = 0
    v_list = g.keys()
    updated = False
    # iterate V times
    for _ in v_list:
        updated = False
        for v in v_list:
            for w in g[v].keys():
                if upper_dist[w] > upper_dist[v]+g[v][w]:
                    upper_dist[w] = upper_dist[v]+g[v][w]
                    updated = True
        # if there is no vertex to update, then break
        if not updated:
            break
    # if it's updated after all iteration,
    # it means there is a negative cycle
    if updated:
        return None
    return upper_dist
