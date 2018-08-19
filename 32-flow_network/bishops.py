# Problem ID: BISHOPS
# https://algospot.com/judge/problem/read/BISHOPS
# took 20ms

from collections import defaultdict
from bipartite_match import bipartite_match


def readline():
    return raw_input()


def count_bishops(board, n):
    groups = defaultdict(lambda: None)
    count = [0, 0]
    dx = [-1, 1]
    dy = [1, 1]
    for di in xrange(2):
        for y in xrange(n):
            for x in xrange(n):
                if board[y][x] == '.' and groups[(di, y, x)] is None:
                    cy, cx = y, x
                    while cy >= 0 and cy < n and cx >= 0 and cx < n and board[cy][cx] == '.':
                        groups[(di, cy, cx)] = count[di]
                        cy += dy[di]
                        cx += dx[di]
                    count[di] += 1
    graph = defaultdict(lambda: defaultdict(lambda: None))
    for y in xrange(n):
        for x in xrange(n):
            if board[y][x] == '.':
                graph[groups[(0, y, x)]][groups[(1, y, x)]] = 1
    return bipartite_match(graph, n)


def bishops():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n = int(readline())
        board = []
        for _ in xrange(n):
            row = readline()
            board.append(row)
        result = count_bishops(board, n)
        print result


if __name__ == '__main__':
    bishops()  # run
