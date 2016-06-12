# Problem ID: DICTIONARY
# https://algospot.com/judge/problem/read/DICTIONARY
# 328ms

from string import ascii_lowercase
from collections import defaultdict

def readline():
    return raw_input()


def print_graph(graph):
    for k in graph.keys():
        print k, '=>', graph[k]


def get_ordered_letters(topo_sort):
    letters = topo_sort[::-1]
    for l in ascii_lowercase:
        if l not in topo_sort:
            letters.append(l)
    return ''.join(letters)


def dfs(here, visited, graph, topo_sort):
    visited.append(here)
    for neighbor in graph[here]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph, topo_sort)
    topo_sort.append(here)


def dfs_all(graph, topo_sort):
    visited = []
    for v in graph.keys():
        if v not in visited:
            dfs(v, visited, graph, topo_sort)


def dictionary():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        graph = defaultdict(set)
        words = []
        invalid = False
        for i in range(n):
            word = readline()
            if i == 0:
                graph[word[0]]
            else:
                for j in range(len(min(word, words[-1]))):
                    if word[j] != words[-1][j]:
                        graph[words[-1][j]].add(word[j])
                        if words[-1][j] in graph[word[j]]:
                            invalid = True
                        break
            words.append(word)
        if invalid:
            print 'INVALID HYPOTHESIS'
        else:
            topo_sort = []
            dfs_all(graph, topo_sort)
            print get_ordered_letters(topo_sort)


if __name__ == '__main__':
    dictionary()  # run
