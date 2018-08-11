from collections import defaultdict


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


def floyd_new(graph):
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for curr in graph.keys():
        dist[curr][curr] = 0
        for neighbor in graph[curr].keys():
            dist[curr][neighbor] = graph[curr][neighbor]
    nodes = graph.keys()
    for k in nodes:
        for u in nodes:
            for v in nodes:
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
    return dist


def floyd_path(graph):
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    path = defaultdict(lambda: defaultdict(list))
    for curr in graph.keys():
        dist[curr][curr] = 0
        path[curr][curr] = [curr]
        for neighbor in graph[curr].keys():
            dist[curr][neighbor] = graph[curr][neighbor]
            path[curr][neighbor] = [curr, neighbor]
    nodes = graph.keys()
    for k in nodes:
        for u in nodes:
            for v in nodes:
                if (dist[u][k] + dist[k][v]) < dist[u][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]
                    path[u][v] = path[u][k] + path[k][v][1:]
    return dist, path
