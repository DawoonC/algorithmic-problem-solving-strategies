# Problem ID: MEETINGROOM
# https://algospot.com/judge/problem/read/MEETINGROOM

from collections import defaultdict
import scc

def readline():
    return raw_input()


def print_graph(graph, meetings):
    for k in graph.keys():
        print k, '=>', graph[k],


def disjoint(a, b):
    return a[1] <= b[0] or b[1] <= a[0]


def make_graph(meetings, graph, num_of_meetings):
    for i in range(0, num_of_meetings, 2):
        j = i + 1
        graph[i * 2 + 1].append(j * 2)
        graph[j * 2 + 1].append(i * 2)
    for i in range(num_of_meetings):
        for j in range(i):
            if not disjoint(meetings[i], meetings[j]):
                graph[i * 2].append(j * 2 + 1)
                graph[j * 2].append(i * 2 + 1)


def solve_2sat(n, graph):
    label = scc.tarjan_scc(graph)
    for i in range(0, n, 2):
        if label[i] == label[i+1]:
            return None
    value = defaultdict(lambda:-1)
    order = []
    for i in range(n):
        order.append((-label[i], i))
    order = sorted(order)
    for i in range(n):
        vertex = order[i][1]
        variable = vertex / 2
        is_true = 1 if vertex % 2 == 0 else 0
        if value[variable] != -1:
            continue
        value[variable] = 1 if not is_true else 0
    return value


def meetingroom():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        meetings = []
        graph = defaultdict(list)
        for i in range(n):
            a,b,c,d = map(int, readline().split())
            meetings.append((a,b))
            meetings.append((c,d))
        make_graph(meetings, graph, n*2)
        result = solve_2sat(n*2*2, graph)
        if result != None:
            print 'POSSIBLE'
            for i in range(n*2):
                if result[i] == 1:
                    print meetings[i][0], meetings[i][1] 
        else:
            print 'IMPOSSIBLE'


if __name__ == '__main__':
    meetingroom()  # run
