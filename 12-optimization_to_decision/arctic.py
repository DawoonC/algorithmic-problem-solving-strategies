# Problem ID: ARCTIC
# https://algospot.com/judge/problem/read/ARCTIC
# took > 1000ms

from collections import defaultdict
from math import sqrt


def readline():
    return raw_input()


def get_distances(locations, n):
    distances = defaultdict(lambda: defaultdict(lambda: None))
    for i in xrange(n):
        for j in xrange(n):
            if i != j and distances[i][j] is None:
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                distances[i][j] = distances[j][i] = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return distances


def is_all_connected(d, n, distances):
    visited = set([0])
    queue = [0]
    seen = 0
    while queue:
        here = queue.pop(0)
        seen += 1
        for there in xrange(n):
            if there not in visited and distances[here][there] <= d:
                visited.add(there)
                queue.append(there)
    return seen == n


def get_min_distance(n, distances):
    lo, hi = 0.0, 1416.0
    for _ in xrange(100):
        mid = (lo + hi) / 2
        if is_all_connected(mid, n, distances):
            hi = mid
        else:
            lo = mid
    return hi


def arctic():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        locations = []
        for i in range(n):
            x, y = map(float, readline().split())
            locations.append((x, y))
        distances = get_distances(locations, n)
        result = get_min_distance(n, distances)
        print '%.2f' % result


if __name__ == '__main__':
    arctic()  # run
