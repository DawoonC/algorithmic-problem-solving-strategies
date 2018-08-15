from collections import defaultdict


# Finds maximum amount of flows from source to sink (target)
def ford_fulkerson(source, sink, capacity, nodes):
    flows = defaultdict(lambda: defaultdict(int))
    total_flows = 0
    while True:
        parents = defaultdict(lambda: None)
        parents[source] = source
        queue = [source]
        while queue and parents[sink] is None:
            curr = queue.pop(0)
            for neighbor in nodes:
                if parents[neighbor] is None and capacity[curr][neighbor] - flows[curr][neighbor] > 0:
                    queue.append(neighbor)
                    parents[neighbor] = curr
        if parents[sink] is None:
            break
        amount = float('inf')
        p = sink
        while p != source:
            amount = min(amount, capacity[parents[p]][p] - flows[parents[p]][p])
            p = parents[p]
        p = sink
        while p != source:
            flows[parents[p]][p] += amount
            # negative amount to inverse direction
            # ensures to find the maximum total flow
            # no matter which path we take.
            flows[p][parents[p]] -= amount
            p = parents[p]
        total_flows += amount
    return total_flows


def test():
    graph = {
        's': {'a': 16, 'b': 3},
        'a': {'b': 1, 'c': 20},
        'b': {'c': 7, 'd': 7},
        'c': {'b': 5, 't': 10},
        'd': {'t': 8},
        't': {},
    }
    nodes = graph.keys()
    capacity = defaultdict(lambda: defaultdict(int))
    for u in nodes:
        for v, w in graph[u].items():
            capacity[u][v] = w
    total_flows = ford_fulkerson('s', 't', capacity, nodes)
    assert total_flows == 17
    graph = {
        's': {'a': 1, 'b': 3},
        'a': {'b': 1, 't': 2},
        'b': {'t': 1},
        't': {},
    }
    nodes = graph.keys()
    capacity = defaultdict(lambda: defaultdict(int))
    for u in nodes:
        for v, w in graph[u].items():
            capacity[u][v] = w
    total_flows = ford_fulkerson('s', 't', capacity, nodes)
    assert total_flows == 2
    print 'test success!'


if __name__ == '__main__':
    test()  # run
