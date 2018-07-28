# Problem ID: PALINDROMIZE
# https://algospot.com/judge/problem/read/PALINDROMIZE
# took 1616ms

from get_partial_match import get_partial_match


def readline():
    return raw_input()


def get_max_overlap(a, b):
    n, m = len(a), len(b)
    begin, matched = 0, 0
    pi = get_partial_match(b)
    while begin < n:
        if matched < m and a[begin + matched] == b[matched]:
            matched += 1
            if (begin + matched) == n:
                return matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += (matched - pi[matched - 1])
                matched = pi[matched - 1]
    return 0


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
