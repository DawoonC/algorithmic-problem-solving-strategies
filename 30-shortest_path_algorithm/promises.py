# Problem ID: PROMISES
# https://algospot.com/judge/problem/read/PROMISES
# timeout

def readline():
    return raw_input()


def init_graph(v_list):
    return [[(0 if i == j else float('inf')) for j in v_list] for i in v_list]


def make_edge(u, v, t, graph):
    if t < graph[u][v]:
        graph[u][v] = graph[v][u] = t


def floyd(graph, v_list):
    inf = float('inf')
    for k in v_list:
        for i in v_list:
            if graph[i][k] != inf:
                for j in v_list:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


def update(u, v, t, graph, v_list):
    for i in v_list:
        for j in v_list:
            graph[i][j] = min(graph[i][j],
                              min(graph[i][u] + t + graph[v][j],
                                  graph[i][v] + t + graph[u][j]))


def promises():
    total_tests = int(readline())
    for testcase in range(total_tests):
        num_of_cities, num_of_curr_road, num_of_future_road = v, m, n = map(int, readline().split())
        v_list = range(num_of_cities)
        graph = init_graph(v_list)
        for i in range(num_of_curr_road):
            u, v, t = map(int, readline().split())
            make_edge(u, v, t, graph)
        floyd(graph, v_list)
        count = 0
        for i in range(num_of_future_road):
            u, v, t = map(int, readline().split())
            if t < graph[u][v]:
                count += 1
                make_edge(u, v, t, graph)
                update(u, v, t, graph, v_list)
        print num_of_future_road - count


if __name__ == '__main__':
    promises()  # run
