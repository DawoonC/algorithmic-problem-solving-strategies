# Problem ID: TPATH
# https://algospot.com/judge/problem/read/TPATH
# took > 4000ms

from disjoint_set import DisjointSet


def readline():
    return raw_input()


def kruskal_min_upper_bound(lower_bound, edges, n):
    sets = DisjointSet(n)
    for w, u, v in edges:
        if w < lower_bound:
            continue
        sets.merge(u, v)
        if sets.find(0) == sets.find(n - 1):
            return w
    return float('inf')


def min_weight_diff(edges, n):
    result = float('inf')
    for w, u, v in edges:
        result = min(result, kruskal_min_upper_bound(w, edges, n) - w)
    return result


def tpath():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n_v, n_e = map(int, readline().split())
        edges = []
        for _ in xrange(n_e):
            u, v, w = map(int, readline().split())
            edges.append((w, u, v))
        edges.sort()
        print min_weight_diff(edges, n_v)


if __name__ == '__main__':
    tpath()  # run
