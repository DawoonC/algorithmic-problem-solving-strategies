# Problem ID: ROUTING
# https://algospot.com/judge/problem/read/ROUTING

from collections import defaultdict
from decimal import Decimal

def readline():
    return raw_input()

def get_precise_decimal(num):
    decimal_num = str(Decimal(num))
    dot = decimal_num.find('.') + 1
    return decimal_num[:dot] + decimal_num[dot:][:10]

def dijkstra(g, start, end):
    dist = {start: 1}
    queue = [start]
    while queue:
        v = queue.pop(0)
        print v
        for w in g[v].keys():
            if w not in dist or dist[v]*g[v][w] < dist[w]:
                dist[w] = dist[v]*g[v][w]
                print dist
                queue.append(w)
    return dist[end]


def make_edge(a, b, c, graph):
    c = float(c)
    if b not in graph[a] or c < graph[a][b]:
        graph[a][b] = c
        graph[b][a] = c


def routing():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n, m = map(int, readline().split())
        graph = defaultdict(lambda: defaultdict(float))
        for i in range(m):
            a, b, c = readline().split()
            make_edge(a, b, c, graph)
        print graph
        result = dijkstra(graph, '0', str(n-1))
        print result
        print get_precise_decimal(result)


if __name__ == '__main__':
    routing()  # run


'''
1
7 14
0 1 1.3
0 2 1.1
0 3 1.24
3 4 1.17
3 5 1.24
3 1 2
1 2 1.31
1 2 1.26
1 4 1.11
1 5 1.37
5 4 1.24
4 6 1.77
5 6 1.11
2 6 1.2
'''