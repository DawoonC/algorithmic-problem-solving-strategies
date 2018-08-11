# Problem ID: FIRETRUCKS
# https://algospot.com/judge/problem/read/FIRETRUCKS
# took 392ms

from collections import defaultdict
import heapq


def readline():
    return raw_input()


def firetruck_dijkstra(stations, graph):
    queue = [(0, start) for start in stations]
    dist = {start: 0 for start in stations}
    while queue:
        _, curr = heapq.heappop(queue)
        for neighbor in graph[curr].keys():
            if neighbor not in dist or (dist[curr] + graph[curr][neighbor]) < dist[neighbor]:
                dist[neighbor] = dist[curr] + graph[curr][neighbor]
                heapq.heappush(queue, (dist[neighbor], neighbor))
    return dist


def firetrucks():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n_v, n_e, n_fire, n_station = map(int, readline().split())
        graph = defaultdict(lambda: defaultdict(None))
        for _ in xrange(n_e):
            u, v, w = map(int, readline().split())
            graph[u][v] = graph[v][u] = w
        fires = map(int, readline().split())
        stations = map(int, readline().split())
        dist = firetruck_dijkstra(stations, graph)
        total = 0
        for fire in fires:
            total += dist[fire]
        print total


if __name__ == '__main__':
    firetrucks()  # run
