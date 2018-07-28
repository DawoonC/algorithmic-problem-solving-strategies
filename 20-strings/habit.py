# Problem ID: HABIT
# https://algospot.com/judge/problem/read/HABIT
# took > 1000ms

from create_suffix_array import create_suffix_array


def readline():
    return raw_input()


def get_common_prefix(s, n, a, b):
    k = 0
    i, j = a, b
    while i < n and j < n and s[i] == s[j]:
        i += 1
        j += 1
        k += 1
    return k


def get_longest_frequent(s, k):
    sa = create_suffix_array(s)
    n = len(s)
    result = 0
    for i in xrange(n - k + 1):
        result = max(result, get_common_prefix(s, n, sa[i], sa[i + k - 1]))
    return result


def habit():
    total_tests = int(readline())
    for testcase in range(total_tests):
        k = int(readline())
        s = readline()
        print get_longest_frequent(s, k)


if __name__ == '__main__':
    habit()  # run
