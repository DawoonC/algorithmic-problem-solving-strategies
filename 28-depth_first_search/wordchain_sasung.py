# Problem ID: WORDCHAIN
# https://algospot.com/judge/problem/read/WORDCHAIN

from collections import defaultdict

def get_euler_circuit(now, circuit):
    for nxt in graph[now]:
        while adj[now][nxt]:
            adj[now][nxt] -= 1
            get_euler_circuit(nxt, circuit)
    circuit.append(now)


def get_euler_trail_or_circuit():
    circuit = []
    for c in set_words:
        if outdegree[c] == indegree[c]+1:
            get_euler_circuit(c, circuit)
            return circuit
    for c in set_words:
        if outdegree[c]:
            get_euler_circuit(c, circuit)
            return circuit
    return circuit


def check_euler():
    plus1 = 0
    minus1 = 0
    for c in set_words:
        delta = outdegree[c] - indegree[c]
        if not(-1 <= delta <= 1):
            return False
        if delta == 1:
            plus1 += 1
        if delta == -1:
            minus1 += 1
    return (plus1 == 1 and minus1 == 1) or (plus1 == 0 or minus1 == 0)


def solve():
    if not check_euler():
        return 'IMPOSSIBLE'
    circuit = get_euler_trail_or_circuit()
    if len(circuit) != N+1:
        return 'IMPOSSIBLE'
    circuit.reverse()
    # print circuit
    ret = []
    for a, b in zip(circuit, circuit[1:]):
        ret.append(graph[a][b].pop())
    return ' '.join(ret)


for C in range(int(input())):
    N = int(input())
    graph = defaultdict(lambda: defaultdict(list))
    adj = defaultdict(lambda: defaultdict(int))
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    set_words = set()
    for w in (raw_input() for i in range(N)):
        a= w[0]
        b = w[-1]
        graph[a][b].append(w)
        adj[a][b] += 1
        outdegree[a] += 1
        indegree[b] += 1
        set_words.add(a)
        set_words.add(b)

    # print outdegree, indegree
    # print set_words
    print(solve())

'''
3
4
dog
god
dragon
need
3
aa
ab
bb
2
ab
cd
'''
