# Problem ID: TSP
# https://algospot.com/judge/problem/read/TSP
# took ?ms

from collections import defaultdict


def readline():
    return raw_input()


# brute force way, O(n!)
def get_shortest_distance(current_length, path, visited, distances, n):
    if len(path) == n:
        return 0
    result = float('inf')
    for next_city in range(n):
        if visited[next_city]:
            continue
        here = path[-1] if len(path) > 0 else None
        path.append(next_city)
        visited[next_city] = True
        d = distances[here][next_city] if here else 0
        candidate = get_shortest_distance(current_length + d, path, visited, distances, n)
        result = min(result, candidate)
        visited[next_city] = False
        path.pop()
    return result


# traveling salesman problem
def tsp():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        distances = []
        for _ in range(n):
            inner = map(float, readline().split())
            distances.append(inner)
        visited = defaultdict(lambda: False)
        path = []
        shortest_distance = get_shortest_distance(0, path, visited, distances, n)
        print shortest_distance


if __name__ == '__main__':
    tsp()  # run
