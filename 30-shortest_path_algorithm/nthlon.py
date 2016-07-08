# Problem ID: NTHLON
# https://algospot.com/judge/problem/read/NTHLON
# timeout

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


def vertex(delta):
    return delta + 200


def nthlon():
    total_tests = int(readline())
    base_list = range(-200, 201)
    start = 401
    for testcase in range(total_tests):
        m = int(readline())
        m_list = range(m)
        a_list = []
        b_list = []
        graph = defaultdict(lambda: defaultdict(int))
        for i in m_list:
            a, b = map(int, readline().split())
            a_list.append(a)
            b_list.append(b)
            delta = a - b
            graph[start][vertex(delta)] = a
        for delta in base_list:
            for i in m_list:
                next = delta + a_list[i] - b_list[i]
                if abs(next) < 201:
                    graph[vertex(delta)][vertex(next)] = a_list[i]
        dist = dijkstra(graph, start)
        result = dist[vertex(0)] if vertex(0) in dist else -1
        print result if result is not -1 else 'IMPOSSIBLE'


if __name__ == '__main__':
    nthlon()  # run
