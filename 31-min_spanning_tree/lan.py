# Problem ID: LAN
# https://algospot.com/judge/problem/read/LAN
# took > 1000ms

from disjoint_set import DisjointSet
from math import sqrt


def readline():
    return raw_input()


def get_distance(a, b, x_list, y_list):
    return sqrt(((y_list[a] - y_list[b]) ** 2) + ((x_list[a] - x_list[b]) ** 2))


def create_edge_list(x_list, y_list, n):
    edges = []
    for i in xrange(n - 1):
        for j in xrange(i + 1, n):
            w = get_distance(i, j, x_list, y_list)
            edges.append((w, i, j))
    return sorted(edges)


def lan_kruskal(edges, sets):
    total = 0
    for w, u, v in edges:
        if sets.find(u) == sets.find(v):
            continue
        sets.merge(u, v)
        total += w
    return total


def lan():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n_v, n_exist = map(int, readline().split())
        x_list = map(int, readline().split())
        y_list = map(int, readline().split())
        sets = DisjointSet(n_v)
        for _ in xrange(n_exist):
            u, v = map(int, readline().split())
            sets.merge(u, v)
        edges = create_edge_list(x_list, y_list, n_v)
        result = lan_kruskal(edges, sets)
        print '%.10f' % result


if __name__ == '__main__':
    lan()  # run
