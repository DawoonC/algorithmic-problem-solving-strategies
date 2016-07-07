# Problem ID: FIRETRUCK
# https://algospot.com/judge/problem/read/FIRETRUCK
# 555ms

from collections import defaultdict

def readline():
    return raw_input()


def dijkstra(g, start):
    dist = {start: 0}
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in g[v].keys():
            if w not in dist or dist[v]+g[v][w] < dist[w]:
                dist[w] = dist[v]+g[v][w]
                queue.append(w)
    return dist


def make_edge(a, b, t, graph):
    t = int(t)
    if b not in graph[a] or t < graph[a][b]:
        graph[a][b] = t
        graph[b][a] = t


def firetruck():
    total_tests = int(readline())
    for testcase in range(total_tests):
        v, e, n, m = map(int, readline().split())
        graph = defaultdict(lambda: defaultdict(int))
        for i in range(e):
            a, b, t = readline().split()
            make_edge(a, b, t, graph)
        firespots = readline().split()
        firestations = readline().split()
        for fst in firestations:
            make_edge('-1', fst, 0, graph)
        dist = dijkstra(graph, '-1')
        result = sum(dist[fire] for fire in firespots)
        print result


if __name__ == '__main__':
    firetruck()  # run
