# Problem ID: DRAGON
# https://algospot.com/judge/problem/read/DRAGON
# took 64ms

from collections import defaultdict

CONSTANTS = {
    'MAX': 1000000000 + 1,
    'EXPAND_X': 'X+YF',
    'EXPAND_Y': 'FX-Y',
}


def readline():
    return raw_input()


# brute force way
def make_curve(seed, generation, curve):
    if generation == 0:
        curve.append(seed)
        return
    for c in seed:
        if c == 'X':
            make_curve(CONSTANTS['EXPAND_X'], generation - 1, curve)
        elif c == 'Y':
            make_curve(CONSTANTS['EXPAND_Y'], generation - 1, curve)
        else:
            curve.append(c)


def precalc():
    cache = defaultdict(lambda: None)
    cache[0] = 1
    for i in range(1, 51):
        # length(n): length after expanding n generation
        # x_length(n) = x_length(n-1) + y_length(n-1) + 2
        # y_length(n) = x_length(n-1) + y_length(n-1) + 2
        # length(n) = length(n-1) * 2 + 2
        cache[i] = min(CONSTANTS['MAX'], cache[i - 1] * 2 + 2)
    return cache


def get_pth_char(seed, generation, skip, cache):
    if generation == 0:
        return seed[skip]
    for i in range(len(seed)):
        if seed[i] == 'X' or seed[i] == 'Y':
            if skip >= cache[generation]:
                skip -= cache[generation]
            elif seed[i] == 'X':
                return get_pth_char(CONSTANTS['EXPAND_X'], generation - 1, skip, cache)
            else:
                return get_pth_char(CONSTANTS['EXPAND_Y'], generation - 1, skip, cache)
        elif skip > 0:
            skip -= 1
        else:
            return seed[i]
    return seed[skip]


def dragon():
    total_tests = int(readline())
    seed = 'FX'
    cache = precalc()
    for testcase in range(total_tests):
        n, p, l = map(int, readline().split())
        curve = []
        for skip in range(p - 1, p + l - 1):
            pth = get_pth_char(seed, n, skip, cache)
            curve.append(pth)
        print (''.join(curve))


if __name__ == '__main__':
    dragon()  # run
