#coding=utf-8
# https://algospot.com/judge/problem/read/BOARDCOVER

cover_type = [
    [[0,0], [1,0], [0,1]],
    [[0,0], [0,1], [1,1]],
    [[0,0], [1,0], [1,1]],
    [[0,0], [1,0], [1,-1]]
]

# black = 1 white = 0
def read():
    result = []
    text_list = list(raw_input())
    for text in text_list:
        if text == '#':
            result.append(1)
        else:
            result.append(0)
    return result


def set(board, y, x, type, delta):
    ok = True
    for i in range(3):
        ny = y + cover_type[type][i][0]
        nx = x + cover_type[type][i][1]

        if ny >= 0 and nx >= 0 and ny < len(board) and nx < len(board[0]):
            board[ny][nx] += delta

        if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
            ok = False
        elif board[ny][nx] > 1:
            ok = False

    return ok


def cover(board):
    y = -1
    x = -1

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y = i
                x = j
                break

        if y != -1:
            break

    if y == -1:
        return 1

    count = 0
    for type in range(4):
        if set(board, y, x, type, 1):
            count += cover(board)
        set(board, y, x, type, -1)

    return count


def board_cover():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        board = []
        total_row, total_col = map(int, raw_input().split())

        for i in range(total_row):
            board.append(read())

        print(cover(board))

board_cover()