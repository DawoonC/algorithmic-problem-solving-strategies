# Problem ID: PALINDROMIZE
# https://algospot.com/judge/problem/read/PALINDROMIZE
# took 1616ms

from get_max_overlap import get_max_overlap


def readline():
    return raw_input()


def palindromize():
    total_tests = int(readline())
    for testcase in range(total_tests):
        s = readline()
        rs = s[::-1]
        max_overlap = get_max_overlap(s, rs)
        remain = len(s) - max_overlap
        print (remain * 2) + max_overlap


if __name__ == '__main__':
    palindromize()  # run
