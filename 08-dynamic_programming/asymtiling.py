# Problem ID: ASYMTILING
# https://algospot.com/judge/problem/read/ASYMTILING
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


def get_nonasym_tilings(width, tiledict, MOD):
    if width % 2 == 1:
        return (get_tilings(width, tiledict) - get_tilings(width/2, tiledict) + MOD) % MOD
    result = get_tilings(width, tiledict)
    result = (result - get_tilings(width/2, tiledict) + MOD) % MOD
    result = (result - get_tilings(width/2-1, tiledict) + MOD) % MOD
    return result


def asymtiling():
    MOD = 1000000007
    total_tests = int(readline())
    for testcase in range(total_tests):
        width = int(readline())
        tiledict = defaultdict(lambda:-1)
        print get_nonasym_tilings(width, tiledict, MOD)


if __name__ == '__main__':
    asymtiling()  # run