# Problem ID: TSP1
# https://algospot.com/judge/problem/read/TSP1
# TSP1: took 160ms
# TSP2: took > 2000ms
# TSP3: took > 2000ms

from collections import defaultdict


def readline():
    return raw_input()


# with dynamic programming, O(2^n)
def get_shortest_distance(here, visited, distances, n, cache):
    if all(visited):
        return 0
    result = cache[(here, str(visited))]
    if result is not None:
        return result
    result = float('inf')
    for next_city in range(n):
        if visited[next_city]:
            continue
        elif here != next_city:
            visited[next_city] = 1
            d = distances[here][next_city] if here != -1 else 0
            candidate = d + get_shortest_distance(next_city, visited, distances, n, cache)
            visited[next_city] = 0
            result = min(result, candidate)
    cache[(here, str(visited))] = result
    return result


# traveling salesman problem
def tsp_w_dp():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        distances = []
        for _ in range(n):
            inner = map(float, readline().split())
            distances.append(inner)
        visited = [0] * n
        cache = defaultdict(lambda: None)
        shortest_distance = get_shortest_distance(-1, visited, distances, n, cache)
        print shortest_distance


if __name__ == '__main__':
    tsp_w_dp()  # run
