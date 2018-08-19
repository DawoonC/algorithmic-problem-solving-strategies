# Problem ID: NQUEEN
# https://algospot.com/judge/problem/read/NQUEEN
# took > 1000ms


def readline():
    return raw_input()


def cover_board(board, x, y, n, cover):
    for i in xrange(n):
        board[i][x] += cover
        board[y][i] += cover
    i, j = 1, 1
    while y + i < n and (x + j < n or x - j >= 0):
        if x + j < n:
            board[y + i][x + j] += cover
        if x - j >= 0:
            board[y + i][x - j] += cover
        i += 1
        j += 1
    return board


def count_nqueen(board, y, n):
    if y == n:
        return 1
    result = 0
    for x in xrange(n):
        if board[y][x] == 0:
            cover_board(board, x, y, n, 1)
            result += count_nqueen(board, y + 1, n)
            cover_board(board, x, y, n, -1)
    return result


def nqueen():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n = int(readline())
        board = [[0] * n for _ in xrange(n)]
        result = count_nqueen(board, 0, n)
        print result


if __name__ == '__main__':
    nqueen()  # run
