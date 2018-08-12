from disjoint_set import DisjointSet


def kruskal(edges, n):
    sorted_edges = sorted([(w, u, v) for u, v, w in edges])
    sets = DisjointSet(n)
    selected = []
    total = 0
    for w, u, v in sorted_edges:
        if sets.find(u) == sets.find(v):
            continue
        sets.merge(u, v)
        selected.append((u, v, w))
        total += w
    return selected, total
