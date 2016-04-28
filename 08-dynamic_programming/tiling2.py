# Problem ID: TILING2
# https://algospot.com/judge/problem/read/TILING2
# took 35ms

from collections import defaultdict

def readline():
    return raw_input()


def get_tilings(width, tiledict):
    if width <= 1:
        return 1
    result = tiledict[width]
    if result != -1:
        return result
    result = tiledict[width] = (get_tilings(width-2, tiledict) + get_tilings(width-1, tiledict)) % 1000000007
    return result


def tiling():
    total_tests = int(readline())
    for testcase in range(total_tests):
        width = int(readline())
        tiledict = defaultdict(lambda:-1)
        print get_tilings(width, tiledict)


if __name__ == '__main__':
    tiling()  # run