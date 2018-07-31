#
# Design and implement an algorithm that can preprocess a
# graph and then answer the question "is x connected to y in the
# graph" for any x and y in constant time Theta(1).
#

#
# `process_graph` will be called only once on each graph.  If you want,
# you can store whatever information you need for `is_connected` in
# global variables
#
from collections import defaultdict


def process_graph(G):
    conn_graph = defaultdict(lambda: defaultdict(bool))
    for v in G.keys():
        stack = [v]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for neighbor in G[curr].keys():
                if neighbor in visited:
                    continue
                conn_graph[v][neighbor] = conn_graph[neighbor][v] = True
                conn_graph[curr][neighbor] = conn_graph[neighbor][curr] = True
                stack.append(neighbor)
    is_connected.conn_graph = conn_graph
    return conn_graph


#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick
#
def is_connected(i, j):
    if hasattr(is_connected, 'conn_graph'):
        return is_connected.conn_graph[i][j]
    return False


#######
# Testing
#
def test():
    G = {'a':{'b':1},
         'b':{'a':1},
         'c':{'d':1},
         'd':{'c':1},
         'e':{}}
    process_graph(G)
    assert is_connected('a', 'b') == True
    assert is_connected('a', 'c') == False

    G = {'a':{'b':1, 'c':1},
         'b':{'a':1},
         'c':{'d':1, 'a':1},
         'd':{'c':1},
         'e':{}}
    process_graph(G)
    assert is_connected('a', 'b') == True
    assert is_connected('a', 'c') == True
    assert is_connected('a', 'e') == False


test()
