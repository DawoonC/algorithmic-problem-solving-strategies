# Problem ID: FIRETRUCKS
# https://algospot.com/judge/problem/read/FIRETRUCKS

from collections import defaultdict


def dijkstra(g, start, fire):
    dist = {start: 0}
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in g[v].keys():
            if w not in dist or dist[v] + g[v][w] < dist[w]:
                dist[w] = dist[v] + g[v][w]
                queue.append(w)

    return count(dist, fire)

def count(dist, fire):
    result = 0
    for f in fire:
        result += dist[f]
        # print dist[f]

    return result

def make_edge(a, b, c, graph):
    c = int(c)
    if b not in graph[a] or c < graph[a][b]:
        graph[a][b] = c
        graph[b][a] = c

def firetrucks():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        v, e, n, m = map(int, raw_input().split())
        graph = defaultdict(lambda: defaultdict(float))
        for i in range(e):
            a, b, c = raw_input().split()
            make_edge(a, b, c, graph)

        fire = map(str, raw_input().split())
        station = map(str, raw_input().split())

        for i in station:
            graph[0][i] = 0
            graph[i][0] = 0

        result = dijkstra(graph, 0, fire)
        print result

firetrucks()

'''
1
8 12 3 2
1 2 3
1 6 9
2 3 6
3 4 4
3 5 2
4 5 7
6 5 5
8 6 5
6 7 3
8 7 3
7 5 1
2 8 3
2 3 5
4 6
'''