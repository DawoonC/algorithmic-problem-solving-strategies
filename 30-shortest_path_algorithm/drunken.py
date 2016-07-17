# Problem ID: DRUNKEN
# https://algospot.com/judge/problem/read/DRUNKEN
# timeout

def readline():
    return raw_input()


def init_graph(v_list):
    return [[(0 if i == j else float('inf')) for j in v_list] for i in v_list]


def make_edge(u, v, t, graph):
    u, v = u-1, v-1
    if t < graph[u][v]:
        graph[u][v] = graph[v][u] = t


def floyd(graph, delayed_graph, delay_order, v_list):
    inf = float('inf')
    for k in v_list:
        delay, w = delay_order[k]
        for i in v_list:
            if graph[i][w] != inf:
                for j in v_list:
                    graph[i][j] = min(graph[i][j], graph[i][w] + graph[w][j])
                    delayed_graph[i][j] = min(delayed_graph[i][j], graph[i][w] + delay + graph[w][j])


def drunken():
    num_of_v, num_of_e = map(int, readline().split())
    delay_list = map(int, readline().split())
    v_list, e_list = range(num_of_v), range(num_of_e)
    delay_order = sorted([(delay_list[i], i) for i in v_list])
    graph = init_graph(v_list)
    delayed_graph = init_graph(v_list)
    for e in e_list:
        u, v, t = map(int, readline().split())
        make_edge(u, v, t, graph)
    floyd(graph, delayed_graph, delay_order, v_list)
    total_tests = int(readline())
    for testcase in range(total_tests):
        start, end = map(int, readline().split())
        print delayed_graph[start-1][end-1]


if __name__ == '__main__':
    drunken()  # run
