# Problem ID: HANOI4B
# https://algospot.com/judge/problem/read/HANOI4B

from collections import defaultdict

def readline():
    return raw_input()


def _get(state, index):
    return (state >> (index * 2)) & 3


def _set(state, index, value):
    return (state & ~(3 << (index * 2))) | (value << (index * 2))


def sgn(x):
    if not x:
        return 0
    return 1 if x > 0 else -1


def incr(x):
    if x < 0:
        return x - 1
    return x + 1


def bidir_search(discs, begin, end):
    if begin == end:
        return 0
    queue = []
    queue.append(begin)
    queue.append(end)
    c = defaultdict(int)
    c[begin] = 1
    c[end] = -1
    disc_range = range(discs-1, -1, -1)
    pole_range = range(4)
    while len(queue) != 0:
        here = queue.pop(0)
        top = [-1,-1,-1,-1]
        for i in disc_range:
            top[_get(here, i)] = i
        for i in pole_range:
            if top[i] != -1:
                for j in pole_range:
                    if i != j and (top[j] == -1 or top[j] > top[i]):
                        there = _set(here, top[i], j)
                        if c[there] == 0:
                            c[there] = incr(c[here])
                        elif sgn(c[there]) != sgn(c[here]):
                            return abs(c[there]) + abs(c[here]) - 1
    return -1


# TODO
def hanoi4b():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        for i in range(4):
            readline()
        for i in range(4):
            readline()


if __name__ == '__main__':
    hanoi4b()  # run
