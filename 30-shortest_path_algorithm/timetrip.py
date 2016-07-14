# Problem ID: TIMETRIP
# https://algospot.com/judge/problem/read/TIMETRIP
# 725ms

from collections import defaultdict

def readline():
    return raw_input()


def bellman_ford(g, start, end, num_of_v):
    upper_dist = defaultdict(lambda: float('inf'))
    upper_dist[start] = 0
    v_list = range(num_of_v)
    path = {start: (start,)}
    for _ in v_list:
        for v in g.keys():
            for w in g[v].keys():
                if upper_dist[w] > upper_dist[v]+g[v][w]:
                    upper_dist[w] = upper_dist[v]+g[v][w]
                    path[w] = path[v]+(w,)
    for v in g.keys():
        for w in g[v].keys():
            if upper_dist[v] + g[v][w] < upper_dist[w]:
                if end in path and v in path[end] and w in path[end]:
                    return None
    return upper_dist


def make_edge(a, b, d, graph, inverted_graph):
    d = int(d)
    if b not in graph[a] or d < graph[a][b]:
        graph[a][b] = d
    if b not in inverted_graph[a] or -d < inverted_graph[a][b]:
        inverted_graph[a][b] = -d


def timetrip():
    total_tests = int(readline())
    for testcase in range(total_tests):
        gx, wh = map(int, readline().split())
        graph = defaultdict(lambda: defaultdict(int))
        inverted_graph = defaultdict(lambda: defaultdict(int))
        for _ in range(wh):
            a, b, d = readline().split()
            make_edge(a, b, d, graph, inverted_graph)
        dist = bellman_ford(graph, '0', '1', gx)
        shortest = 'INFINITY' if dist == None else dist['1']
        if shortest == float('inf'):
            print 'UNREACHABLE'
            continue
        inverted_dist = bellman_ford(inverted_graph, '0', '1', gx)
        longest = 'INFINITY' if inverted_dist == None else -inverted_dist['1']
        print shortest, longest


if __name__ == '__main__':
    timetrip()  # run
