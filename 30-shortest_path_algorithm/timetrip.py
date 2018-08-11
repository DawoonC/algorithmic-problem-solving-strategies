# Problem ID: TIMETRIP
# https://algospot.com/judge/problem/read/TIMETRIP
# took 192ms

from collections import defaultdict


def readline():
    return raw_input()


def timetrip_bellman_ford(start, graph, n):
    max_dist = defaultdict(lambda: -float('inf'))
    min_dist = defaultdict(lambda: float('inf'))
    max_dist[start] = min_dist[start] = 0
    max_updated = False
    min_updated = False
    for _ in xrange(n):
        max_updated = min_updated = False
        for curr in graph.keys():
            for neighbor in graph[curr].keys():
                for w in graph[curr][neighbor]:
                    if (min_dist[curr] + w) < min_dist[neighbor]:
                        min_dist[neighbor] = min_dist[curr] + w
                        min_updated = True
                    if (max_dist[curr] + w) > max_dist[neighbor]:
                        max_dist[neighbor] = max_dist[curr] + w
                        max_updated = True
        if not max_updated and not min_updated:
            break
    return (
        None if min_updated else min_dist,
        None if max_updated else max_dist,
    )


def timetrip():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n_v, n_e = map(int, readline().split())
        graph = defaultdict(lambda: defaultdict(list))
        for _ in xrange(n_e):
            u, v, w = map(int, readline().split())
            graph[u][v].append(w)
        min_dist, max_dist = timetrip_bellman_ford(0, graph, n_v)
        min_result = 'INFINITY' if min_dist is None else min_dist[1]
        max_result = 'INFINITY' if max_dist is None else max_dist[1]
        if min_result == float('inf'):
            print 'UNREACHABLE'
        else:
            print min_result, max_result


if __name__ == '__main__':
    timetrip()  # run
