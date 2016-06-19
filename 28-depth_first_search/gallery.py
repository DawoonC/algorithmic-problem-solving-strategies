# Problem ID: GALLERY
# https://algospot.com/judge/problem/read/GALLERY
# 313ms

from collections import defaultdict

def readline():
    return raw_input()


def print_graph(graph):
    for k in graph.keys():
        print k, '=>', graph[k]


def make_graph(u, v, graph):
    graph[u].append(v)
    graph[v].append(u)


def dfs(here, graph, visited, counter):
    visited.append(here)
    children = defaultdict(int)
    for neighbor in graph[here]:
        if neighbor not in visited:
            children[dfs(neighbor, graph, visited, counter)] += 1
    if children['UNWATCHED']:
        counter['installed'] += 1
        return 'INSTALLED'
    if children['INSTALLED']:
        return 'WATCHED'
    return 'UNWATCHED'


def install_camera(graph):
    visited = []
    counter = {'installed': 0}
    for v in graph.keys():
        if v not in visited and dfs(v, graph, visited, counter) == 'UNWATCHED':
            counter['installed'] += 1
    return counter['installed']


def gallery():
    total_tests = int(readline())
    for testcase in range(total_tests):
        num_gallery, num_hallway = map(int, readline().split())
        graph = defaultdict(list)
        for i in range(num_hallway):
            u, v = map(int, readline().split())
            make_graph(u, v, graph)
        print num_gallery - len(graph.keys()) + install_camera(graph)


if __name__ == '__main__':
    gallery()  # run
