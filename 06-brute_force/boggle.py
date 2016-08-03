# Problem ID: BOGGLE
# https://algospot.com/judge/problem/read/BOGGLE

import sys
from collections import defaultdict

def get_upper_left(board, current_pos):
    """
    Get value and location of upper left of the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[0] == 0 or current_pos[1] == 0):
        return None
    else:
        return (board[current_pos[0]-1][current_pos[1]-1], (current_pos[0]-1, current_pos[1]-1))


def get_upper(board, current_pos):
    """
    Get value and location above the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[0] == 0):
        return None
    else:
        return (board[current_pos[0]-1][current_pos[1]], (current_pos[0]-1, current_pos[1]))


def get_upper_right(board, current_pos):
    """
    Get value and location of upper right of the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[0] == 0 or current_pos[1] == 4):
        return None
    else:
        return (board[current_pos[0]-1][current_pos[1]+1], (current_pos[0]-1, current_pos[1]+1))


def get_left(board, current_pos):
    """
    Get value and location of left of the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[1] == 0):
        return None
    else:
        return (board[current_pos[0]][current_pos[1]-1], (current_pos[0], current_pos[1]-1))


def get_right(board, current_pos):
    """
    Get value and location of right of the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[1] == 4):
        return None
    else:
        return (board[current_pos[0]][current_pos[1]+1], (current_pos[0], current_pos[1]+1))


def get_lower_left(board, current_pos):
    """
    Get value and location of lower left of the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[0] == 4 or current_pos[1] == 0):
        return None
    else:
        return (board[current_pos[0]+1][current_pos[1]-1], (current_pos[0]+1, current_pos[1]-1))


def get_lower(board, current_pos):
    """
    Get value and location below the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[0] == 4):
        return None
    else:
        return (board[current_pos[0]+1][current_pos[1]], (current_pos[0]+1, current_pos[1]))


def get_lower_right(board, current_pos):
    """
    Get value and location of lower right of the current position.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
    Returns:
        A tuple containing the value of the next position and location of the next position,
        or None if there is no next position.
        example:
            ('A', (2,2))
    """
    if (current_pos[0] == 4 or current_pos[1] == 4):
        return None
    else:
        return (board[current_pos[0]+1][current_pos[1]+1], (current_pos[0]+1,current_pos[1]+1))


pos_getters = [
    get_upper_left,
    get_upper,
    get_upper_right,
    get_left,
    get_right,
    get_lower_left,
    get_lower,
    get_lower_right
]


def check_char_match(board, current_pos, word, boggle_dict):
    """
    Recursively checks if the word matches characters in the board.

    Args:
        board: list of strings representing each row in the board
        current_pos: a tuple containing current position in the board (row_index, col_index)
        word: a word to find from the board
    Returns:
        True if there is a matching characters in the board
        False if not
    """
    if word == '':
        return True
    result = boggle_dict[(current_pos[0],current_pos[1],word)]
    if result != None:
        return result
    for pos_getter in pos_getters:
        next = pos_getter(board, current_pos)
        if next and next[0] == word[0]:
            result = boggle_dict[(current_pos[0],current_pos[1],word)] = check_char_match(board, next[1], word[1:], boggle_dict)
            if result:
                return True
    return False


def check_word_exist(board, word, boggle_dict):
    """
    Checks if the word exists in the board.

    Args:
        board: list of strings representing each row in the board
        word: a word to find from the board
    Returns:
        True if the word exists in the board
        False if not
    """
    for row in range(5):
        for col in range(5):
            if board[row][col] == word[0]:
                result = boggle_dict[(row,col,word)]
                if result != None:
                    return result
                result = boggle_dict[(row,col,word)] = check_char_match(board, (row, col), word[1:], boggle_dict)
                if result:
                    return True
    return False


def readline():
    return raw_input()


def boggle():
    total_tests = int(readline())
    for testcase in range(total_tests):
        board = []
        for row in range(5):
            board.append(readline())
        total_words = int(readline())
        for i in range(total_words):
            word = readline()
            boggle_dict = defaultdict(lambda: None)
            result = check_word_exist(board, word, boggle_dict)
            if result:
                print word, 'YES'
            else:
                print word, 'NO'


if __name__ == '__main__':
    boggle()  # run