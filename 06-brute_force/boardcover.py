# Problem ID: BOARDCOVER
# https://algospot.com/judge/problem/read/BOARDCOVER

from collections import defaultdict

adjacent_panels = [
    ((-1,-1),(-1,0)),
    ((-1,0),(-1,1)),
    ((-1,0),(0,-1)),
    ((-1,0),(0,1)),
    ((-1,-1),(0,-1)),
    ((-1,1),(0,1)),
    ((0,-1),(1,0)),
    ((0,1),(1,0)),
    ((1,-1),(1,0)),
    ((1,0),(1,1)),
    ((0,-1),(1,-1)),
    ((0,1),(1,1))
]

def readline():
    return raw_input()


def get_coverable_panels(board, current_pos, taken, height, width, i):
    """
    Get coverable adjacent panels from current position.

    Args:
        board: a list representing the board to cover
        current_pos: a tuple representing position of current panel
        taken: a dictionary which tracks whether each panel is taken for covering
        height: height of the board
        width: width of the board
        i: index to get adjacent panels
    Returns:
        a tuple of coverable adjacent panels,
        or None if there is no coverable panels
    """
    # get two adjacent panels to current panel
    panel_1 = (current_pos[0]+adjacent_panels[i][0][0], current_pos[1]+adjacent_panels[i][0][1])
    panel_2 = (current_pos[0]+adjacent_panels[i][1][0], current_pos[1]+adjacent_panels[i][1][1])
    # if adjacent panel is out of the board, return None
    if panel_1[0] >= height or panel_1[0] < 0 or panel_2[0] >= height or panel_2[0] < 0:
        return None
    if panel_1[1] >= width or panel_1[1] < 0 or panel_2[1] >= width or panel_2[1] < 0:
        return None
    # if adjacent panel is already taken, return None
    if board[panel_1[0]][panel_1[1]] == '#' or taken[panel_1]:
        return None
    elif board[panel_2[0]][panel_2[1]] == '#' or taken[panel_2]:
        return None
    # if adjacent panels are available, then return them
    else:
        return (panel_1, panel_2)


def cover(board, taken, height, width):
    """
    Recursively find all possible way to cover the board.

    Args:
        board: a list representing the board to cover
        taken: a dictionary which tracks whether each panel is taken for covering
        height: height of the board
        width: width of the board
    Returns:
        a number of all possible way to cover the board
    """
    # find a panel that hasn't been taken yet
    current_pos = None
    for row_i in range(height):
        for col_i in range(width):
            if board[row_i][col_i] != '#' and not taken[(row_i,col_i)]:
                current_pos = (row_i, col_i)
                break
        if current_pos:
            break
    # if there is no panel to select,
    # then it means we found a way to cover the board, so return 1
    if current_pos == None:
        return 1
    # recursively find all possible way to cover the board
    count = 0
    for i in range(12):
        coverable_panels = get_coverable_panels(board, current_pos, taken, height, width, i)
        if coverable_panels != None:
            taken[coverable_panels[0]] = taken[coverable_panels[1]] = taken[current_pos] = True
            count += cover(board, taken, height, width)
            taken[coverable_panels[0]] = taken[coverable_panels[1]] = taken[current_pos] = False
    return count


def boardcover():
    total_tests = int(readline())
    for testcase in range(total_tests):
        height, width = map(int, readline().split())
        board = []
        num_of_white = 0
        for row_i in range(height):
            row = readline()
            num_of_white += row.count('.')
            board.append(row)
        # if number of white panel is not divisible by 3,
        # then the board can not be covered
        if num_of_white % 3 != 0:
            print 0
        # find all possible way to cover the board
        else:
            taken = defaultdict(bool)
            print cover(board, taken, height, width)


if __name__ == '__main__':
    boardcover()  # run