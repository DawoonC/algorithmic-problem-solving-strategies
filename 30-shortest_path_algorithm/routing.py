# Problem ID: ROUTING
# https://algospot.com/judge/problem/read/ROUTING
# took > 2000ms

from collections import defaultdict
import heapq


def readline():
    return raw_input()


def route_dijkstra(start, graph):
    queue = [(1, start)]
    dist = {start: 1}
    while queue:
        _, curr = heapq.heappop(queue)
        for neighbor in graph[curr].keys():
            if neighbor not in dist or (dist[curr] * graph[curr][neighbor]) < dist[neighbor]:
                dist[neighbor] = dist[curr] * graph[curr][neighbor]
                heapq.heappush(queue, (dist[neighbor], neighbor))
    return dist


def routing():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n_com, n_line = map(int, readline().split())
        graph = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for _ in xrange(n_line):
            u, v, w = readline().split()
            u, v, w = int(u), int(v), float(w)
            graph[u][v] = graph[v][u] = min(graph[u][v], w)
        dist = route_dijkstra(0, graph)
        print '%.10f' % dist[n_com - 1]


if __name__ == '__main__':
    routing()  # run
