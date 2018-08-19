# Problem ID: NQUEEN
# https://algospot.com/judge/problem/read/NQUEEN
# took > 1000ms


def readline():
    return raw_input()


def count_nqueen(board, y, n, cols, d1, d2):
    if y == n:
        return 1
    result = 0
    for x in xrange(n):
        id1 = x - y + n
        id2 = x + y
        if cols[x] or d1[id1] or d2[id2]:
            continue
        cols[x], d1[id1], d2[id2] = True, True, True
        result += count_nqueen(board, y + 1, n, cols, d1, d2)
        cols[x], d1[id1], d2[id2] = False, False, False
    return result


def nqueen():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n = int(readline())
        board = [[0] * n for _ in xrange(n)]
        cols = [False] * n
        d1 = [False] * (n * 2)
        d2 = [False] * (n * 2)
        result = count_nqueen(board, 0, n, cols, d1, d2)
        print result


if __name__ == '__main__':
    nqueen()  # run
