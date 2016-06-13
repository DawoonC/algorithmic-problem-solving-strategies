# Problem ID: WORDCHAIN
# https://algospot.com/judge/problem/read/WORDCHAIN
# 67ms

from string import ascii_lowercase
from collections import defaultdict

def readline():
    return raw_input()


def get_euler_circuit(here, circuit, adj):
    for there in range(26):
        while adj[here][there] > 0:
            adj[here][there] -= 1
            get_euler_circuit(there, circuit, adj)
    circuit.append(here)


def get_euler_trail_or_circuit(adj, outdegree, indegree):
    circuit = []
    # trail
    for i in range(26):
        if outdegree[i] == indegree[i]+1:
            get_euler_circuit(i, circuit, adj)
            return circuit
    # circuit
    for j in range(26):
        if outdegree[j]:
            get_euler_circuit(j, circuit, adj)
            return circuit
    return circuit


def check_euler(outdegree, indegree):
    plus1 = 0
    minus1 = 0
    for i in range(26):
        delta = outdegree[i] - indegree[i]
        if delta < -1 or 1 < delta: return False
        if delta == 1:
            plus1 += 1
        if delta == -1:
            minus1 += 1
    return (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0)


def solve(graph, adj, outdegree, indegree, n):
    if not check_euler(outdegree, indegree):
        return 'IMPOSSIBLE'
    circuit = get_euler_trail_or_circuit(adj, outdegree, indegree)
    if len(circuit) != n+1: return 'IMPOSSIBLE'
    circuit = circuit[::-1]
    result = ''
    for i in range(1, len(circuit)):
        a = circuit[i-1]
        b = circuit[i]
        if result:
            result += ' '
        result += graph[a][b].pop()
    return result


def wordchain():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        adj = [[0 for j in range(26)] for i in range(26)]
        graph = [[[] for j in range(26)] for i in range(26)]
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for i in range(n):
            word = readline()
            a = ascii_lowercase.find(word[0])
            b = ascii_lowercase.find(word[-1])
            graph[a][b].append(word)
            adj[a][b] += 1
            outdegree[a] += 1
            indegree[b] += 1
        result = solve(graph, adj, outdegree, indegree, n)
        print result if result else 'IMPOSSIBLE'


if __name__ == '__main__':
    wordchain()  # run
