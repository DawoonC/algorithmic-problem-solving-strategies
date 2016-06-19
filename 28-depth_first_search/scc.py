from collections import defaultdict

def scc(here, graph, stack, discovered, finished, scc_ids, counter):
    counter['vertex_counter'] += 1
    result = discovered[here] = counter['vertex_counter']
    stack.append(here)
    for _next in graph[here]:
        if discovered[_next] == -1:
            result = min(result, scc(_next, graph, stack, discovered, finished, scc_ids, counter))
        elif discovered[_next] < discovered[here] and finished[_next] != 1:
            result = min(result, discovered[_next])
    if result == discovered[here]:
        while True:
            scc_vertex = stack.pop()
            scc_ids[scc_vertex] = counter['scc_counter']
            if scc_vertex == here:
                break
        counter['scc_counter'] += 1
    finished[here] = 1
    return result


def tarjan_scc(graph):
    stack = []
    discovered = defaultdict(lambda:-1)
    finished = defaultdict(lambda:-1)
    scc_ids = defaultdict(lambda:-1)
    counter = {'vertex_counter': 0, 'scc_counter': 0}
    for v in graph.keys():
        if discovered[v] == -1:
            scc(v, graph, stack, discovered, finished, scc_ids, counter)
    return scc_ids
