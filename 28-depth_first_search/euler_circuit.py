def get_euler_circuit(here, graph, circuit):
    for neighbor in xrange(len(graph)):
        while graph[here][neighbor] > 0:
            graph[here][neighbor] -= 1
            graph[neighbor][here] -= 1
            get_euler_circuit(neighbor, graph, circuit)
    circuit.append(here)


def test():
    graph = [
        [0, 0, 2, 2],
        [0, 0, 4, 0],
        [2, 4, 0, 4],
        [2, 0, 4, 0],
    ]
    circuit = []
    get_euler_circuit(0, graph, circuit)
    print ' -> '.join(map(str, circuit[::-1]))


if __name__ == '__main__':
    test()  # run
