def init_graph(v_list):
    return [[(0 if i == j else float('inf')) for j in v_list] for i in v_list]


def floyd(graph, v_list):
    inf = float('inf')
    for k in v_list:
        for i in v_list:
            if graph[i][k] != inf:
                for j in v_list:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph
