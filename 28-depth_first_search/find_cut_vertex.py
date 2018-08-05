from collections import defaultdict


def find_cut_vertex(here, is_root, graph, discovered, cut_vertices, counter):
    # keep track order of discovery for every vertex
    result = discovered[here] = counter['val']
    counter['val'] += 1
    children = 0
    for neighbor in graph[here]:
        if discovered[neighbor] is None:
            children += 1
            subtree = find_cut_vertex(neighbor, False, graph, discovered, cut_vertices, counter)
            # if there is no path to reach higher node in the tree from subtree
            # then it means current vertext is a cut vertex
            if not is_root and subtree >= discovered[here]:
                cut_vertices[here] = True
            result = min(result, subtree)
        else:
            result = min(result, discovered[neighbor])
    if is_root:
        cut_vertices[here] = (children >= 2)
    return result


def test():
    graph = {
        0: [1],
        1: [0, 2, 3],
        2: [1, 3, 5],
        3: [1, 2, 4, 5],
        4: [3],
        5: [2, 3, 6, 7],
        6: [5],
        7: [5],
    }
    discovered = defaultdict(lambda: None)
    cut_vertices = defaultdict(lambda: False)
    counter = {'val': 0}
    result = find_cut_vertex(0, True, graph, discovered, cut_vertices, counter)
    print 'result:', result
    print 'discovered:', discovered
    print 'cut_vertices:', cut_vertices


if __name__ == '__main__':
    test()  # run
